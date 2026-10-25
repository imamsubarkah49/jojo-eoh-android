# JoJo EoH import coverage

Source log: `docs/jojo-shad-log.txt`
Known NIDs in `src/import_names.inc`: **778**
Unique imports in the log: **336**
Imports with no matching NID: **151** (84 system/HLE, 67 native)

## Imports by library

| Library | Unique imports |
|---|---:|
| `libc` | 203 |
| `libSceNpUtility` | 17 |
| `libSceNpMatching2` | 16 |
| `libkernel` | 15 |
| `libSceVoiceQoS` | 13 |
| `libSceLibcInternal` | 13 |
| `libSceNpManager` | 11 |
| `libSceRtc` | 11 |
| `libSceInvitationDialog` | 6 |
| `libSceNpFriendListDialog` | 5 |
| `libSceGameCustomDataDialog` | 5 |
| `libSceJpegDec` | 5 |
| `libSceNpSnsFacebookDialog` | 4 |
| `libSceJpegEnc` | 4 |
| `libScePngEnc` | 4 |
| `libSceNpSns` | 3 |
| `libSceVideoRecording` | 1 |

## Missing system NIDs (need an HLE implementation or a deliberate stub)

| NID | Library | Symbol |
|---|---|---|
| `sJptZwvs1is` | `libSceGameCustomDataDialog` | `sceGameCustomDataDialogGetResult` |
| `xtbb-2f703A` | `libSceGameCustomDataDialog` | `sceGameCustomDataDialogInitialize` |
| `5TvttyRuU84` | `libSceGameCustomDataDialog` | `sceGameCustomDataDialogOpen` |
| `HwEtHFCpU5U` | `libSceGameCustomDataDialog` | `sceGameCustomDataDialogTerminate` |
| `PkdLsRA4ON0` | `libSceGameCustomDataDialog` | `sceGameCustomDataDialogUpdateStatus` |
| `WWtCL5lzi7Y` | `libSceInvitationDialog` | `sceInvitationDialogClose` |
| `8XKR6wa64iQ` | `libSceInvitationDialog` | `sceInvitationDialogGetResult` |
| `XvA5KS56wcs` | `libSceInvitationDialog` | `sceInvitationDialogInitialize` |
| `0zU0G+wiVLA` | `libSceInvitationDialog` | `sceInvitationDialogOpen` |
| `B6HVJtDYxEE` | `libSceInvitationDialog` | `sceInvitationDialogTerminate` |
| `9+g9iOq+7kg` | `libSceInvitationDialog` | `sceInvitationDialogUpdateStatus` |
| `JPh3Zgg0Zwc` | `libSceJpegDec` | `sceJpegDecCreate` |
| `1kzQRoWEgSA` | `libSceJpegDec` | `sceJpegDecDecode` |
| `Hwh11+m5KoI` | `libSceJpegDec` | `sceJpegDecDelete` |
| `LSinoSQH790` | `libSceJpegDec` | `sceJpegDecParseHeader` |
| `uNAUmANZMEw` | `libSceJpegDec` | `sceJpegDecQueryMemorySize` |
| `K+rocojkr-I` | `libSceJpegEnc` | `sceJpegEncCreate` |
| `j1LyMdaM+C0` | `libSceJpegEnc` | `sceJpegEncDelete` |
| `QbrU0cUghEM` | `libSceJpegEnc` | `sceJpegEncEncode` |
| `o6ZgXfFdWXQ` | `libSceJpegEnc` | `sceJpegEncQueryMemorySize` |
| `+Y1acHGomGQ` | `libSceNpFriendListDialog` | `sceNpFriendListDialogClose` |
| `2L-W-ZYn2Qo` | `libSceNpFriendListDialog` | `sceNpFriendListDialogInitialize` |
| `zUM-RG5Hmyc` | `libSceNpFriendListDialog` | `sceNpFriendListDialogOpen` |
| `ECEzk+K9L2k` | `libSceNpFriendListDialog` | `sceNpFriendListDialogTerminate` |
| `frwz3eyuA6w` | `libSceNpFriendListDialog` | `sceNpFriendListDialogUpdateStatus` |
| `F6E4ycq9Dbg` | `libSceNpManager` | `sceNpGetUserIdByOnlineId` |
| `s4UEa5iBJdc` | `libSceNpManager` | `sceNpInGameMessageCreateHandle` |
| `+anuSx2avHQ` | `libSceNpManager` | `sceNpInGameMessageDeleteHandle` |
| `GFhVUpRmbHE` | `libSceNpManager` | `sceNpInGameMessageInitialize` |
| `Vh1bhUG6mSs` | `libSceNpManager` | `sceNpInGameMessagePrepare` |
| `ON7Sf5XEMmI` | `libSceNpManager` | `sceNpInGameMessageSendData` |
| `bMG3cVmUmuk` | `libSceNpManager` | `sceNpInGameMessageTerminate` |
| `26vWrPAWJfM` | `libSceNpMatching2` | `sceNpMatching2GetRoomDataExternalList` |
| `Jraxifmoet4` | `libSceNpMatching2` | `sceNpMatching2GetRoomDataInternal` |
| `dMQ+xGvTdqM` | `libSceNpMatching2` | `sceNpMatching2GetRoomMemberDataExternalList` |
| `5lhvOqheFBA` | `libSceNpMatching2` | `sceNpMatching2GetRoomMemberDataInternal` |
| `qeF-q5KDtAc` | `libSceNpMatching2` | `sceNpMatching2GetUserInfoList` |
| `uBESzz4CQws` | `libSceNpMatching2` | `sceNpMatching2RegisterRoomMessageCallback` |
| `opDpl74pi2E` | `libSceNpMatching2` | `sceNpMatching2SendRoomChatMessage` |
| `twVupeaYYrk` | `libSceNpMatching2` | `sceNpMatching2SignalingGetConnectionInfo` |
| `OoTjfxl8-wI` | `libSceNpSns` | `sceNpSnsFacebookCreateRequest` |
| `pTvAKV1iQkE` | `libSceNpSns` | `sceNpSnsFacebookDeleteRequest` |
| `VtyS8XLBqNE` | `libSceNpSns` | `sceNpSnsFacebookGetAccessToken` |
| `AifdcI1aKas` | `libSceNpSnsFacebookDialog` | `sceNpSnsFacebookDialogGetResult` |
| `tdQArULbNQk` | `libSceNpSnsFacebookDialog` | `sceNpSnsFacebookDialogInitialize` |
| `Hi3onqHSN6M` | `libSceNpSnsFacebookDialog` | `sceNpSnsFacebookDialogOpen` |
| `cdqOFyupRS4` | `libSceNpSnsFacebookDialog` | `sceNpSnsFacebookDialogTerminate` |
| `BYIZGKm6bO4` | `libSceNpUtility` | `sceNpBandwidthTestGetStatus` |
| `jktww3yJXnc` | `libSceNpUtility` | `sceNpBandwidthTestInitStart` |
| `pLr1fEQS1z8` | `libSceNpUtility` | `sceNpBandwidthTestShutdown` |
| `iQr9UxPHUFs` | `libSceNpUtility` | `sceNpLookupCreateRequest` |
| `rAOOqDAxBIk` | `libSceNpUtility` | `sceNpWordFilterAbortRequest` |
| `1dMndqL-QgE` | `libSceNpUtility` | `sceNpWordFilterCensorComment` |
| `IEB+vgVoQbw` | `libSceNpUtility` | `sceNpWordFilterCreateAsyncRequest` |
| `iCq5xW5KQW4` | `libSceNpUtility` | `sceNpWordFilterCreateRequest` |
| `r9BgI0PfJZg` | `libSceNpUtility` | `sceNpWordFilterCreateTitleCtx` |
| `PYFS1H70bDs` | `libSceNpUtility` | `sceNpWordFilterDeleteRequest` |
| `t0P5z5yuFPA` | `libSceNpUtility` | `sceNpWordFilterDeleteTitleCtx` |
| `ur5SShyG0dk` | `libSceNpUtility` | `sceNpWordFilterPollAsync` |
| `Jj4mkpFO2gE` | `libSceNpUtility` | `sceNpWordFilterSanitizeComment` |
| `7aGTPfrqT9s` | `libScePngEnc` | `scePngEncCreate` |
| `RUrWdwTWZy8` | `libScePngEnc` | `scePngEncDelete` |
| `xgDjJKpcyHo` | `libScePngEnc` | `scePngEncEncode` |
| `9030RnBDoh4` | `libScePngEnc` | `scePngEncQueryMemorySize` |
| `18B2NS1y9UU` | `libSceRtc` | `sceRtcGetCurrentTick` |
| `jfRO0uTjtzA` | `libSceRtc` | `sceRtcGetWin32FileTime` |
| `NxEI1KByvCI` | `libSceRtc` | `sceRtcParseDateTime` |
| `99bMGglFW3I` | `libSceRtc` | `sceRtcParseRFC3339` |
| `n5JiAJXsbcs` | `libSceRtc` | `sceRtcSetWin32FileTime` |
| `Fc8qxlKINYQ` | `libSceVideoRecording` | `sceVideoRecordingSetInfo` |
| `kLU6hhXsa2A` | `libSceVoiceQoS` | `sceVoiceQoSConnect` |
| `lvNClhNHzxI` | `libSceVoiceQoS` | `sceVoiceQoSCreateLocalEndpoint` |
| `iqQQW2cBmWU` | `libSceVoiceQoS` | `sceVoiceQoSCreateRemoteEndpoint` |
| `kE0kdvcHTiY` | `libSceVoiceQoS` | `sceVoiceQoSDeleteLocalEndpoint` |
| `H4zqFaDhHW4` | `libSceVoiceQoS` | `sceVoiceQoSDeleteRemoteEndpoint` |
| `j9Xt85krooc` | `libSceVoiceQoS` | `sceVoiceQoSDisconnect` |
| `ATRGkmbolVM` | `libSceVoiceQoS` | `sceVoiceQoSEnd` |
| `eZu2RP0Ma3w` | `libSceVoiceQoS` | `sceVoiceQoSGetLocalEndpointAttribute` |
| `Trpt2QBZHCI` | `libSceVoiceQoS` | `sceVoiceQoSGetStatus` |
| `U8IfNl6-Css` | `libSceVoiceQoS` | `sceVoiceQoSInit` |
| `PWokFqab5q4` | `libSceVoiceQoS` | `sceVoiceQoSReadPacket` |
| `F7wS7FbfumQ` | `libSceVoiceQoS` | `sceVoiceQoSSetLocalEndpointAttribute` |
| `SpxLratrO1Q` | `libSceVoiceQoS` | `sceVoiceQoSWritePacket` |
| `UtszJWHrDcA` | `libkernel` | `sceKernelFchmod` |

