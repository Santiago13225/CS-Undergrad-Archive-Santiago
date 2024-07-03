#include <stdio.h>
#include <math.h>
#define PRINT_1 printf("1");
#define PRINT_0 printf("0");
int main(void) {

  int value = 198 ;
  
  printf ( "Please enter a number between 0-255 ");
  scanf ("%d", &value);
  int position = 7;
  while ( position >= 0)
    if ( value & 1 << position-- )
    PRINT_1
  else
    PRINT_0
    
  printf("\n");

  return 0;
}