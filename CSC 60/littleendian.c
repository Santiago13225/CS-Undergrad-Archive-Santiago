#include <stdio.h>
#include <stdlib.h>
int main ( )
{
  int x = 0x01020304;

  char *ptr = ( char *) &x ;

  printf ( "address of ptr=%p value=%x\n", ptr, *ptr);
  ptr++;
  printf ( "address of ptr=%p value=%x\n", ptr, *ptr);
  ptr++;
  printf ( "address of ptr=%p value=%x\n", ptr, *ptr);
  ptr++;
  printf ( "address of ptr=%p value=%x\n", ptr, *ptr);

}