## Missing native NIDs (libc / libc internal / Fios2)

These are normally supplied by the game's bundled `libc.prx` or `libSceFios2.prx`; a missing name here usually means the linker did not see the module, not that the game needs a new runtime function.

| NID | Library | Symbol |
|---|---|---|
| `2sWzhYqFH4E` | `libSceLibcInternal` | `_Stdout` |
| `H2e8t5ScQGc` | `libSceLibcInternal` | `__cxa_finalize` |
| `tIhsqj0qsFE` | `libSceLibcInternal` | `free` |
| `1mecP7RgI2A` | `libSceLibcInternal` | `gmtime` |
| `5bBacGLyLOs` | `libSceLibcInternal` | `gmtime_s` |
| `efhK-YSUYYQ` | `libSceLibcInternal` | `localtime` |
| `gQX+4GDQjpM` | `libSceLibcInternal` | `malloc` |
| `n7AepwR0s34` | `libSceLibcInternal` | `mktime` |
| `hcuQgD53UxM` | `libSceLibcInternal` | `printf` |
| `wLlFkwG9UcQ` | `libSceLibcInternal` | `time` |
| `GMpvxPFW924` | `libSceLibcInternal` | `vprintf` |
| `Q2V+iqvjgC0` | `libSceLibcInternal` | `vsnprintf` |
| `KeOZ19X8-Ug` | `libc` | `_Cosh` |
| `wZi5ly2guNw` | `libc` | `_Exit` |
| `mnufPlYbnN0` | `libc` | `_FDtest` |
| `U52BlHBvYvE` | `libc` | `_Getmbcurmax` |
| `QxqK-IdpumU` | `libc` | `_Getpmbstate` |
| `zS94yyJRSUs` | `libc` | `_Getpwcstate` |
| `vZkmJmvqueY` | `libc` | `_Lockfilelock` |
| `-9SIhUr4Iuo` | `libc` | `_Mbtowcx` |
| `MU25eqxSDTw` | `libc` | `_Sinh` |
| `QlcJbyd6jxM` | `libc` | `_Stodx` |
| `7dlAxeH-htg` | `libc` | `_Stofx` |
| `BKidCxmLC5w` | `libc` | `_Stoldx` |
| `mOnfZ5aNDQE` | `libc` | `_Stollx` |
| `Ecwid6wJMhY` | `libc` | `_Stolx` |
| `pSpDCDyxkaY` | `libc` | `_Stoullx` |
| `YDnLaav6W6Q` | `libc` | `_Stoulx` |
| `0x7rx8TKy2Y` | `libc` | `_Unlockfilelock` |
| `stv1S3BKfgw` | `libc` | `_Wctombx` |
| `LTov9gMEqCU` | `libc` | `_ZNSt8ios_base7_AddstdEPS_` |
| `P8F2oavZXtY` | `libc` | `_ZNSt8ios_baseD2Ev` |
| `1h8hFQghR7w` | `libc` | `_ZSt12setprecisioni` |
| `Qoo175Ig+-k` | `libc` | `_ZSt21_sceLibcClassicLocale` |
| `wiR+rIcbnlc` | `libc` | `_ZSt4_Fpz` |
| `vU9svJtEnWc` | `libc` | `_ZSt4setwi` |
| `vYWK2Pz8vGE` | `libc` | `_ZSt7_FiopenPKcNSt5_IosbIiE9_OpenmodeEi` |
| `dCzeFfg9WWI` | `libc` | `_ZTVSt9exception` |
| `Ye20uNnlglA` | `libc` | `abs` |
| `NesIgTmfF0Q` | `libc` | `bsearch` |
| `fmT2cjPoWBs` | `libc` | `fabsf` |
| `fiOgmWkP+Xc` | `libc` | `fmax` |
| `iU0z6SdUNbI` | `libc` | `fmin` |
| `NL836gOLANs` | `libc` | `fopen_s` |
| `7PkSz+qnTto` | `libc` | `fsetpos` |
| `aX8H2+BBlWE` | `libc` | `ldexpl` |
| `KuOuD58hqn4` | `libc` | `malloc_stats_fast` |
| `tdcAqgCS+uI` | `libc` | `mbstowcs_s` |
| `NFLs+dRJGNg` | `libc` | `memcpy_s` |
| `DDHG1a6+3q0` | `libc` | `roundf` |
| `LYo3GhIlB38` | `libc` | `sceLibcMspaceCalloc` |
| `-hn1tcVHq5Q` | `libc` | `sceLibcMspaceCreate` |
| `W6SiVSiCDtI` | `libc` | `sceLibcMspaceDestroy` |
| `Vla-Z+eXlxo` | `libc` | `sceLibcMspaceFree` |
| `OJjm-QOIHlI` | `libc` | `sceLibcMspaceMalloc` |
| `k04jLXu3+Ic` | `libc` | `sceLibcMspaceMallocStatsFast` |
| `iF1iQHzxBJU` | `libc` | `sceLibcMspaceMemalign` |
| `gigoVHZvVPE` | `libc` | `sceLibcMspaceRealloc` |
| `p6lrRW8-MLY` | `libc` | `sceLibcMspaceReallocalign` |
| `Q+xU11-h0xQ` | `libc` | `sqrtf` |
| `5Xa2ACNECdo` | `libc` | `strcpy_s` |
| `YNzNkJzYqEg` | `libc` | `strncpy_s` |
| `DQbtGaBKlaw` | `libc` | `strnlen_s` |
| `JM4EBvWT9rc` | `libc` | `tanh` |
| `rWSuTWY2JN0` | `libc` | `vsnprintf_s` |
| `6f5f-qx4ucA` | `libc` | `wcscpy_s` |
| `sZLrjx-yEx4` | `libc` | `wcstombs_s` |
