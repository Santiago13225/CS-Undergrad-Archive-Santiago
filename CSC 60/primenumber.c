#include <stdio.h>

int main ()
{
  unsigned char number;
  printf ( "Enter a number 0-255 \n");

  scanf ("%hhu", &number);
  int i, flag = 0;

  for ( i = 2; i < number /2 ; i++ ) {
     if ( number % i == 0 ) {
       flag = 1;
       break;
     }
  }
  if ( flag == 0)
    printf ( "%hhu is a prime number\n", number);
  else
    printf ( "%hhu is not a prime number\n", number);
   

}