;THIS IS DEMONSTRATION PROGRAM for LAB6. It is a 32bit App for MASM on MSVC++
;IT MODIFIES LAB4 DEMO EXAMPLE TO USE TWO PROCEDURES.
;ARITHMETIC INSTRUCTIONS, IRVINE LIB, ONE PROCEDURE COMPUTES
;ANOTHER PROCEDURE PRINTS SINGLE-DIGIT OUTPUT ON SCREEN
;INSTRUCTOR: Ghansah, Testing, Lab6EXAMPLE based on Lab4DEMO_EXAMPLE 	
;PROCEDURES, REGISTER PARAMETER PASSINGADD, SUB, MUL, DIV Instructions
;Z = X + Y + X*Y - Y/4
;Z = Z MOD 5
;*IN FUTURE, MODIFY CODE TO DEAL WITH NEGATIVE VALUES
COMMENT &
Objectives: Students will learn to use DIV Instruction for integer division and  
obtaining remainder (ie. % which is MOD operator). They will also learn to use Irvine 
Libraries to Output both single and string of Characters to the Screen

************************************
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
**********MAIN AND TWO FUNCTIONS*******
void main()
{
	int X;
	int Y=9;
	int Result;
	
	X=2;
Result = computeR(X,Y)
outputR (Result)
}	

int computeR (int a, int b);
{
	a=a+1;
	b=b+2;
	return ((a+b+a*b-b/4)%5) ;
}

outputR( int c);	
{	Print ("Result =", c)

}

&
;*****EQUIVALENT ASSEMBLY CODE FOR ABOVE C PROGRAM*****
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
;parameter passing via registers
;Entry. esi=X, edi=Y, Exit. eax contains result
  mov esi,X
  mov edi,Y
  call computeR
  mov Result,eax
;Passing Parameter to OutputR procedure
  mov ebx,Result
  call outputR
invoke exitprocess,0	;EXIT TO OS
main endp

computeR proc
;This Procedure performs computation using two parameters. 
;It receives parameters via registers and returns results via registers as follows
;Entry: esi= 1st parameter eg. a=X, edi= 2nd parameter eg. b=Y, 
;Exit: eax contains result to returned to caller


  inc esi		;a++ i.e. a=a+1
  add edi,2		;b=b+2
  mov eax,esi	;eax=eax+a Note:eax will be used to accumulate result 
  add eax,edi	; eax = eax+b
  mov ebx,eax	;ebx=a+b. save eax, will need it to do X*Y (multiplication)
  mov eax,esi
  mul edi		; eax=a*b
  add eax,ebx	;eax=a*b + a+b
  mov ecx,eax	;Result=ecx= a*b + a+b 
  ;; DIVISION AND MODULUS PART TO ENSURE SINGLE DIGIT RESULT TO USE WRITECHAR
  ; eax = a+b + a*b - b/4
  ; eax = eax MOD 7
  mov ebx,eax		; save Result
  mov eax,edi			; get ready to do b/4

  mov edx,0			;zero out edx
  mov ebx,4
  div ebx			;Now eax=b/4
  sub ecx,eax	;Result = Result-b/4
  mov eax,ecx	;Get Ready to do Result MOD 7
  mov edx,0
  mov ebx,7
  div ebx			;edx= eax MOD 7
  mov eax,edx		;eax returns the result
  ret				;Return from Procedure
computeR endp

outputR proc
;This procedure outputs single digit on the screen in the format 
;"c=" c where c is the variable
;It receives parameters via registers and returns results via registers as follows
;Entry: ebx= parameter that contains digit to be printed on screen.  
;Exit: Nothing

  add ebx, 30h	; convert Number to ASCII character. 
  
  mov edx, OFFSET ResultMsg;	NOTE: This could be parameter from main
  call WriteString
  mov eax, ebx	; AL contains Number. write the number to the screen
  call WriteChar	;print result on the screen
  call CrLf			; Go to Newline
  ret
outputR endp

end main
