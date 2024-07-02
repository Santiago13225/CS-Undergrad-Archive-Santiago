;THIS PROGRAM is Demo of LAB3 Example. It is 32bit for MASM on MSVC++
;ARITH instructions: ADD, SUB, MUL
;How to Declare Variables
;Z = X + Y + X*Y
;*IN FUTURE, MODIFY CODE TO DEAL WITH NEGATIVE VALUES
COMMENT &
Objectives: Students will learn to use Registers to do Step by Step ASM Instructions 
to handle Intel Architecture Restrictions such as: 1) No memory-memory ADD or MOV
2) We Cannot Add more than 2 items at a time in same instruction 

The High Level C code follows
void main()
{
	int X;
	int Y=9;
	int Z=12;
	int Result;

	X=2;
	X=X+1;
	Y=Y+2;
	Result=X+Y+X*Y-Z;
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
X DWORD ?
Y DWORD 9
Z DWORD 12
Result DWORD ?

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
  sub eax,Z		;eax=X*Y + X+Y - Z
  mov Result,eax	;Result= X*Y + X+Y-Z 
  invoke exitprocess,0	;EXIT TO OS
main endp

end main
