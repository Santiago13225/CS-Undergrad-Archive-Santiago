#include <stdio.h>
#include <math.h>


int main(void) {
 
  int value = 145;
  int i, coin;
  for ( i = 0 ; i < 4; i++, value = value%coin) {
    if ( i == 0) {
       coin=25; 
       printf ( "%d quarters\n", value / coin);
    }
    else if ( i == 1) {
      coin=10; 
      printf ( "%d Dimes\n", value / coin);
    } 
    else if ( i == 2) {
      coin=5; 
      printf ( "%d Nickels\n", value / coin);
    }
    else if ( i == 3) {
      coin=1; 
      printf ( "%d Pennies\n", value / coin);
    }
  }

  return 0;
}