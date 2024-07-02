;THIS PROGRAM Lab2 Hello_Neg It is 32bit for MASM on MSVC++
; FILL IN THE FOLLOWING WITH APPROPRIATE INFORMATION
;YOUR FULL NAME
;CSC 35
;SEMESTER
;Instructor: Dr.Ghansah
;DAY, DATE and TIME
;LAB SECTION #
;Program# and Title
COMMENT &
Objectives: Students will learn to output to screen using Libraries and Deal with Negative Numbers

&
;
.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO ,dwExitCode:DWORD
INCLUDE Irvine32.inc
;This is a comment
;The following is group comment delimited with &
COMMENT &
INCLUDE c:\irvine\Irvine32.inc
include c:\irvine\macros.inc
includelib c:\irvine\irvine32.lib
includelib c:\irvine\kernel32.lib
includelib c:\irvine\user32.lib
&

.data
msg1 BYTE "Hello CSC35!", 0dh, 0ah, 0
msg2 BYTE "My Name is Your Full Name!", 0dh, 0ah, 0

.code
 
main proc
;
;output the Hello Message on the Screen
;
  mov edx, OFFSET msg1
  call writestring
  mov edx, OFFSET msg2
  call writestring
;
;*******************************
; Negative and Positive numbers in Binary
;
  mov eax, 0fffffffh
  add eax, 1
  neg eax
  add eax,20000001h
  mov bx, -1
  add ax, bx
  
  invoke exitprocess,0	;EXIT TO OS
main endp

end main
