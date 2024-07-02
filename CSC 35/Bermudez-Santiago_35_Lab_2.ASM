;THIS PROGRAM Lab2 Hello_Neg It is 32bit for MASM on MSVC++
; FILL IN THE FOLLOWING WITH APPROPRIATE INFORMATION
;Santiago Bermudez
;CSC 35
;Spring 2021
;Instructor: Dr.Ghansah
;Tuesday, 2/9/21. 12:00pm
;LAB SECTION #11
;Program#2: Hello CSC 35 and Negative Numbers!
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

.data;	both variables declared in "data" area, vars consist of array of characters, each of which is a byte
msg1 BYTE "Hello CSC35 Class, Spring 2021!", 0dh, 0ah, 0	;msg1 and msg2 are variables
msg2 BYTE "My Name is Santiago Bermudez****!", 0dh, 0ah, 0		;0dh and 0ah are used for carriage return and line feed 

.code
 
main proc
;
;output the Hello Message on the Screen
;
  mov edx, OFFSET msg1		; edx points to a memory address identifiable by a label (*msg1, in this case)
  call writestring			; writestring assumes you have the characters to print in edx
  mov edx, OFFSET msg2		; edx points to a memory address identifiable by a label (*msg2, in this case)
  call writestring			; writestring assumes you have the characters to print in edx and write them out
;
;*******************************
; Negative and Positive numbers in Binary
;
  mov eax, 0fffffffh		;	moves hexadecimal value to eax register 
  add eax, 1				;	adds 1 to eax, giving us a hexadecimal value of 10000000
  neg eax					;	negates eax by 2's compliment, giving us a hexadecimal of f0000000
  add eax,20000001h			;	adds 20000001 to eax, giving us 10000001
  mov bx, -1				;	moves -1 to bx, giving us ebx with ffff for the 4 least significant bits
  add ax, bx				;	adds bx to ax, giving us 0000 for the 4 least significant bits on eax
  
  invoke exitprocess,0	;EXIT TO OS
main endp

end main
