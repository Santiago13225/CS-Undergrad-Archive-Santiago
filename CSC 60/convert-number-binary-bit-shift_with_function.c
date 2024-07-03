#include <stdio.h>
#include <math.h>
#define PRINT_1 printf("1");
#define PRINT_0 printf("0");

void shift_and_print( int num, int pos)
{
  if ( num & 1 << pos )
    PRINT_1
  else
    PRINT_0
  
}
int main(void) {

  int value = 192 ;
  int position = 7;
  while ( position >= 0)
   shift_and_print (value , position--);
    
  printf("\n");

  return 0;
}