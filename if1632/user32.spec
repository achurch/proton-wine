name	user32
type	win32

  1 stub ActivateKeyboardLayout
  2 stdcall AdjustWindowRect(ptr long long) AdjustWindowRect32
  3 stdcall AdjustWindowRectEx(ptr long long long) AdjustWindowRectEx32
  4 stdcall AnyPopup() AnyPopup32
  5 stdcall AppendMenuA(long long long ptr) AppendMenu32A
  6 stdcall AppendMenuW(long long long ptr) AppendMenu32W
  7 stdcall ArrangeIconicWindows(long) ArrangeIconicWindows32
  8 stub AttachThreadInput
  9 stdcall BeginDeferWindowPos(long) BeginDeferWindowPos32
 10 stdcall BeginPaint(long ptr) BeginPaint32
 11 stdcall BringWindowToTop(long) BringWindowToTop32
 12 stub BroadcastSystemMessage
 13 stub CalcChildScroll
 14 stub CallMsgFilter
 15 stdcall CallMsgFilterA(ptr long) CallMsgFilter32A
 16 stdcall CallMsgFilterW(ptr long) CallMsgFilter32W
 17 stdcall CallNextHookEx(long long long long) CallNextHookEx32
 18 stdcall CallWindowProcA(ptr long long long long) CallWindowProc32A
 19 stdcall CallWindowProcW(ptr long long long long) CallWindowProc32W
 20 stub CascadeChildWindows
 21 stub CascadeWindows
 22 stdcall ChangeClipboardChain(long long) ChangeClipboardChain32
 23 stdcall ChangeMenuA(long long ptr long long) ChangeMenu32A
 24 stdcall ChangeMenuW(long long ptr long long) ChangeMenu32W
 25 stdcall CharLowerA(ptr) CharLower32A
 26 stdcall CharLowerBuffA(ptr long) CharLowerBuff32A
 27 stdcall CharLowerBuffW(ptr long) CharLowerBuff32W
 28 stdcall CharLowerW(ptr) CharLower32W
 29 stdcall CharNextA(ptr) CharNext32A
 30 stdcall CharNextExA(long ptr long) CharNextEx32A
 31 stdcall CharNextExW(long ptr long) CharNextEx32W
 32 stdcall CharNextW(ptr) CharNext32W
 33 stdcall CharPrevA(ptr ptr) CharPrev32A
 34 stdcall CharPrevExA(long ptr ptr long) CharPrevEx32A
 35 stdcall CharPrevExW(long ptr ptr long) CharPrevEx32W
 36 stdcall CharPrevW(ptr ptr) CharPrev32W
 37 stdcall CharToOemA(ptr ptr) CharToOem32A
 38 stdcall CharToOemBuffA(ptr ptr long) CharToOemBuff32A
 39 stdcall CharToOemBuffW(ptr ptr long) CharToOemBuff32W
 40 stdcall CharToOemW(ptr ptr) CharToOem32W
 41 stdcall CharUpperA(ptr) CharUpper32A
 42 stdcall CharUpperBuffA(ptr long) CharUpperBuff32A
 43 stdcall CharUpperBuffW(ptr long) CharUpperBuff32W
 44 stdcall CharUpperW(ptr) CharUpper32W
 45 stdcall CheckDlgButton(long long long) CheckDlgButton32
 46 stdcall CheckMenuItem(long long long) CheckMenuItem32
 47 stub CheckMenuRadioItem
 48 stdcall CheckRadioButton(long long long long) CheckRadioButton32
 49 stdcall ChildWindowFromPoint(long long long) ChildWindowFromPoint32
 50 stub ChildWindowFromPointEx
 51 stub ClientThreadConnect
 52 stdcall ClientToScreen(long ptr) ClientToScreen32
 53 stdcall ClipCursor(ptr) ClipCursor32
 54 stdcall CloseClipboard() CloseClipboard32
 55 stub CloseDesktop
 56 stdcall CloseWindow(long) CloseWindow32
 57 stub CloseWindowStation
 58 stub CopyAcceleratorTableA
 59 stub CopyAcceleratorTableW
 60 stdcall CopyIcon(long) CopyIcon32
 61 stdcall CopyImage(long long long long long) CopyImage32
 62 stdcall CopyRect(ptr ptr) CopyRect32
 63 stdcall CountClipboardFormats() CountClipboardFormats32
 64 stub CreateAcceleratorTableA
 65 stub CreateAcceleratorTableW
 66 stdcall CreateCaret(long long long long) CreateCaret32
 67 stdcall CreateCursor(long long long long long ptr ptr) CreateCursor32
 68 stub CreateDesktopA
 69 stub CreateDesktopW
 70 stdcall CreateDialogIndirectParamA(long ptr long ptr long) CreateDialogIndirectParam32A
 71 stub CreateDialogIndirectParamAorW
 72 stdcall CreateDialogIndirectParamW(long ptr long ptr long) CreateDialogIndirectParam32W
 73 stdcall CreateDialogParamA(long ptr long ptr long) CreateDialogParam32A
 74 stdcall CreateDialogParamW(long ptr long ptr long) CreateDialogParam32W
 75 stdcall CreateIcon(long long long long long ptr ptr) CreateIcon32
 76 stub CreateIconFromResource
 77 stdcall CreateIconFromResourceEx(ptr long long long long long long) CreateIconFromResourceEx32
 78 stub CreateIconIndirect
 79 stub CreateMDIWindowA
 80 stub CreateMDIWindowW
 81 stdcall CreateMenu() CreateMenu32
 82 stdcall CreatePopupMenu() CreatePopupMenu32
 83 stdcall CreateWindowExA(long ptr ptr long long long long long 
                            long long long ptr) CreateWindowEx32A
 84 stdcall CreateWindowExW(long ptr ptr long long long long long 
                            long long long ptr) CreateWindowEx32W
 85 stub CreateWindowStationA
 86 stub CreateWindowStationW
 87 stub DdeAbandonTransaction
 88 stub DdeAccessData
 89 stub DdeAddData
 90 stdcall DdeClientTransaction(ptr long long long long long long ptr) DdeClientTransaction32
 91 stub DdeCmpStringHandles
 92 stdcall DdeConnect(long long long ptr) DdeConnect32
 93 stub DdeConnectList
 94 stub DdeCreateDataHandle
 95 stdcall DdeCreateStringHandleA(long ptr long) DdeCreateStringHandle32A
 96 stdcall DdeCreateStringHandleW(long ptr long) DdeCreateStringHandle32W
 97 stdcall DdeDisconnect(long) DdeDisconnect32
 98 stub DdeDisconnectList
 99 stub DdeEnableCallback
