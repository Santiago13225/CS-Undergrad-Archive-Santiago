;THIS IS DEMONSTRATION PROGRAM for LAB4. It is a 32bit App for MASM on MSVC++
;ARITHMETIC INSTRUCTIONS, IRVINE LIB, SINGLE-DIGIT OUTPUT EXAMPLE
;INSTRUCTOR: Ghansah, Testing, Lab4EXAMPLE ADD, SUB, MUL, DIV Instructions
;Z = X + Y + X*Y - Y/4
;Z = Z MOD 5
;*IN FUTURE, MODIFY CODE TO DEAL WITH NEGATIVE VALUES
COMMENT &
Objectives: Students will learn to use DIV Instruction for integer division and  
obtaining remainder (ie. % which is MOD operator). They will also learn to use Irvine 
Libraries to Output both single and string of Characters to the Screen


The High Level C code follows
void main()
{
	int X;
	int Y=9;
	int Result;

	X=2;
	X=X+1;
	Y=Y+2;
	Result=X+Y+X*Y-Y/4;
	Result=Result%5; Result MOD 5
	Print ("Result =", Result)

}

&
;
.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO ,dwExitCode:DWORD
INCLUDE c:\irvine\Irvine32.inc
include c:\irvine\macros.inc
includelib c:\irvine\irvine32.lib
includelib c:\irvine\kernel32.lib
includelib c:\irvine\user32.lib

.data
X DWORD 0
Y DWORD 9
Result DWORD ?
ResultMsg BYTE "Result = ",0
;
.code
 
main proc
  mov X,2		;X=2
  inc X		;X++ i.e. X=X+1
  add Y,2		;Y=Y+2
  mov eax,X	;eax=eax+X Note:eax will be used to accumulate result 
  add eax,Y	; eax = eax+Y
  mov ebx,eax	;ebx=X+Y. save eax, will need it to do X*Y (multiplication)
  mov eax,X
  mul Y		; eax=X*Y
  add eax,ebx	;eax=X*Y + X+Y
  mov Result,eax	;Result= X*Y + X+Y 
  ;; DIVISION AND MODULUS PART TO ENSURE SINGLE DIGIT RESULT TO USE WRITECHAR
  ; Result = X+Y + X*Y - Y/4
  ; Result = Result MOD 5
  mov ebx,eax		; save Result
  mov eax,Y			; get ready to do Y/4

  mov edx,0			;zero out edx
  mov ebx,4
  div ebx			;Now eax=Y/4
  sub Result,eax	;Result = Result-Y/4
  mov eax,Result	;Get Ready to do Result MOD 5
  mov edx,0
  mov ebx,5
  div ebx			;edx= Result MOD 5
  mov Result,edx
  add Result, 30h	; convert result to ASCII character. Only works if Result is a BYTE
  mov edx, OFFSET ResultMsg
  call WriteString
  mov eax, Result	; AL contains Number. write the number to the screen
  call WriteChar	;print result on the screen
  call CrLf			; Go to Newline
  invoke exitprocess,0	;EXIT TO OS
main endp

end main
