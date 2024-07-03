#include <stdio.h>
#include <math.h>
#define PRINT_1 printf("1");
#define PRINT_0 printf("0");
#define UPDATEVALUE(pos) value=value-pow(2,pos);

int main(void) {
  int position = 7;
  int value = 192;

  printf ( "Please enter a number between 0-255 ");
  scanf ("%d", &value);
  do {
    if ( value >= pow(2, position)) {
      PRINT_1
      UPDATEVALUE(position)
    } else PRINT_0

    position--;
  }  while ( position >= 0 );


  
  printf("\n");

  return 0;
}