#include <stdio.h>
#include <math.h>
#define PRINT_1 printf("1");
#define PRINT_0 printf("0");
#define UPDATEVALUE(pos) value=value-pow(2,pos);

int main(void) {
  int position = 7;
  int value = 128;

  printf ( "Please enter a number between 0-255 ");
  scanf ("%d", &value);
  for ( position=7; position>=0;position--)
    if ( value >= pow(2, position)) {
      PRINT_1
      UPDATEVALUE(position)
    } else PRINT_0
 
  printf("\n");

  return 0;
}