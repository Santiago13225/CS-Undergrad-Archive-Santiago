#include <stdio.h>

int main ( )
 {
  unsigned char a  = 0, e = 0 , i = 0 , o = 0, u = 0;
  char ch = '\0' ; // NULL Terminator

  printf ("Enter a text and hit enter key \n");
  while ( ch != '\n' ) {
    ch = getchar() ;
    switch  ( ch )  {
     case 97:
     case 65:  //  65 = 'A',  97 = 'a'
      a = 1;
      break;
     case 'e' :
     case 'E' :
      e = 1 ;
      break;
     case 'i' :
     case 'I' :
      i = 1 ;
      break;
     case 'o' :
     case 'O' :
      o = 1 ;
      break;
     case 'u' :
     case 'U' :
      u = 1 ;
      break;
     default:
      break;
   }
  }

 if ( a >= 1 && e  > 0 && i && o == 1 && u != 0 )
   printf ( "Entered text has all vowels \n");
 else
   printf ( "Entered text doesn't have all vowels \n");

  return 0;
 }
