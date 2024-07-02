;THIS PROGRAM IS 64bits for MASM on MSVC++
;SIMD INSTRUCTIONS, Ghansah, Test, 
;******THIS IS 64 BIT VERSION. MIGHT INCLUDE VECTOR 64 BIT INSTRUCTIONS****
;Uses 64bit Irvine Libraries for ALL i/o
;THIS PROGRAM IS FOR TESTING SIMD INSTRUCTION IN X86-64
COMMENT &
.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO ,dwExitCode:DWORD
INCLUDE c:\irvine\Irvine32.inc
include c:\irvine\macros.inc
includelib c:\irvine\irvine32.lib
includelib c:\irvine\kernel32.lib
includelib c:\irvine\user32.lib
&

ExitProcess 	proto
ReadInt64       proto
ReadString      proto
WriteString		proto
WriteInt64		proto
WriteHex32		proto
WriteHex64		proto
Crlf 				proto

.data
MyInt1 DWORD 0,1,2,3				;FOR SIMD
MyInt2 DWORD 5,5,5,5				;FOR SIMD
;

.code
main proc
;SIMD CODE
movdqu xmm0,xmmword ptr [MyInt1]		;read 128b of integer into SSE Register
movdqu xmm1,xmmword ptr [MyInt2]
paddd xmm0,xmm1                     ;packed add double. ie add the corresponding double words
                                    ;(bits) packed in xmm registers.


  mov   ecx,0
  call  ExitProcess	;EXIT TO OS
main endp
PUBLIC main



 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;  ;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
end 
