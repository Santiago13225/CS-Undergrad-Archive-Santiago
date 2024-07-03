#include <stdio.h>



int main(void) {
 
  int value = 81;

  int nQ = value / 25 ;
  printf ( "%d quarters\n", nQ);
  value = value%25;
  int nD = value / 10 ;
  printf ( "%d Dimes\n", nD);
  value = value%10;
  int nN = value / 5 ;
  printf ( "%d Dimes\n", nN);
  int nP = value%5;
  printf("%d Pennies\n", nP);


  return 0;
}