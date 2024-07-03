#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX_QUESTIONS 25

unsigned char dataBank[MAX_QUESTIONS*4] = {
'+', 2, 4, 6,  // index = 0 , operand1 operand2, answer
'-', 4, 4, 0,  // index = 4
'/', 4, 2, 2,  // index = 8
'*', 2, 4, 8,  // index = 12
'+', 3, 4, 7,  // index = 16
'-', 4, 1, 3,  // 20 
'-', 4, 2, 2,  // 24
'+', 1, 4, 5,
'*', 1, 4, 4,
'*', 3, 3, 9,
'+', 2, 2, 4,
'*', 5, 1, 5,
'/', 5, 1, 5,
'*', 2, 2, 4,
'+', 5, 4, 9,
'/', 3, 3, 1,
'/', 6, 3, 2,
'/', 6, 2, 3,
'+', 6, 2, 8,
'/', 8, 2, 4,
'/', 8, 4, 2,
'/', 8, 1, 8,
'-', 5, 2, 3,
'-', 7, 2, 5,
'-', 8, 2, 6
 };

int main  ( )
{
   srand ( time(NULL));
   unsigned char answer, i =0 ;

   unsigned char *qPtr = dataBank ;
   
   unsigned char *op1, *op2, *ans, *op;
   
   
   unsigned char input ;
   for ( i  = 0 ; i < 20 ; i+=4 ) {
	   op =  &dataBank[i];
       op1 = &dataBank[i+1];;
       op2 = &dataBank[i+2];;
       ans = &dataBank[i+3];;
	   
	   switch ( *op ) {
	    case '+':
	    printf ( "What is %d plus %d=", *op1, *op2);
		break;
		case '-':
	    printf ( "What is %d minus %d=", *op1, *op2);
		break;
		case '*':
	    printf ( "What is %d times %d=", *op1, *op2);
		break;
		case '/':
	    printf ( "What is %d divided %d=", *op1, *op2);
		break;
      }
   
       scanf ( "%d", &input);
   
   if ( *ans == input)
	   printf ( "Good Job");
     else
     printf ( "Oh no...");
     
   
   
   
   
   }
   
   
   // Expand the 
   

  

}
