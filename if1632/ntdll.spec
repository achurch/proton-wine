name	ntdll
type	win32

001 stub CsrAllocateCaptureBuffer
002 stub CsrAllocateCapturePointer
003 stub CsrAllocateMessagePointer
004 stub CsrCaptureMessageBuffer
005 stub CsrCaptureMessageString
006 stub CsrCaptureTimeout
007 stub CsrClientCallServer
008 stub CsrClientConnectToServer
009 stub CsrClientMaxMessage
010 stub CsrClientSendMessage
011 stub CsrClientThreadConnect
012 stub CsrFreeCaptureBuffer
013 stub CsrIdentifyAlertableThread
014 stub CsrNewThread
015 stub CsrProbeForRead
016 stub CsrProbeForWrite
017 stub CsrSetPriorityClass
018 stub CsrpProcessCallbackRequest
019 stub DbgBreakPoint
020 stub DbgPrint
021 stub DbgPrompt
022 stub DbgSsHandleKmApiMsg
023 stub DbgSsInitialize
024 stub DbgUiConnectToDbg
025 stub DbgUiContinue
026 stub DbgUiWaitStateChange
027 stub DbgUserBreakPoint
028 stub KiUserApcDispatcher
029 stub KiUserCallbackDispatcher
030 stub KiUserExceptionDispatcher
031 stub LdrAccessResource
032 stub LdrDisableThreadCalloutsForDll
033 stub LdrEnumResources
034 stub LdrFindEntryForAddress
035 stub LdrFindResourceDirectory_U
036 stub LdrFindResource_U
037 stub LdrGetDllHandle
038 stub LdrGetProcedureAddress
039 stub LdrInitializeThunk
040 stub LdrLoadDll
041 stub LdrProcessRelocationBlock
042 stub LdrQueryImageFileExecutionOptions
043 stub LdrQueryProcessModuleInformation
044 stub LdrShutdownProcess
045 stub LdrShutdownThread
046 stub LdrUnloadDll
047 stub LdrVerifyImageMatchesChecksum
048 stub NPXEMULATORTABLE
049 stub NlsMbCodePageTag
050 stub NlsMbOemCodePageTag
051 stub NtAcceptConnectPort
052 stub NtAccessCheck
053 stub NtAccessCheckAndAuditAlarm
054 stub NtAdjustGroupsToken
055 stub NtAdjustPrivilegesToken
056 stub NtAlertResumeThread
057 stub NtAlertThread
058 stub NtAllocateLocallyUniqueId
059 stub NtAllocateUuids
060 stub NtAllocateVirtualMemory
061 stub NtCallbackReturn
062 stub NtCancelIoFile
063 stub NtCancelTimer
064 stub NtClearEvent
065 stub NtClose
066 stub NtCloseObjectAuditAlarm
067 stub NtCompleteConnectPort
068 stub NtConnectPort
069 stub NtContinue
070 stub NtCreateDirectoryObject
071 stub NtCreateEvent
072 stub NtCreateEventPair
073 stub NtCreateFile
074 stub NtCreateIoCompletion
075 stub NtCreateKey
076 stub NtCreateMailslotFile
077 stub NtCreateMutant
078 stub NtCreateNamedPipeFile
079 stub NtCreatePagingFile
080 stub NtCreatePort
081 stub NtCreateProcess
082 stub NtCreateProfile
083 stub NtCreateSection
084 stub NtCreateSemaphore
085 stub NtCreateSymbolicLinkObject
086 stub NtCreateThread
087 stub NtCreateTimer
088 stub NtCreateToken
089 register NtCurrentTeb() NtCurrentTeb
090 stub NtDelayExecution
091 stub NtDeleteFile
092 stub NtDeleteKey
093 stub NtDeleteValueKey
094 stub NtDeviceIoControlFile
095 stub NtDisplayString
096 stub NtDuplicateObject
097 stub NtDuplicateToken
098 stub NtEnumerateBus
099 stub NtEnumerateKey
100 stub NtEnumerateValueKey
101 stub NtExtendSection
102 stub NtFlushBuffersFile
103 stub NtFlushInstructionCache
104 stub NtFlushKey
105 stub NtFlushVirtualMemory
106 stub NtFlushWriteBuffer
107 stub NtFreeVirtualMemory
108 stub NtFsControlFile
109 stub NtGetContextThread
110 stub NtGetPlugPlayEvent
111 stub NtGetTickCount
112 stub NtImpersonateClientOfPort
113 stub NtImpersonateThread
114 stub NtInitializeRegistry
115 stub NtListenPort
116 stub NtLoadDriver
117 stub NtLoadKey
118 stub NtLockFile
119 stub NtLockVirtualMemory
120 stub NtMakeTemporaryObject
121 stub NtMapViewOfSection
122 stub NtNotifyChangeDirectoryFile
123 stub NtNotifyChangeKey
124 stub NtOpenDirectoryObject
125 stub NtOpenEvent
126 stub NtOpenEventPair
127 stdcall NtOpenFile(ptr long ptr ptr long long) NtOpenFile
128 stub NtOpenIoCompletion
129 stub NtOpenKey
130 stub NtOpenMutant
131 stub NtOpenObjectAuditAlarm
132 stub NtOpenProcess
133 stub NtOpenProcessToken
134 stub NtOpenSection
135 stub NtOpenSemaphore
136 stub NtOpenSymbolicLinkObject
137 stub NtOpenThread
138 stub NtOpenThreadToken
139 stub NtOpenTimer
140 stub NtPlugPlayControl
141 stub NtPrivilegeCheck
142 stub NtPrivilegeObjectAuditAlarm
143 stub NtPrivilegedServiceAuditAlarm
144 stub NtProtectVirtualMemory
145 stub NtPulseEvent
146 stub NtQueryAttributesFile
147 stub NtQueryDefaultLocale
148 stub NtQueryDirectoryFile
149 stub NtQueryDirectoryObject
150 stub NtQueryEaFile
151 stub NtQueryEvent
152 stub NtQueryInformationFile
153 stub NtQueryInformationPort
154 stub NtQueryInformationProcess
155 stub NtQueryInformationThread
156 stub NtQueryInformationToken
157 stub NtQueryIntervalProfile
158 stub NtQueryIoCompletion
159 stub NtQueryKey
160 stub NtQueryMutant
161 stub NtQueryObject
162 stub NtQueryPerformanceCounter
163 stub NtQuerySection
164 stub NtQuerySecurityObject
165 stub NtQuerySemaphore
166 stub NtQuerySymbolicLinkObject
167 stub NtQuerySystemEnvironmentValue
168 stub NtQuerySystemInformation
169 stub NtQuerySystemTime
170 stub NtQueryTimer
171 stub NtQueryTimerResolution
172 stub NtQueryValueKey
173 stub NtQueryVirtualMemory
174 stub NtQueryVolumeInformationFile
175 stub NtRaiseException
176 stub NtRaiseHardError
177 stub NtReadFile
178 stub NtReadRequestData
179 stub NtReadVirtualMemory
180 stub NtRegisterNewDevice
181 stub NtRegisterThreadTerminatePort
182 stub NtReleaseMutant
183 stub NtReleaseProcessMutant
184 stub NtReleaseSemaphore
185 stub NtRemoveIoCompletion
186 stub NtReplaceKey
187 stub NtReplyPort
188 stub NtReplyWaitReceivePort
189 stub NtReplyWaitReplyPort
190 stub NtRequestPort
191 stub NtRequestWaitReplyPort
192 stub NtResetEvent
193 stub NtRestoreKey
194 stub NtResumeThread
195 stub NtSaveKey
196 stub NtSetContextThread
197 stub NtSetDefaultHardErrorPort
198 stub NtSetDefaultLocale
199 stub NtSetEaFile
200 stub NtSetEvent
201 stub NtSetHighEventPair
202 stub NtSetHighWaitLowEventPair
203 stub NtSetHighWaitLowThread
204 stub NtSetInformationFile
205 stub NtSetInformationKey
206 stub NtSetInformationObject
207 stub NtSetInformationProcess
208 stub NtSetInformationThread
209 stub NtSetInformationToken
210 stub NtSetIntervalProfile
211 stub NtSetIoCompletion
212 stub NtSetLdtEntries
213 stub NtSetLowEventPair
214 stub NtSetLowWaitHighEventPair
215 stub NtSetLowWaitHighThread
216 stub NtSetSecurityObject
217 stub NtSetSystemEnvironmentValue
218 stub NtSetSystemInformation
219 stub NtSetSystemPowerState
220 stub NtSetSystemTime
221 stub NtSetTimer
222 stub NtSetTimerResolution
223 stub NtSetValueKey
224 stub NtSetVolumeInformationFile
225 stub NtShutdownSystem
226 stub NtStartProfile
227 stub NtStopProfile
228 stub NtSuspendThread
229 stub NtSystemDebugControl
230 stub NtTerminateProcess
231 stub NtTerminateThread
232 stub NtTestAlert
233 stub NtUnloadDriver
234 stub NtUnloadKey
235 stub NtUnlockFile
236 stub NtUnlockVirtualMemory
237 stub NtUnmapViewOfSection
238 stub NtVdmControl
239 stub NtW32Call
240 stub NtWaitForMultipleObjects
241 stub NtWaitForProcessMutant
242 stub NtWaitForSingleObject
243 stub NtWaitHighEventPair
244 stub NtWaitLowEventPair
245 stub NtWriteFile
246 stub NtWriteRequestData
247 stub NtWriteVirtualMemory
248 stub PfxFindPrefix
249 stub PfxInitialize
250 stub PfxInsertPrefix
251 stub PfxRemovePrefix
252 stub RestoreEm87Context
253 stub RtlAbortRXact
254 stub RtlAbsoluteToSelfRelativeSD
255 stub RtlAcquirePebLock
256 stub RtlAcquireResourceExclusive
257 stub RtlAcquireResourceShared
258 stub RtlAddAccessAllowedAce
259 stub RtlAddAccessDeniedAce
260 stdcall RtlAddAce(ptr long long ptr long) RtlAddAce
261 stub RtlAddActionToRXact
262 stub RtlAddAttributeActionToRXact
263 stub RtlAddAuditAccessAce
264 stub RtlAdjustPrivilege
265 stub RtlAllocateAndInitializeSid
266 stdcall RtlAllocateHeap(long long long) HeapAlloc
267 stub RtlAnsiCharToUnicodeChar
268 stub RtlAnsiStringToUnicodeSize
269 stdcall RtlAnsiStringToUnicodeString(ptr ptr long) RtlAnsiStringToUnicodeString
270 stub RtlAppendAsciizToString
271 stub RtlAppendStringToString
272 stub RtlAppendUnicodeStringToString
273 stub RtlAppendUnicodeToString
274 stub RtlApplyRXact
275 stub RtlApplyRXactNoFlush
276 stub RtlAreAllAccessesGranted
277 stub RtlAreAnyAccessesGranted
278 stub RtlAreBitsClear
279 stub RtlAreBitsSet
280 stub RtlAssert
281 stub RtlCaptureStackBackTrace
282 stub RtlCharToInteger
283 stub RtlCheckRegistryKey
284 stub RtlClearAllBits
285 stub RtlClearBits
286 stub RtlCompactHeap
287 stub RtlCompareMemory
288 stub RtlCompareMemoryUlong
289 stub RtlCompareString
290 stub RtlCompareUnicodeString
291 stub RtlCompressBuffer
292 stub RtlConsoleMultiByteToUnicodeN
293 stub RtlConvertExclusiveToShared
294 stub RtlConvertLongToLargeInteger
295 stub RtlConvertSharedToExclusive
296 stub RtlConvertSidToUnicodeString
297 stub RtlConvertUiListToApiList
298 stub RtlConvertUlongToLargeInteger
299 stub RtlCopyLuid
300 stub RtlCopyLuidAndAttributesArray
301 stub RtlCopySecurityDescriptor
302 stdcall RtlCopySid(long ptr ptr) RtlCopySid
303 stub RtlCopySidAndAttributesArray
304 stub RtlCopyString
305 stub RtlCopyUnicodeString
306 stdcall RtlCreateAcl(ptr long long) RtlCreateAcl
307 stub RtlCreateAndSetSD
308 stub RtlCreateEnvironment
309 stdcall RtlCreateHeap(long long long) HeapCreate
310 stub RtlCreateProcessParameters
311 stub RtlCreateQueryDebugBuffer
312 stub RtlCreateRegistryKey
313 stdcall RtlCreateSecurityDescriptor(ptr long) RtlCreateSecurityDescriptor
314 stub RtlCreateTagHeap
315 stub RtlCreateUnicodeString
316 stub RtlCreateUnicodeStringFromAsciiz
317 stub RtlCreateUserProcess
318 stub RtlCreateUserSecurityObject
319 stub RtlCreateUserThread
320 stub RtlCustomCPToUnicodeN
321 stub RtlCutoverTimeToSystemTime
322 stub RtlDeNormalizeProcessParams
323 stub RtlDecompressBuffer
324 stub RtlDecompressFragment
325 stub RtlDelete
326 stub RtlDeleteAce
327 stub RtlDeleteCriticalSection
328 stub RtlDeleteElementGenericTable
329 stub RtlDeleteRegistryValue
330 stub RtlDeleteResource
331 stub RtlDeleteSecurityObject
332 stub RtlDestroyEnvironment
333 stub RtlDestroyHeap
334 stub RtlDestroyProcessParameters
335 stub RtlDestroyQueryDebugBuffer
336 stub RtlDetermineDosPathNameType_U
337 stub RtlDoesFileExists_U
338 stdcall RtlDosPathNameToNtPathName_U(ptr ptr long long) RtlDosPathNameToNtPathName_U
339 stub RtlDosSearchPath_U
340 stub RtlDumpResource
341 stub RtlEnlargedIntegerMultiply
342 stub RtlEnlargedUnsignedDivide
343 stub RtlEnlargedUnsignedMultiply
344 stdcall RtlEnterCriticalSection(ptr) EnterCriticalSection
345 stub RtlEnumProcessHeaps
346 stub RtlEnumerateGenericTable
347 stub RtlEnumerateGenericTableWithoutSplaying
348 stub RtlEqualComputerName
349 stub RtlEqualDomainName
350 stub RtlEqualLuid
351 stub RtlEqualPrefixSid
352 stub RtlEqualSid
353 stub RtlEqualString
354 stub RtlEqualUnicodeString
355 stub RtlEraseUnicodeString
356 stub RtlExpandEnvironmentStrings_U
357 stub RtlExtendHeap
358 stub RtlExtendedIntegerMultiply
359 stub RtlExtendedLargeIntegerDivide
360 stub RtlExtendedMagicDivide
361 stdcall RtlFillMemory(ptr long long) RtlFillMemory
362 stub RtlFillMemoryUlong
363 stub RtlFindClearBits
364 stub RtlFindClearBitsAndSet
365 stub RtlFindLongestRunClear
366 stub RtlFindLongestRunSet
367 stub RtlFindMessage
368 stub RtlFindSetBits
369 stub RtlFindSetBitsAndClear
370 stdcall RtlFirstFreeAce(ptr ptr) RtlFirstFreeAce
371 stub RtlFormatCurrentUserKeyPath
372 stub RtlFormatMessage
373 stub RtlFreeAnsiString
374 stdcall RtlFreeHeap(long long long) HeapFree
375 stub RtlFreeOemString
376 stub RtlFreeSid
377 stdcall RtlFreeUnicodeString(ptr) RtlFreeUnicodeString
378 stub RtlGenerate8dot3Name
379 stub RtlGetAce
380 stub RtlGetCallersAddress
381 stub RtlGetCompressionWorkSpaceSize
382 stub RtlGetControlSecurityDescriptor
383 stub RtlGetCurrentDirectory_U
384 stub RtlGetDaclSecurityDescriptor
385 stub RtlGetElementGenericTable
386 stub RtlGetFullPathName_U
387 stub RtlGetGroupSecurityDescriptor
388 stub RtlGetLongestNtPathLength
389 stub RtlGetNtGlobalFlags
390 stdcall RtlGetNtProductType(ptr) RtlGetNtProductType
391 stub RtlGetOwnerSecurityDescriptor
392 stub RtlGetProcessHeaps
393 stub RtlGetSaclSecurityDescriptor
394 stub RtlGetUserInfoHeap
395 stub RtlIdentifierAuthoritySid
396 stub RtlImageDirectoryEntryToData
397 stdcall RtlImageNtHeader(long) RtlImageNtHeader
398 stub RtlImpersonateSelf
399 stdcall RtlInitAnsiString(ptr ptr) RtlInitAnsiString
400 stub RtlInitCodePageTable
401 stub RtlInitNlsTables
402 stdcall RtlInitString(ptr ptr) RtlInitString
403 stdcall RtlInitUnicodeString(ptr ptr) RtlInitUnicodeString
404 stub RtlInitializeBitMap
405 stub RtlInitializeContext
406 stdcall RtlInitializeCriticalSection(ptr) InitializeCriticalSection
407 stub RtlInitializeGenericTable
408 stub RtlInitializeRXact
409 stub RtlInitializeResource
410 stdcall RtlInitializeSid(ptr ptr long) RtlInitializeSid
411 stub RtlInsertElementGenericTable
412 stub RtlIntegerToChar
413 stub RtlIntegerToUnicodeString
414 stub RtlIsDosDeviceName_U
415 stub RtlIsGenericTableEmpty
416 stub RtlIsNameLegalDOS8Dot3
417 stub RtlIsTextUnicode
418 stub RtlLargeIntegerAdd
419 stub RtlLargeIntegerArithmeticShift
420 stub RtlLargeIntegerDivide
421 stub RtlLargeIntegerNegate
422 stub RtlLargeIntegerShiftLeft
423 stub RtlLargeIntegerShiftRight
424 stub RtlLargeIntegerSubtract
425 stub RtlLargeIntegerToChar
426 stdcall RtlLeaveCriticalSection(ptr) LeaveCriticalSection
427 stdcall RtlLengthRequiredSid(long) RtlLengthRequiredSid
428 stub RtlLengthSecurityDescriptor
429 stdcall RtlLengthSid(ptr) RtlLengthSid
430 stub RtlLocalTimeToSystemTime
431 stub RtlLockHeap
432 stub RtlLookupElementGenericTable
433 stub RtlMakeSelfRelativeSD
434 stub RtlMapGenericMask
435 stdcall RtlMoveMemory(ptr ptr long) RtlMoveMemory
436 stdcall RtlMultiByteToUnicodeN(ptr long ptr ptr long) RtlMultiByteToUnicodeN
437 stub RtlMultiByteToUnicodeSize
438 stub RtlNewInstanceSecurityObject
439 stub RtlNewSecurityGrantedAccess
440 stub RtlNewSecurityObject
441 stdcall RtlNormalizeProcessParams(ptr) RtlNormalizeProcessParams
442 stdcall RtlNtStatusToDosError(long) RtlNtStatusToDosError
443 stub RtlNumberGenericTableElements
444 stub RtlNumberOfClearBits
445 stub RtlNumberOfSetBits
446 stub RtlOemStringToUnicodeSize
447 stdcall RtlOemStringToUnicodeString(ptr ptr long) RtlOemStringToUnicodeString
448 stdcall RtlOemToUnicodeN(ptr long ptr ptr long) RtlOemToUnicodeN
449 stub RtlOpenCurrentUser
450 stub RtlPcToFileHeader
451 stub RtlPrefixString
452 stub RtlPrefixUnicodeString
453 stub RtlProtectHeap
454 stub RtlQueryEnvironmentVariable_U
455 stub RtlQueryInformationAcl
456 stub RtlQueryProcessBackTraceInformation
457 stub RtlQueryProcessDebugInformation
458 stub RtlQueryProcessHeapInformation
459 stub RtlQueryProcessLockInformation
460 stub RtlQueryRegistryValues
461 stub RtlQuerySecurityObject
462 stub RtlQueryTagHeap
463 stub RtlQueryTimeZoneInformation
464 stub RtlRaiseException
465 stub RtlRaiseStatus
466 stub RtlRandom
467 stub RtlReAllocateHeap
468 stub RtlRealPredecessor
469 stub RtlRealSuccessor
470 stub RtlReleasePebLock
471 stub RtlReleaseResource
472 stub RtlRemoteCall
473 stub RtlResetRtlTranslations
474 stub RtlRunDecodeUnicodeString
475 stub RtlRunEncodeUnicodeString
476 stub RtlSecondsSince1970ToTime
477 stub RtlSecondsSince1980ToTime
478 stub RtlSelfRelativeToAbsoluteSD
479 stub RtlSetAllBits
480 stub RtlSetBits
481 stub RtlSetCurrentDirectory_U
482 stub RtlSetCurrentEnvironment
483 stdcall RtlSetDaclSecurityDescriptor(ptr long ptr long) RtlSetDaclSecurityDescriptor
484 stub RtlSetEnvironmentVariable
485 stdcall RtlSetGroupSecurityDescriptor(ptr ptr long) RtlSetGroupSecurityDescriptor
486 stub RtlSetInformationAcl
487 stdcall RtlSetOwnerSecurityDescriptor(ptr ptr long) RtlSetOwnerSecurityDescriptor
488 stdcall RtlSetSaclSecurityDescriptor(ptr long ptr long) RtlSetSaclSecurityDescriptor
489 stub RtlSetSecurityObject
490 stub RtlSetTimeZoneInformation
491 stub RtlSetUserFlagsHeap
492 stub RtlSetUserValueHeap
493 stdcall RtlSizeHeap(long long long) HeapSize
494 stub RtlSplay
495 stub RtlStartRXact
496 stdcall RtlSubAuthorityCountSid(ptr) RtlSubAuthorityCountSid
497 stdcall RtlSubAuthoritySid(ptr long) RtlSubAuthoritySid
498 stub RtlSubtreePredecessor
499 stub RtlSubtreeSuccessor
500 stub RtlSystemTimeToLocalTime
501 stub RtlTimeFieldsToTime
502 stub RtlTimeToElapsedTimeFields
503 stub RtlTimeToSecondsSince1970
504 stub RtlTimeToSecondsSince1980
505 stub RtlTimeToTimeFields
506 stub RtlUnicodeStringToAnsiSize
507 stdcall RtlUnicodeStringToAnsiString(ptr ptr long) RtlUnicodeStringToAnsiString
508 stub RtlUnicodeStringToCountedOemString
509 stub RtlUnicodeStringToInteger
510 stub RtlUnicodeStringToOemSize
511 stdcall RtlUnicodeStringToOemString(ptr ptr long) RtlUnicodeStringToOemString
512 stub RtlUnicodeToCustomCPN
513 stub RtlUnicodeToMultiByteN
514 stub RtlUnicodeToMultiByteSize
515 stdcall RtlUnicodeToOemN(ptr long ptr ptr long) RtlUnicodeToOemN
516 stub RtlUniform
517 stub RtlUnlockHeap
518 stub RtlUnwind
519 stub RtlUpcaseUnicodeChar
520 stdcall RtlUpcaseUnicodeString(ptr ptr long) RtlUpcaseUnicodeString
521 stub RtlUpcaseUnicodeStringToAnsiString
522 stub RtlUpcaseUnicodeStringToCountedOemString
523 stub RtlUpcaseUnicodeStringToOemString
524 stub RtlUpcaseUnicodeToCustomCPN
525 stub RtlUpcaseUnicodeToMultiByteN
526 stub RtlUpcaseUnicodeToOemN
527 stub RtlUpperChar
528 stub RtlUpperString
529 stub RtlUsageHeap
530 stub RtlValidAcl
531 stub RtlValidSecurityDescriptor
532 stub RtlValidSid
533 stub RtlValidateHeap
534 stub RtlValidateProcessHeaps
535 stub RtlWalkHeap
536 stub RtlWriteRegistryValue
537 stub RtlZeroHeap
538 stdcall RtlZeroMemory(ptr long) RtlZeroMemory
539 stub RtlpInitializeRtl
540 stub RtlpNtCreateKey
541 stub RtlpNtEnumerateSubKey
542 stub RtlpNtMakeTemporaryKey
543 stub RtlpNtOpenKey
544 stub RtlpNtQueryValueKey
545 stub RtlpNtSetValueKey
546 stub RtlpUnWaitCriticalSection
547 stub RtlpWaitForCriticalSection
548 stdcall RtlxAnsiStringToUnicodeSize(ptr) RtlxAnsiStringToUnicodeSize
549 stdcall RtlxOemStringToUnicodeSize(ptr) RtlxOemStringToUnicodeSize
550 stub RtlxUnicodeStringToAnsiSize
551 stub RtlxUnicodeStringToOemSize
552 stub SaveEm87Context
553 stub ZwAcceptConnectPort
554 stub ZwAccessCheck
555 stub ZwAccessCheckAndAuditAlarm
556 stub ZwAdjustGroupsToken
557 stub ZwAdjustPrivilegesToken
558 stub ZwAlertResumeThread
559 stub ZwAlertThread
560 stub ZwAllocateLocallyUniqueId
561 stub ZwAllocateUuids
562 stub ZwAllocateVirtualMemory
563 stub ZwCallbackReturn
564 stub ZwCancelIoFile
565 stub ZwCancelTimer
566 stub ZwClearEvent
567 stub ZwClose
568 stub ZwCloseObjectAuditAlarm
569 stub ZwCompleteConnectPort
570 stub ZwConnectPort
571 stub ZwContinue
572 stub ZwCreateDirectoryObject
573 stub ZwCreateEvent
574 stub ZwCreateEventPair
575 stub ZwCreateFile
576 stub ZwCreateIoCompletion
577 stub ZwCreateKey
578 stub ZwCreateMailslotFile
579 stub ZwCreateMutant
580 stub ZwCreateNamedPipeFile
581 stub ZwCreatePagingFile
582 stub ZwCreatePort
583 stub ZwCreateProcess
584 stub ZwCreateProfile
585 stub ZwCreateSection
586 stub ZwCreateSemaphore
587 stub ZwCreateSymbolicLinkObject
588 stub ZwCreateThread
589 stub ZwCreateTimer
590 stub ZwCreateToken
591 stub ZwDelayExecution
592 stub ZwDeleteFile
593 stub ZwDeleteKey
594 stub ZwDeleteValueKey
595 stub ZwDeviceIoControlFile
596 stub ZwDisplayString
597 stub ZwDuplicateObject
598 stub ZwDuplicateToken
599 stub ZwEnumerateBus
600 stub ZwEnumerateKey
601 stub ZwEnumerateValueKey
602 stub ZwExtendSection
603 stub ZwFlushBuffersFile
604 stub ZwFlushInstructionCache
605 stub ZwFlushKey
606 stub ZwFlushVirtualMemory
607 stub ZwFlushWriteBuffer
608 stub ZwFreeVirtualMemory
609 stub ZwFsControlFile
610 stub ZwGetContextThread
611 stub ZwGetPlugPlayEvent
612 stub ZwGetTickCount
613 stub ZwImpersonateClientOfPort
614 stub ZwImpersonateThread
615 stub ZwInitializeRegistry
616 stub ZwListenPort
617 stub ZwLoadDriver
618 stub ZwLoadKey
619 stub ZwLockFile
620 stub ZwLockVirtualMemory
621 stub ZwMakeTemporaryObject
622 stub ZwMapViewOfSection
623 stub ZwNotifyChangeDirectoryFile
624 stub ZwNotifyChangeKey
625 stub ZwOpenDirectoryObject
626 stub ZwOpenEvent
627 stub ZwOpenEventPair
628 stub ZwOpenFile
629 stub ZwOpenIoCompletion
630 stub ZwOpenKey
631 stub ZwOpenMutant
632 stub ZwOpenObjectAuditAlarm
633 stub ZwOpenProcess
634 stub ZwOpenProcessToken
635 stub ZwOpenSection
636 stub ZwOpenSemaphore
637 stub ZwOpenSymbolicLinkObject
638 stub ZwOpenThread
639 stub ZwOpenThreadToken
640 stub ZwOpenTimer
641 stub ZwPlugPlayControl
642 stub ZwPrivilegeCheck
643 stub ZwPrivilegeObjectAuditAlarm
644 stub ZwPrivilegedServiceAuditAlarm
645 stub ZwProtectVirtualMemory
646 stub ZwPulseEvent
647 stub ZwQueryAttributesFile
648 stub ZwQueryDefaultLocale
649 stub ZwQueryDirectoryFile
650 stub ZwQueryDirectoryObject
651 stub ZwQueryEaFile
652 stub ZwQueryEvent
653 stub ZwQueryInformationFile
654 stub ZwQueryInformationPort
655 stub ZwQueryInformationProcess
656 stub ZwQueryInformationThread
657 stub ZwQueryInformationToken
658 stub ZwQueryIntervalProfile
659 stub ZwQueryIoCompletion
660 stub ZwQueryKey
661 stub ZwQueryMutant
662 stub ZwQueryObject
663 stub ZwQueryPerformanceCounter
664 stub ZwQuerySection
665 stub ZwQuerySecurityObject
666 stub ZwQuerySemaphore
667 stub ZwQuerySymbolicLinkObject
668 stub ZwQuerySystemEnvironmentValue
669 stub ZwQuerySystemInformation
670 stub ZwQuerySystemTime
671 stub ZwQueryTimer
672 stub ZwQueryTimerResolution
673 stub ZwQueryValueKey
674 stub ZwQueryVirtualMemory
675 stub ZwQueryVolumeInformationFile
676 stub ZwRaiseException
677 stub ZwRaiseHardError
678 stub ZwReadFile
679 stub ZwReadRequestData
680 stub ZwReadVirtualMemory
681 stub ZwRegisterNewDevice
682 stub ZwRegisterThreadTerminatePort
683 stub ZwReleaseMutant
684 stub ZwReleaseProcessMutant
685 stub ZwReleaseSemaphore
686 stub ZwRemoveIoCompletion
687 stub ZwReplaceKey
688 stub ZwReplyPort
689 stub ZwReplyWaitReceivePort
690 stub ZwReplyWaitReplyPort
691 stub ZwRequestPort
692 stub ZwRequestWaitReplyPort
693 stub ZwResetEvent
694 stub ZwRestoreKey
695 stub ZwResumeThread
696 stub ZwSaveKey
697 stub ZwSetContextThread
698 stub ZwSetDefaultHardErrorPort
699 stub ZwSetDefaultLocale
700 stub ZwSetEaFile
701 stub ZwSetEvent
702 stub ZwSetHighEventPair
703 stub ZwSetHighWaitLowEventPair
704 stub ZwSetHighWaitLowThread
705 stub ZwSetInformationFile
706 stub ZwSetInformationKey
707 stub ZwSetInformationObject
708 stub ZwSetInformationProcess
709 stub ZwSetInformationThread
710 stub ZwSetInformationToken
711 stub ZwSetIntervalProfile
712 stub ZwSetIoCompletion
713 stub ZwSetLdtEntries
714 stub ZwSetLowEventPair
715 stub ZwSetLowWaitHighEventPair
716 stub ZwSetLowWaitHighThread
717 stub ZwSetSecurityObject
718 stub ZwSetSystemEnvironmentValue
719 stub ZwSetSystemInformation
720 stub ZwSetSystemPowerState
721 stub ZwSetSystemTime
722 stub ZwSetTimer
723 stub ZwSetTimerResolution
724 stub ZwSetValueKey
725 stub ZwSetVolumeInformationFile
726 stub ZwShutdownSystem
727 stub ZwStartProfile
728 stub ZwStopProfile
729 stub ZwSuspendThread
730 stub ZwSystemDebugControl
731 stub ZwTerminateProcess
732 stub ZwTerminateThread
733 stub ZwTestAlert
734 stub ZwUnloadDriver
735 stub ZwUnloadKey
736 stub ZwUnlockFile
737 stub ZwUnlockVirtualMemory
738 stub ZwUnmapViewOfSection
739 stub ZwVdmControl
740 stub ZwW32Call
741 stub ZwWaitForMultipleObjects
742 stub ZwWaitForProcessMutant
743 stub ZwWaitForSingleObject
744 stub ZwWaitHighEventPair
745 stub ZwWaitLowEventPair
746 stub ZwWriteFile
747 stub ZwWriteRequestData
748 stub ZwWriteVirtualMemory
749 stub _CIpow
750 stub __eCommonExceptions
751 stub __eEmulatorInit
752 stub __eF2XM1
753 stub __eFABS
754 stub __eFADD32
755 stub __eFADD64
756 stub __eFADDPreg
757 stub __eFADDreg
758 stub __eFADDtop
759 stub __eFCHS
760 stub __eFCOM
761 stub __eFCOM32
762 stub __eFCOM64
763 stub __eFCOMP
764 stub __eFCOMP32
765 stub __eFCOMP64
766 stub __eFCOMPP
767 stub __eFCOS
768 stub __eFDECSTP
769 stub __eFDIV32
770 stub __eFDIV64
771 stub __eFDIVPreg
772 stub __eFDIVR32
773 stub __eFDIVR64
774 stub __eFDIVRPreg
775 stub __eFDIVRreg
776 stub __eFDIVRtop
777 stub __eFDIVreg
778 stub __eFDIVtop
779 stub __eFFREE
780 stub __eFIADD16
781 stub __eFIADD32
782 stub __eFICOM16
783 stub __eFICOM32
784 stub __eFICOMP16
785 stub __eFICOMP32
786 stub __eFIDIV16
787 stub __eFIDIV32
788 stub __eFIDIVR16
789 stub __eFIDIVR32
790 stub __eFILD16
791 stub __eFILD32
792 stub __eFILD64
793 stub __eFIMUL16
794 stub __eFIMUL32
795 stub __eFINCSTP
796 stub __eFINIT
797 stub __eFIST16
798 stub __eFIST32
799 stub __eFISTP16
800 stub __eFISTP32
801 stub __eFISTP64
802 stub __eFISUB16
803 stub __eFISUB32
804 stub __eFISUBR16
805 stub __eFISUBR32
806 stub __eFLD1
807 stub __eFLD32
808 stub __eFLD64
809 stub __eFLD80
810 stub __eFLDCW
811 stub __eFLDENV
812 stub __eFLDL2E
813 stub __eFLDLN2
814 stub __eFLDPI
815 stub __eFLDZ
816 stub __eFMUL32
817 stub __eFMUL64
818 stub __eFMULPreg
819 stub __eFMULreg
820 stub __eFMULtop
821 stub __eFPATAN
822 stub __eFPREM
823 stub __eFPREM1
824 stub __eFPTAN
825 stub __eFRNDINT
826 stub __eFRSTOR
827 stub __eFSAVE
828 stub __eFSCALE
829 stub __eFSIN
830 stub __eFSQRT
831 stub __eFST
832 stub __eFST32
833 stub __eFST64
834 stub __eFSTCW
835 stub __eFSTENV
836 stub __eFSTP
837 stub __eFSTP32
838 stub __eFSTP64
839 stub __eFSTP80
840 stub __eFSTSW
841 stub __eFSUB32
842 stub __eFSUB64
843 stub __eFSUBPreg
844 stub __eFSUBR32
845 stub __eFSUBR64
846 stub __eFSUBRPreg
847 stub __eFSUBRreg
848 stub __eFSUBRtop
849 stub __eFSUBreg
850 stub __eFSUBtop
851 stub __eFTST
852 stub __eFUCOM
853 stub __eFUCOMP
854 stub __eFUCOMPP
855 stub __eFXAM
856 stub __eFXCH
857 stub __eFXTRACT
858 stub __eFYL2X
859 stub __eFYL2XP1
860 stub __eGetStatusWord
861 stub _alloca_probe
862 cdecl _chkstk() NTDLL_chkstk
863 stub _fltused
864 stub _ftol
865 stub _itoa
866 stub _ltoa
867 stub _memccpy
868 stub _memicmp
869 stub _snprintf
870 stub _snwprintf
871 stub _splitpath
872 cdecl _strcmpi(ptr ptr) CRTDLL__strcmpi
873 cdecl _stricmp(ptr ptr) CRTDLL__strcmpi
874 stub _strlwr
875 cdecl _strnicmp(ptr ptr long) CRTDLL__strnicmp
876 cdecl _strupr(ptr) CRTDLL__strupr
877 stub _ultoa
878 stub _vsnprintf
879 cdecl _wcsicmp(ptr ptr) CRTDLL__wcsicmp
880 cdecl _wcslwr(ptr) CRTDLL__wcslwr
881 cdecl _wcsnicmp(ptr ptr long) CRTDLL__wcsnicmp
882 cdecl _wcsupr(ptr) CRTDLL__wcsupr
883 stub abs
884 stub atan
885 cdecl atoi(ptr) atoi
886 cdecl atol(ptr) atol
887 stub ceil
888 stub cos
889 stub fabs
890 stub floor
891 cdecl isalpha(long) isalpha
892 cdecl isdigit(long) isdigit
893 cdecl islower(long) islower
894 cdecl isprint(long) isprint
895 cdecl isspace(long) isspace
896 cdecl isupper(long) isupper
897 stub iswalpha
898 stub iswctype
899 cdecl isxdigit(long) isxdigit
900 stub labs
901 stub log
902 stub mbstowcs
903 cdecl memchr(ptr long long) memchr
904 cdecl memcmp(ptr ptr long) memcmp
905 cdecl memcpy(ptr ptr long) memcpy
906 cdecl memmove(ptr ptr long) memmove
907 cdecl memset(ptr long long) memset
908 stub pow
909 stub qsort
910 stub sin
911 varargs sprintf() wsprintf32A
912 stub sqrt
913 varargs sscanf() sscanf
914 cdecl strcat(ptr ptr) strcat
915 cdecl strchr(ptr long) strchr
916 cdecl strcmp(ptr ptr) strcmp
917 cdecl strcpy(ptr ptr) strcpy
918 cdecl strcspn(ptr ptr) strcspn
919 cdecl strlen(ptr) strlen
920 cdecl strncat(ptr ptr long) strncat
921 cdecl strncmp(ptr ptr long) strncmp
922 cdecl strncpy(ptr ptr long) strncpy
923 cdecl strpbrk(ptr ptr long) strpbrk
924 cdecl strrchr(ptr long) strrchr
925 cdecl strspn(ptr ptr) strspn
926 cdecl strstr(ptr ptr) strstr
927 varargs swprintf() wsprintf32W
928 stub tan
929 cdecl tolower(long) tolower
930 cdecl toupper(long) toupper
931 stub towlower
932 stub towupper
933 cdecl vsprintf(ptr ptr ptr) CRTDLL_vsprintf
934 cdecl wcscat(ptr ptr) CRTDLL_wcscat
935 cdecl wcschr(ptr long) CRTDLL_wcschr
936 stub wcscmp
937 cdecl wcscpy(ptr ptr) CRTDLL_wcscpy
938 stub wcscspn
939 cdecl wcslen(ptr) CRTDLL_wcslen
940 stub wcsncat
941 stub wcsncmp
942 cdecl wcsncpy(ptr ptr long) CRTDLL_wcsncpy
943 stub wcspbrk
944 cdecl wcsrchr(ptr long) CRTDLL_wcsrchr
945 stub wcsspn
946 cdecl wcsstr(ptr ptr) CRTDLL_wcsstr
947 stub wcstok
948 stub wcstol
949 cdecl wcstombs(ptr ptr long) CRTDLL_wcstombs
950 stub wcstoul
