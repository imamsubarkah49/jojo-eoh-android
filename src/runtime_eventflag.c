/* Kernel event flags: 32-bit handles over a 64-bit bit pattern.
 * The CyberConnect2 boot path creates a flag and waits for OR/AND bits.
 * Waiters are woken by broadcast; the timeout is in microseconds. */
#define _GNU_SOURCE
#include "runtime.h"
#include <errno.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define ERR(n) ((int32_t)(UINT32_C(0x80020000)|(n)))

typedef struct EventFlag {
    uint32_t id, attr;
    uint64_t bits;
    int deleted;
    pthread_cond_t cv;
    struct EventFlag *next;
} EventFlag;

static pthread_mutex_t lock=PTHREAD_MUTEX_INITIALIZER;
static EventFlag *registry;
static uint32_t next_id=1;

static EventFlag *find_locked(uint32_t id) {
    for (EventFlag *e=registry;e;e=e->next) if (e->id==id && !e->deleted) return e;
    return NULL;
}
static int matches(const EventFlag *e,uint64_t want,uint32_t mode) {
    if (!want) return 0;
    return (mode & 2) ? (e->bits & want)!=0 : (e->bits & want)==want;
}
static void consume(EventFlag *e,uint64_t want,uint32_t mode) {
    if (!(mode & 0x10)) return;
    e->bits &= (mode & 2) ? ~(e->bits & want) : ~want;
}
static ABI int32_t evf_create(const char *name,uint32_t attr,uint64_t initial,const void *options) {
    (void)options;
    if (!name) return ERR(22);
    EventFlag *e=calloc(1,sizeof(*e));
    if (!e) return ERR(12);
    if (pthread_cond_init(&e->cv,NULL)) { free(e); return ERR(12); }
    e->attr=attr;
    e->bits=initial;
    pthread_mutex_lock(&lock);
    e->id=next_id++;
    e->next=registry;
    registry=e;
    printf("Runtime: event flag id=%u, attr=%u, bits=%llx\n",e->id,attr,
           (unsigned long long)initial);
    pthread_mutex_unlock(&lock);
    return (int32_t)e->id;
}
static ABI int32_t evf_wait(uint32_t id,uint64_t want,uint32_t mode,uint64_t *result,uint32_t *timeout) {
    if (!result || !want) return ERR(22);
    pthread_mutex_lock(&lock);
    EventFlag *e=find_locked(id);
    if (!e) { pthread_mutex_unlock(&lock); return ERR(3); }
    if (matches(e,want,mode)) {
        *result=e->bits;
        consume(e,want,mode);
        pthread_mutex_unlock(&lock);
        return 0;
    }
    if (timeout && *timeout==0) { pthread_mutex_unlock(&lock); return ERR(60); }
    struct timespec deadline={0};
    if (timeout) {
        clock_gettime(CLOCK_REALTIME,&deadline);
        deadline.tv_sec += *timeout/1000000;
        deadline.tv_nsec += (long)(*timeout%1000000)*1000;
        if (deadline.tv_nsec>=1000000000) { deadline.tv_sec++; deadline.tv_nsec-=1000000000; }
    }
    int rc=0;
    while (!matches(e,want,mode)) {
        rc = timeout ? pthread_cond_timedwait(&e->cv,&lock,&deadline)
                     : pthread_cond_wait(&e->cv,&lock);
        if (e->deleted) { pthread_mutex_unlock(&lock); return ERR(3); }
        if (rc==ETIMEDOUT) { pthread_mutex_unlock(&lock); return ERR(60); }
        if (rc) { fprintf(stderr,"STOP: event flag wait error %d\n",rc); exit(21); }
    }
    *result=e->bits;
    consume(e,want,mode);
    if (timeout) *timeout=0;
    pthread_mutex_unlock(&lock);
    return 0;
}
static ABI int32_t evf_poll(uint32_t id,uint64_t want,uint32_t mode,uint64_t *result) {
    if (!result || !want) return ERR(22);
    pthread_mutex_lock(&lock);
    EventFlag *e=find_locked(id);
    if (!e) { pthread_mutex_unlock(&lock); return ERR(3); }
    if (!matches(e,want,mode)) { pthread_mutex_unlock(&lock); return ERR(16); }
    *result=e->bits;
    consume(e,want,mode);
    pthread_mutex_unlock(&lock);
    return 0;
}
static ABI int32_t evf_set(uint32_t id,uint64_t bits) {
    pthread_mutex_lock(&lock);
    EventFlag *e=find_locked(id);
    if (!e) { pthread_mutex_unlock(&lock); return ERR(3); }
    e->bits |= bits;
    pthread_cond_broadcast(&e->cv);
    pthread_mutex_unlock(&lock);
    return 0;
}
static ABI int32_t evf_clear(uint32_t id,uint64_t bits) {
    pthread_mutex_lock(&lock);
    EventFlag *e=find_locked(id);
    if (!e) { pthread_mutex_unlock(&lock); return ERR(3); }
    e->bits &= ~bits;
    pthread_mutex_unlock(&lock);
    return 0;
}
static ABI int32_t evf_delete(uint32_t id) {
    pthread_mutex_lock(&lock);
    EventFlag *e=find_locked(id);
    if (!e) { pthread_mutex_unlock(&lock); return ERR(3); }
    e->deleted=1;
    pthread_cond_broadcast(&e->cv);
    pthread_mutex_unlock(&lock);
    return 0;
}
static ABI int32_t evf_cancel(uint32_t id,uint64_t bits,int32_t *waiters) {
    pthread_mutex_lock(&lock);
    EventFlag *e=find_locked(id);
    if (!e) { pthread_mutex_unlock(&lock); return ERR(3); }
    e->bits=bits;
    if (waiters) *waiters=0;
    pthread_cond_broadcast(&e->cv);
    pthread_mutex_unlock(&lock);
    return 0;
}
static ABI int32_t evf_close(uint32_t id) { (void)id; return 0; }
static ABI int32_t evf_open(const char *name,uint32_t attr,uint32_t *out) {
    (void)attr;
    if (!name || !out) return ERR(22);
    pthread_mutex_lock(&lock);
    for (EventFlag *e=registry;e;e=e->next)
        if (!e->deleted) { *out=e->id; pthread_mutex_unlock(&lock); return 0; }
    pthread_mutex_unlock(&lock);
    return ERR(2);
}

uintptr_t runtime_eventflag_resolve(const char *name) {
    static const struct { const char *nid; void *fn; } table[]={
        {"BpFoboUJoZU#libkernel",evf_create},
        {"JTvBflhYazQ#libkernel",evf_wait},
        {"9lvj5DjHZiA#libkernel",evf_poll},
        {"IOnSvHzqu6A#libkernel",evf_set},
        {"7uhBFWRAS60#libkernel",evf_clear},
        {"8mql9OcQnd4#libkernel",evf_delete},
        {"PZku4ZrXJqg#libkernel",evf_cancel},
        {"s9-RaxukuzQ#libkernel",evf_close},
        {"1vDaenmJtyA#libkernel",evf_open},
    };
    for (size_t i=0;i<sizeof(table)/sizeof(*table);++i)
        if (!strcmp(name,table[i].nid)) return (uintptr_t)table[i].fn;
    return 0;
}