100 stdcall DdeFreeDataHandle(long) DdeFreeDataHandle32
101 stdcall DdeFreeStringHandle(long long) DdeFreeStringHandle32
102 stub DdeGetData
103 stdcall DdeGetLastError(long) DdeGetLastError32
104 stub DdeGetQualityOfService
105 stub DdeImpersonateClient
106 stdcall DdeInitializeA(ptr ptr long long) DdeInitialize32A
107 stdcall DdeInitializeW(ptr ptr long long) DdeInitialize32W
108 stdcall DdeKeepStringHandle(long long) DdeKeepStringHandle32
109 stdcall DdeNameService(long long long long) DdeNameService32
110 stub DdePostAdvise
111 stub DdeQueryConvInfo
112 stub DdeQueryNextServer
113 stub DdeQueryStringA
114 stub DdeQueryStringW
115 stdcall DdeReconnect(long) DdeReconnect
116 stub DdeSetQualityOfService
117 stub DdeSetUserHandle
118 stub DdeUnaccessData
119 stdcall DdeUninitialize(long) DdeUninitialize32
120 stdcall DefDlgProcA(long long long long) DefDlgProc32A
121 stdcall DefDlgProcW(long long long long) DefDlgProc32W
122 stdcall DefFrameProcA(long long long long long) DefFrameProc32A
123 stdcall DefFrameProcW(long long long long long) DefFrameProc32W
124 stdcall DefMDIChildProcA(long long long long) DefMDIChildProc32A
125 stdcall DefMDIChildProcW(long long long long) DefMDIChildProc32W
126 stdcall DefWindowProcA(long long long long) DefWindowProc32A
127 stdcall DefWindowProcW(long long long long) DefWindowProc32W
128 stdcall DeferWindowPos(long long long long long long long long) DeferWindowPos32
129 stdcall DeleteMenu(long long long) DeleteMenu32
130 stub DestroyAcceleratorTable
131 stdcall DestroyCaret() DestroyCaret32
132 stdcall DestroyCursor(long) DestroyCursor32
133 stdcall DestroyIcon(long) DestroyIcon32
134 stdcall DestroyMenu(long) DestroyMenu32
135 stdcall DestroyWindow(long) DestroyWindow32
136 stdcall DialogBoxIndirectParamA(long ptr long ptr long) DialogBoxIndirectParam32A
137 stdcall DialogBoxIndirectParamAorW(long ptr long ptr long) DialogBoxIndirectParam32A
138 stdcall DialogBoxIndirectParamW(long ptr long ptr long) DialogBoxIndirectParam32W
139 stdcall DialogBoxParamA(long ptr long ptr long) DialogBoxParam32A
140 stdcall DialogBoxParamW(long ptr long ptr long) DialogBoxParam32W
141 stdcall DispatchMessageA(ptr) DispatchMessage32A
142 stdcall DispatchMessageW(ptr) DispatchMessage32W
143 stdcall DlgDirListA(long ptr long long long) DlgDirList32A
144 stdcall DlgDirListComboBoxA(long ptr long long long) DlgDirListComboBox32A
145 stdcall DlgDirListComboBoxW(long ptr long long long) DlgDirListComboBox32W
146 stdcall DlgDirListW(long ptr long long long) DlgDirList32W
147 stdcall DlgDirSelectComboBoxExA(long ptr long long) DlgDirSelectComboBoxEx32A
148 stdcall DlgDirSelectComboBoxExW(long ptr long long) DlgDirSelectComboBoxEx32W
149 stdcall DlgDirSelectExA(long ptr long long) DlgDirSelectEx32A
150 stdcall DlgDirSelectExW(long ptr long long) DlgDirSelectEx32W
151 stdcall DragDetect(long long long) DragDetect32
152 stub DragObject
153 stdcall DrawAnimatedRects(long long ptr ptr) DrawAnimatedRects32
154 stub DrawCaption
155 stdcall DrawEdge(long ptr long long) DrawEdge32
156 stdcall DrawFocusRect(long ptr) DrawFocusRect32
157 stub DrawFrame
158 stdcall DrawFrameControl(long ptr long long) DrawFrameControl32
159 stdcall DrawIcon(long long long long) DrawIcon32
160 stub DrawIconEx
161 stdcall DrawMenuBar(long) DrawMenuBar32
162 stdcall DrawStateA(long long ptr long long long long long long long) DrawState32A
163 stub DrawStateW
164 stdcall DrawTextA(long ptr long ptr long) DrawText32A
165 stdcall DrawTextExA(long ptr long ptr long ptr) DrawTextEx32A
166 stdcall DrawTextExW(long ptr long ptr long ptr) DrawTextEx32W
167 stdcall DrawTextW(long ptr long ptr long) DrawText32W
168 stub EditWndProc
169 stdcall EmptyClipboard() EmptyClipboard32
170 stdcall EnableMenuItem(long long long) EnableMenuItem32
171 stdcall EnableScrollBar(long long long) EnableScrollBar32
172 stdcall EnableWindow(long long) EnableWindow32
173 stdcall EndDeferWindowPos(long) EndDeferWindowPos32
174 stdcall EndDialog(long long) EndDialog32
175 stdcall EndMenu() EndMenu
176 stdcall EndPaint(long ptr) EndPaint32
177 stub EndTask
178 stdcall EnumChildWindows(long ptr long) EnumChildWindows32
179 stdcall EnumClipboardFormats(long) EnumClipboardFormats32
180 stub EnumDesktopsA
181 stub EnumDesktopsW
182 stub EnumDisplayDeviceModesA
183 stub EnumDisplayDeviceModesW
184 stub EnumDisplayDevicesA
185 stub EnumDisplayDevicesW
186 stdcall EnumPropsA(long ptr) EnumProps32A
187 stdcall EnumPropsExA(long ptr long) EnumPropsEx32A
188 stdcall EnumPropsExW(long ptr long) EnumPropsEx32W
189 stdcall EnumPropsW(long ptr) EnumProps32W
190 stdcall EnumThreadWindows(long ptr long) EnumThreadWindows
191 stub EnumWindowStationsA
192 stub EnumWindowStationsW
193 stdcall EnumWindows(ptr long) EnumWindows32
194 stdcall EqualRect(ptr ptr) EqualRect32
195 stdcall ExcludeUpdateRgn(long long) ExcludeUpdateRgn32
196 stdcall ExitWindowsEx(long long) ExitWindowsEx
197 stdcall FillRect(long ptr long) FillRect32
198 stdcall FindWindowA(ptr ptr) FindWindow32A
199 stdcall FindWindowExA(long long ptr ptr) FindWindowEx32A
200 stdcall FindWindowExW(long long ptr ptr) FindWindowEx32W
201 stdcall FindWindowW(ptr ptr) FindWindow32W
202 stdcall FlashWindow(long long) FlashWindow32
203 stdcall FrameRect(long ptr long) FrameRect32
204 stub FreeDDElParam
205 stdcall GetActiveWindow() GetActiveWindow32
206 stdcall GetAppCompatFlags(long) GetAppCompatFlags32
207 stdcall GetAsyncKeyState(long) GetAsyncKeyState32
208 stdcall GetCapture() GetCapture32
209 stdcall GetCaretBlinkTime() GetCaretBlinkTime32
210 stdcall GetCaretPos(ptr) GetCaretPos32
211 stdcall GetClassInfoA(long ptr ptr) GetClassInfo32A
212 stdcall GetClassInfoExA(long ptr ptr) GetClassInfoEx32A
213 stdcall GetClassInfoExW(long ptr ptr) GetClassInfoEx32W
214 stdcall GetClassInfoW(long ptr ptr) GetClassInfo32W
215 stdcall GetClassLongA(long long) GetClassLong32A
216 stdcall GetClassLongW(long long) GetClassLong32W
217 stdcall GetClassNameA(long ptr long) GetClassName32A
218 stdcall GetClassNameW(long ptr long) GetClassName32W
219 stdcall GetClassWord(long long) GetClassWord32
220 stdcall GetClientRect(long long) GetClientRect32
221 stdcall GetClipCursor(ptr) GetClipCursor32
222 stdcall GetClipboardData(long) GetClipboardData32
223 stdcall GetClipboardFormatNameA(long ptr long) GetClipboardFormatName32A
224 stdcall GetClipboardFormatNameW(long ptr long) GetClipboardFormatName32W
225 stdcall GetClipboardOwner() GetClipboardOwner32
226 stdcall GetClipboardViewer(long) GetClipboardViewer32
227 stdcall GetCursor() GetCursor32
228 stub GetCursorInfo
229 stdcall GetCursorPos(ptr) GetCursorPos32
230 stdcall GetDC(long) GetDC32
231 stdcall GetDCEx(long long long) GetDCEx32
232 stdcall GetDesktopWindow() GetDesktopWindow32
233 stdcall GetDialogBaseUnits() GetDialogBaseUnits
234 stdcall GetDlgCtrlID(long) GetDlgCtrlID32
235 stdcall GetDlgItem(long long) GetDlgItem32
236 stdcall GetDlgItemInt(long long ptr long) GetDlgItemInt32
237 stdcall GetDlgItemTextA(long long ptr long) GetDlgItemText32A
238 stdcall GetDlgItemTextW(long long ptr long) GetDlgItemText32W
239 stdcall GetDoubleClickTime() GetDoubleClickTime32
240 stdcall GetFocus() GetFocus32
241 stdcall GetForegroundWindow() GetForegroundWindow32
242 stub GetIconInfo
243 stub GetInputDesktop
244 stdcall GetInputState() GetInputState32
245 stdcall GetInternalWindowPos(long ptr ptr) GetInternalWindowPos32
246 stdcall GetKBCodePage() GetKBCodePage32
247 stdcall GetKeyNameTextA(long ptr long) GetKeyNameText32A
248 stdcall GetKeyNameTextW(long ptr long) GetKeyNameText32W
249 stdcall GetKeyState(long) GetKeyState32
250 stdcall GetKeyboardLayout(long) GetKeyboardLayout
251 stdcall GetKeyboardLayoutList(long ptr) GetKeyboardLayoutList
252 stub GetKeyboardLayoutNameA
253 stub GetKeyboardLayoutNameW
254 stdcall GetKeyboardState(ptr) GetKeyboardState
255 stdcall GetKeyboardType(long) GetKeyboardType32
256 stdcall GetLastActivePopup(long) GetLastActivePopup32
257 stdcall GetMenu(long) GetMenu32
258 stdcall GetMenuCheckMarkDimensions() GetMenuCheckMarkDimensions
259 stub GetMenuContextHelpId
260 stub GetMenuDefaultItem
261 stub GetMenuIndex
262 stdcall GetMenuItemCount(long) GetMenuItemCount32
263 stdcall GetMenuItemID(long long) GetMenuItemID32
264 stdcall GetMenuItemInfoA(long long long ptr) GetMenuItemInfo32A
265 stdcall GetMenuItemInfoW(long long long ptr) GetMenuItemInfo32W
266 stub GetMenuItemRect
267 stdcall GetMenuState(long long long) GetMenuState32
268 stdcall GetMenuStringA(long long ptr long long) GetMenuString32A
269 stdcall GetMenuStringW(long long ptr long long) GetMenuString32W
270 stdcall GetMessageA(ptr long long long) GetMessage32A
271 stdcall GetMessageExtraInfo() GetMessageExtraInfo
272 stdcall GetMessagePos() GetMessagePos
273 stdcall GetMessageTime() GetMessageTime
274 stdcall GetMessageW(ptr long long long) GetMessage32W
275 stdcall GetNextDlgGroupItem(long long long) GetNextDlgGroupItem32
276 stdcall GetNextDlgTabItem(long long long) GetNextDlgTabItem32
277 stdcall GetOpenClipboardWindow() GetOpenClipboardWindow32
278 stdcall GetParent(long) GetParent32
279 stub GetPriorityClipboardFormat
280 stub GetProcessWindowStation
281 stdcall GetPropA(long ptr) GetProp32A
282 stdcall GetPropW(long ptr) GetProp32W
283 stub GetQueueStatus
284 stdcall GetScrollInfo(long long ptr) GetScrollInfo32
285 stdcall GetScrollPos(long long) GetScrollPos32
286 stdcall GetScrollRange(long long ptr ptr) GetScrollRange32
287 stdcall GetShellWindow() GetShellWindow32
288 stdcall GetSubMenu(long long) GetSubMenu32
289 stdcall GetSysColor(long) GetSysColor32
290 stdcall GetSysColorBrush(long) GetSysColorBrush32
291 stdcall GetSystemMenu(long long) GetSystemMenu32
292 stdcall GetSystemMetrics(long) GetSystemMetrics32
293 stdcall GetTabbedTextExtentA(long ptr long long ptr) GetTabbedTextExtent32A
294 stdcall GetTabbedTextExtentW(long ptr long long ptr) GetTabbedTextExtent32W
295 stub GetThreadDesktop
296 stdcall GetTopWindow(long) GetTopWindow32
297 stdcall GetUpdateRect(long ptr long) GetUpdateRect32
298 stdcall GetUpdateRgn(long long long) GetUpdateRgn32
299 stub GetUserObjectInformationA
300 stub GetUserObjectInformationW
301 stub GetUserObjectSecurity
302 stdcall GetWindow(long long) GetWindow32
303 stub GetWindowContextHelpId
304 stdcall GetWindowDC(long) GetWindowDC32
305 stdcall GetWindowLongA(long long) GetWindowLong32A
306 stdcall GetWindowLongW(long long) GetWindowLong32W
307 stdcall GetWindowPlacement(long ptr) GetWindowPlacement32
308 stdcall GetWindowRect(long ptr) GetWindowRect32
309 stdcall GetWindowTextA(long ptr long) GetWindowText32A
310 stdcall GetWindowTextLengthA(long) GetWindowTextLength32A
311 stdcall GetWindowTextLengthW(long) GetWindowTextLength32W
312 stdcall GetWindowTextW(long ptr long) GetWindowText32W
313 stdcall GetWindowThreadProcessId(long ptr) GetWindowThreadProcessId
314 stdcall GetWindowWord(long long) GetWindowWord32
315 stdcall GrayStringA(long long ptr long long long long long long) GrayString32A
316 stdcall GrayStringW(long long ptr long long long long long long) GrayString32W
317 stdcall HideCaret(long) HideCaret32
318 stdcall HiliteMenuItem(long long long long) HiliteMenuItem32
319 stub ImpersonateDdeClientWindow
320 stdcall InSendMessage() InSendMessage32
321 stdcall InflateRect(ptr long long) InflateRect32
322 stdcall InsertMenuA(long long long long ptr) InsertMenu32A
323 stdcall InsertMenuItemA(long long long ptr) InsertMenuItem32A
324 stdcall InsertMenuItemW(long long long ptr) InsertMenuItem32W
325 stdcall InsertMenuW(long long long long ptr) InsertMenu32W
326 stub InternalGetWindowText
327 stdcall IntersectRect(ptr ptr ptr) IntersectRect32
328 stdcall InvalidateRect(long ptr long) InvalidateRect32
329 stdcall InvalidateRgn(long long long) InvalidateRgn32
330 stdcall InvertRect(long ptr) InvertRect32
331 stdcall IsCharAlphaA(long) IsCharAlpha32A
332 stdcall IsCharAlphaNumericA(long) IsCharAlphaNumeric32A
333 stdcall IsCharAlphaNumericW(long) IsCharAlphaNumeric32W
334 stdcall IsCharAlphaW(long) IsCharAlpha32W
335 stdcall IsCharLowerA(long) IsCharLower32A
336 stdcall IsCharLowerW(long) IsCharLower32W
337 stdcall IsCharUpperA(long) IsCharUpper32A
338 stdcall IsCharUpperW(long) IsCharUpper32W
339 stdcall IsChild(long long) IsChild32
340 stdcall IsClipboardFormatAvailable(long) IsClipboardFormatAvailable32
341 stub IsDialogMessage
342 stdcall IsDialogMessageA(long ptr) IsDialogMessage32A
343 stdcall IsDialogMessageW(long ptr) IsDialogMessage32W
344 stdcall IsDlgButtonChecked(long long) IsDlgButtonChecked32
345 stdcall IsIconic(long) IsIconic32
346 stdcall IsMenu(long) IsMenu32
347 stdcall IsRectEmpty(ptr) IsRectEmpty32
348 stdcall IsWindow(long) IsWindow32
349 stdcall IsWindowEnabled(long) IsWindowEnabled32
350 stdcall IsWindowUnicode(long) IsWindowUnicode
351 stdcall IsWindowVisible(long) IsWindowVisible32
352 stdcall IsZoomed(long) IsZoomed32
353 stdcall KillSystemTimer(long long) KillSystemTimer32
354 stdcall KillTimer(long long) KillTimer32
355 stdcall LoadAcceleratorsA(long ptr) LoadAccelerators32A
356 stdcall LoadAcceleratorsW(long ptr) LoadAccelerators32W
357 stdcall LoadBitmapA(long ptr) LoadBitmap32A
358 stdcall LoadBitmapW(long ptr) LoadBitmap32W
359 stdcall LoadCursorA(long ptr) LoadCursor32A
360 stub LoadCursorFromFileA
361 stub LoadCursorFromFileW
362 stdcall LoadCursorW(long ptr) LoadCursor32W
363 stdcall LoadIconA(long ptr) LoadIcon32A
364 stdcall LoadIconW(long ptr) LoadIcon32W
365 stdcall LoadImageA(long ptr long long long long) LoadImage32A
366 stdcall LoadImageW(long ptr long long long long) LoadImage32W
367 stub LoadKeyboardLayoutA
368 stub LoadKeyboardLayoutW
369 stub LoadLocalFonts
370 stdcall LoadMenuA(long ptr) LoadMenu32A
371 stdcall LoadMenuIndirectA(ptr) LoadMenuIndirect32A
372 stdcall LoadMenuIndirectW(ptr) LoadMenuIndirect32W
373 stdcall LoadMenuW(long ptr) LoadMenu32W
374 stub LoadRemoteFonts
375 stdcall LoadStringA(long long ptr long) LoadString32A
376 stdcall LoadStringW(long long ptr long) LoadString32W
377 stub LockWindowStation
378 stdcall LockWindowUpdate(long) LockWindowUpdate32
378 stdcall LookupIconIdFromDirectory(ptr long) LookupIconIdFromDirectory
379 stdcall LookupIconIdFromDirectoryEx(ptr long long long long) LookupIconIdFromDirectoryEx32
381 stub MBToWCSEx
382 stdcall MapDialogRect(long ptr) MapDialogRect32
383 stdcall MapVirtualKeyA(long long) MapVirtualKey32A
384 stub MapVirtualKeyExA
385 stdcall MapVirtualKeyW(long long) MapVirtualKey32A
386 stdcall MapWindowPoints(long long ptr long) MapWindowPoints32
387 stub MenuItemFromPoint
388 stub MenuWindowProcA
389 stub MenuWindowProcW
390 stdcall MessageBeep(long) MessageBeep32
391 stdcall MessageBoxA(long ptr ptr long) MessageBox32A
392 stdcall MessageBoxExA(long ptr ptr long long) MessageBoxEx32A
393 stdcall MessageBoxExW(long ptr ptr long long) MessageBoxEx32W
394 stub MessageBoxIndirectA
395 stub MessageBoxIndirectW
396 stdcall MessageBoxW(long ptr ptr long) MessageBox32W
397 stdcall ModifyMenuA(long long long long ptr) ModifyMenu32A
398 stdcall ModifyMenuW(long long long long ptr) ModifyMenu32W
399 stdcall MoveWindow(long long long long long long) MoveWindow32
400 stdcall MsgWaitForMultipleObjects(long ptr long long long) MsgWaitForMultipleObjects
401 stdcall OemKeyScan(long) OemKeyScan
402 stdcall OemToCharA(ptr ptr) OemToChar32A
403 stdcall OemToCharBuffA(ptr ptr long) OemToCharBuff32A
404 stdcall OemToCharBuffW(ptr ptr long) OemToCharBuff32W
405 stdcall OemToCharW(ptr ptr) OemToChar32W
406 stdcall OffsetRect(ptr long long) OffsetRect32
407 stdcall OpenClipboard(long) OpenClipboard32
408 stub OpenDesktopA
409 stub OpenDesktopW
410 stdcall OpenIcon(long) OpenIcon32
411 stub OpenInputDesktop
412 stub OpenWindowStationA
413 stub OpenWindowStationW
414 stub PackDDElParam
415 stub PaintDesktop
416 stdcall PeekMessageA(ptr long long long long) PeekMessage32A
417 stdcall PeekMessageW(ptr long long long long) PeekMessage32W
418 stub PlaySoundEvent
419 stdcall PostMessageA(long long long long) PostMessage32A
420 stdcall PostMessageW(long long long long) PostMessage32W
421 stdcall PostQuitMessage(long) PostQuitMessage32
422 stub PostThreadMessageA
423 stub PostThreadMessageW
424 stdcall PtInRect(ptr long long) PtInRect32
425 stub QuerySendMessage
426 stdcall RedrawWindow(long ptr long long) RedrawWindow32
427 stdcall RegisterClassA(ptr) RegisterClass32A
428 stdcall RegisterClassExA(ptr) RegisterClassEx32A
429 stdcall RegisterClassExW(ptr) RegisterClassEx32W
430 stdcall RegisterClassW(ptr) RegisterClass32W
431 stdcall RegisterClipboardFormatA(ptr) RegisterClipboardFormat32A
432 stdcall RegisterClipboardFormatW(ptr) RegisterClipboardFormat32W
433 stub RegisterHotKey
434 stub RegisterLogonProcess
435 stub RegisterSystemThread
436 stub RegisterTasklist
437 stdcall RegisterWindowMessageA(ptr) RegisterWindowMessage32A
438 stdcall RegisterWindowMessageW(ptr) RegisterWindowMessage32W
439 stdcall ReleaseCapture() ReleaseCapture
440 stdcall ReleaseDC(long long) ReleaseDC32
441 stdcall RemoveMenu(long long long) RemoveMenu32
442 stdcall RemovePropA(long ptr) RemoveProp32A
443 stdcall RemovePropW(long ptr) RemoveProp32W
444 stub ReplyMessage
445 stub ResetDisplay
446 stub ReuseDDElParam
447 stdcall ScreenToClient(long ptr) ScreenToClient32
448 stdcall ScrollChildren(long long long long) ScrollChildren32
449 stdcall ScrollDC(long long long ptr ptr long ptr) ScrollDC32
450 stdcall ScrollWindow(long long long ptr ptr) ScrollWindow32
451 stdcall ScrollWindowEx(long long long ptr ptr long ptr long) ScrollWindowEx32
452 stdcall SendDlgItemMessageA(long long long long long) SendDlgItemMessage32A
453 stdcall SendDlgItemMessageW(long long long long long) SendDlgItemMessage32W
454 stdcall SendMessageA(long long long long) SendMessage32A
455 stub SendMessageCallbackA
456 stub SendMessageCallbackW
457 stub SendMessageTimeoutA
458 stub SendMessageTimeoutW
459 stdcall SendMessageW(long long long long) SendMessage32W
460 stub SendNotifyMessageA
461 stub SendNotifyMessageW
462 stub ServerSetFunctionPointers
463 stdcall SetActiveWindow(long) SetActiveWindow32
464 stdcall SetCapture(long) SetCapture32
465 stdcall SetCaretBlinkTime(long) SetCaretBlinkTime32
466 stdcall SetCaretPos(long long) SetCaretPos32
467 stdcall SetClassLongA(long long long) SetClassLong32A
468 stdcall SetClassLongW(long long long) SetClassLong32W
469 stdcall SetClassWord(long long long) SetClassWord32
470 stdcall SetClipboardData(long long) SetClipboardData32
471 stdcall SetClipboardViewer(long) SetClipboardViewer32
472 stdcall SetCursor(long) SetCursor32
473 stub SetCursorContents
474 stdcall SetCursorPos(long long) SetCursorPos32
475 stub SetDebugErrorLevel
476 stdcall SetDeskWallPaper(ptr) SetDeskWallPaper32
477 stdcall SetDlgItemInt(long long long long) SetDlgItemInt32
478 stdcall SetDlgItemTextA(long long ptr) SetDlgItemText32A
479 stdcall SetDlgItemTextW(long long ptr) SetDlgItemText32W
480 stdcall SetDoubleClickTime(long) SetDoubleClickTime32
481 stdcall SetFocus(long) SetFocus32
482 stdcall SetForegroundWindow(long) SetForegroundWindow32
483 stdcall SetInternalWindowPos(long long ptr ptr) SetInternalWindowPos32
484 stdcall SetKeyboardState(ptr) SetKeyboardState
485 stdcall SetLastErrorEx(long long) SetLastErrorEx
486 stub SetLogonNotifyWindow
487 stdcall SetMenu(long long) SetMenu32
488 stub SetMenuContextHelpId
489 stdcall SetMenuDefaultItem(long long long) SetMenuDefaultItem32
490 stdcall SetMenuItemBitmaps(long long long long long) SetMenuItemBitmaps32
491 stdcall SetMenuItemInfoA(long long long ptr) SetMenuItemInfo32A
492 stdcall SetMenuItemInfoW(long long long ptr) SetMenuItemInfo32W
493 stub SetMessageExtraInfo
494 stdcall SetMessageQueue(long) SetMessageQueue32
495 stdcall SetParent(long long) SetParent32
496 stub SetProcessWindowStation
497 stdcall SetPropA(long ptr long) SetProp32A
498 stdcall SetPropW(long ptr long) SetProp32W
499 stdcall SetRect(ptr long long long long) SetRect32
500 stdcall SetRectEmpty(ptr) SetRectEmpty32
501 stdcall SetScrollInfo(long long ptr long) SetScrollInfo32
502 stdcall SetScrollPos(long long long long) SetScrollPos32
503 stdcall SetScrollRange(long long long long long) SetScrollRange32
504 stub SetShellWindow
505 stdcall SetSysColors(long ptr ptr) SetSysColors32
506 stub SetSysColorsTemp
507 stub SetSystemCursor
508 stdcall SetSystemMenu(long long) SetSystemMenu32
509 stdcall SetSystemTimer(long long long ptr) SetSystemTimer32
510 stub SetThreadDesktop
511 stdcall SetTimer(long long long ptr) SetTimer32
512 stub SetUserObjectInformationA
513 stub SetUserObjectInformationW
514 stub SetUserObjectSecurity
515 stub SetWindowContextHelpId
516 stub SetWindowFullScreenState
517 stdcall SetWindowLongA(long long long) SetWindowLong32A
518 stdcall SetWindowLongW(long long long) SetWindowLong32W
519 stdcall SetWindowPlacement(long ptr) SetWindowPlacement32
520 stdcall SetWindowPos(long long long long long long long) SetWindowPos32
521 stub SetWindowStationUser
522 stdcall SetWindowTextA(long ptr) SetWindowText32A
523 stdcall SetWindowTextW(long ptr) SetWindowText32W
524 stdcall SetWindowWord(long long long) SetWindowWord32
525 stdcall SetWindowsHookA(long ptr) SetWindowsHook32A
526 stdcall SetWindowsHookExA(long long long long) SetWindowsHookEx32A
527 stdcall SetWindowsHookExW(long long long long) SetWindowsHookEx32W
528 stdcall SetWindowsHookW(long long long long) SetWindowsHook32W
529 stdcall ShowCaret(long) ShowCaret32
530 stdcall ShowCursor(long) ShowCursor32
531 stdcall ShowOwnedPopups(long long) ShowOwnedPopups32
532 stdcall ShowScrollBar(long long long) ShowScrollBar32
533 stub ShowStartGlass
534 stdcall ShowWindow(long long) ShowWindow32
535 stub ShowWindowAsync
536 stdcall SubtractRect(ptr ptr ptr) SubtractRect32
537 stdcall SwapMouseButton(long) SwapMouseButton32
538 stub SwitchDesktop
539 stdcall SwitchToThisWindow(long long) SwitchToThisWindow32
540 stdcall SystemParametersInfoA(long long ptr long) SystemParametersInfo32A
541 stdcall SystemParametersInfoW(long long ptr long) SystemParametersInfo32W
542 stdcall TabbedTextOutA(long long long ptr long long ptr long) TabbedTextOut32A
543 stdcall TabbedTextOutW(long long long ptr long long ptr long) TabbedTextOut32W
544 stub TileChildWindows
545 stub TileWindows
546 stdcall ToAscii(long long ptr ptr long) ToAscii32
547 stub ToAsciiEx
548 stub ToUnicode
549 stdcall TrackPopupMenu(long long long long long long ptr) TrackPopupMenu32
550 stdcall TrackPopupMenuEx(long long long long long ptr) TrackPopupMenuEx
551 stdcall TranslateAccelerator(long long ptr) TranslateAccelerator32
552 stdcall TranslateAcceleratorA(long long ptr) TranslateAccelerator32
553 stdcall TranslateAcceleratorW(long long ptr) TranslateAccelerator32
554 stub TranslateCharsetInfo
555 stdcall TranslateMDISysAccel(long ptr) TranslateMDISysAccel32
556 stdcall TranslateMessage(ptr) TranslateMessage32
557 stdcall UnhookWindowsHook(long ptr) UnhookWindowsHook32
558 stdcall UnhookWindowsHookEx(long) UnhookWindowsHookEx32
559 stdcall UnionRect(ptr ptr ptr) UnionRect32
560 stub UnloadKeyboardLayout
561 stub UnlockWindowStation
562 stub UnpackDDElParam
563 stdcall UnregisterClassA(ptr long) UnregisterClass32A
564 stdcall UnregisterClassW(ptr long) UnregisterClass32W
565 stub UnregisterHotKey
566 stub UpdatePerUserSystemParameters
567 stdcall UpdateWindow(long) UpdateWindow32
568 stub UserClientDllInitialize
569 stub UserRealizePalette
570 stub UserRegisterWowHandlers
571 stdcall ValidateRect(long ptr) ValidateRect32
572 stdcall ValidateRgn(long long) ValidateRgn32
573 stdcall VkKeyScanA(long) VkKeyScan32A
574 stub VkKeyScanExA
575 stub VkKeyScanExW
576 stdcall VkKeyScanW(long) VkKeyScan32W
577 stub WaitForInputIdle
578 stdcall WaitMessage() WaitMessage
579 stdcall WinHelpA(long ptr long long) WinHelp32A
580 stdcall WinHelpW(long ptr long long) WinHelp32W
581 stdcall WindowFromDC(long) WindowFromDC32
582 stdcall WindowFromPoint(long long) WindowFromPoint32
583 stub keybd_event
584 stub mouse_event
585 varargs wsprintfA() wsprintf32A
586 varargs wsprintfW() wsprintf32W
587 stdcall wvsprintfA(ptr ptr ptr) wvsprintf32A
588 stdcall wvsprintfW(ptr ptr ptr) wvsprintf32W
#late additions
589 stub ChangeDisplaySettingsA
590 stub ChangeDisplaySettingsW
591 stub EnumDesktopWindows
592 stub EnumDisplaySettingsA
593 stub EnumDisplaySettingsW
594 stub GetWindowRgn
595 stub MapVirtualKeyExW
596 stub RegisterServicesProcess
597 stub SetWindowRgn
598 stub ToUnicodeEx
599 stub DrawCaptionTempA
600 stub RegisterNetworkCapabilities
601 stub WNDPROC_CALLBACK
