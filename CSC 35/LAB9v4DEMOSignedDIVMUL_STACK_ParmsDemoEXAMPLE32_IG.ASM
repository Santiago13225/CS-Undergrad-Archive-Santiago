;THIS IS DEMONSTRATION PROGRAM for LAB9. It is a 32bit App for MASM on MSVC++
;IT MODIFIES LAB7 DEMO EXAMPLE TO USE TWO PROCEDURES with stack parameter passing.
;ARITHMETIC INSTRUCTIONS, IRVINE LIB, ONE PROCEDURE COMPUTES
;ANOTHER PROCEDURE PRINTS SINGLE-DIGIT OUTPUT ON SCREEN
;INSTRUCTOR: Ghansah, Testing, Lab9EXAMPLE based on Lab6DEMO_EXAMPLE 	
;PROCEDURES, REGISTER PARAMETER PASSING using ADD, SUB, iMUL, iDIV, CDQ, and NEG Instructions
;Z = X + Y + X*Y - Y*Y/4
;Z = Z MOD 7
;*THIS CODE DEALS WITH NEGATIVE VALUES
COMMENT &
Objectives: Students will learn to use iDIV Instruction for integer division and  
obtaining remainder (ie. % which is MOD operator). They will also learn to use Irvine 
Libraries to input single characters and Output both single and string of Characters to the Screen

************************************
The High Level C code follows
void main()
{
	int X;
	int Y=9;
	int Result;

	X=Read();
	X=X+1;
	Y=Y+2;
	Result=X+Y+X*Y-Y*Y/4;
	Result=Result%7; Result MOD 7
	Print ("Result =", Result)

}
**********MAIN AND TWO FUNCTIONS*******
void main()
{
	int X;
	int Y=9;
	int Result;
	
	X=Read();
Result = computeR(X,Y)
outputR (Result)
}	

int computeR (int a, int b);
{
	a=a+1;
	b=b+2;
	return ((a+b+a*b-b*b/4)%7) ;
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
X DWORD 0						;unsigned variable
Y SDWORD -9					;signed variable
Result SDWORD ?					;signed variable
xprompt BYTE "INPUT X= ",0
quotient_msg BYTE "Quotient = ",0 
ResultMsg BYTE "Result = ",0
continue BYTE "Press Any Any key to continue or q to QUIT", 0

;
.code
 
main proc
add Y,2		;Y=Y+2. Y is fixed but X can change
topMain:
mov edx,offset xprompt
call WriteString
call ReadChar
call WriteChar
;call CrLf
sub al,30h
movsx eax,al
mov X, eax

  inc X		;X++ i.e. X=X+1
  
  call CrLf


			;parameter passing via registers
			;Entry. esi=X, edi=Y, Exit. eax contains result
  ;mov esi,X
  ;mov edi,Y
			;input parameter passing via Stack
  push Y
  push X

  call computeR
					;Caller Cleans up the Stack
  add esp,8			;deallocate two 4Byte input parameters from stack

  mov Result,eax		;output returned via Register eax
  mov edx, OFFSET ResultMsg;	Print "Result="
  call WriteString
						;Passing Parameter to OutputR procedure
  ;mov ebx,Result
  push Result
  call outputR
  ;Caller Cleans up the Stack
  add esp,4			;deallocate one 4Byte input parameter from stack
  call CrLf
  mov edx, offset continue  ;prompt to continue or quit
  call WriteString
   

call CrLf			; Go to Newline
call CrLf
  call readchar             ;this procedure does not echo
  cmp al,'q'
  jne topMain	

invoke exitprocess,0	;EXIT TO OS
main endp

computeR proc
;This Procedure performs computation using two parameters. 
;It receives parameters via Stack and returns results via registers as follows
;Entry: esi=[ebp+8]= 2nd parameter pushed on stack eg. a=X, 
;edi= [ebp+12] 1st parameter pushed on stack eg. b=Y, 
;Exit: eax contains result to returned to caller
  push ebp						;set up stack frame
  mov ebp,esp

  mov eax,[ebp+8]	;eax=eax+a Note:eax will be used to accumulate result 
  add eax,[ebp+12]	; eax = eax+b
  mov ebx,eax	;ebx=a+b. save eax, will need it to do X*Y (multiplication)
  mov eax,[ebp+8]
  imul DWORD PTR [ebp+12]		; eax=a*b
  add eax,ebx	;eax=a*b + a+b
  mov ecx,eax	;Result=ecx= a*b + a+b 
  ;; DIVISION AND MODULUS PART TO ENSURE SINGLE DIGIT RESULT TO USE WRITECHAR
  ; eax = a+b + a*b - b*b/4
  ; eax = eax MOD 7
  ;mov ebx,eax		; save Result
  ; get ready to do b*b
  mov eax,[ebp+12]
  imul eax
						; eax = eax*eax=b*b
  						; get ready to do b*b/4

  ;mov edx,0			;zero out edx
  cdq
  mov ebx,4
  idiv ebx			;Now eax=b*b/4
  sub ecx,eax	;Result = Result-b*b/4
  mov eax,ecx	;Get Ready to do Result MOD 7
  ;mov edx,0
  cdq
  mov ebx,7
  idiv ebx			;edx= eax MOD 7
  mov eax,edx		;eax returns the result
  mov esp,ebp
  pop ebp

  ret				;Return from Procedure
computeR endp

outputR proc
;This procedure outputs single digit on the screen in the format 
;"c=" c where c is the variable
;It receives parameters via Stack and returns results via registers as follows
;Entry: [ebp+8]]=ebx= parameter that contains digit to be printed on screen.  
;Exit: Nothing
  push ebp						;set up stack frame
  mov ebp,esp

  mov eax, [ebp+8]  ; Get parameter (W=number) to be printed from the stack
  cmp eax,0         ;See if number is negative or positive
  jge ConvertToDec  ;Number is >=0 so convert to Decimal and print
  neg eax           ;Number is < 0 (negative) so convert to positive before converting to decimal
  mov ebx,eax           ;save it temporarily
  mov al, "-"
  call WriteChar    ;Display Negative Sign
  mov eax,ebx       ;get Number back into eax. It be the dividend in the division below

  ConvertToDec:
    add eax, 30h	; convert Number to ASCII character. 
    
  ; AL contains Number. write the number to the screen
  call WriteChar	;print result on the screen
 mov esp,ebp
  pop ebp
  ret
outputR endp

end main
