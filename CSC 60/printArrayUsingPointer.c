#include <stdio.h>
int main ( )
{
    unsigned char data[5] = { 0xAB, 0xAC, 0xAD, 0xAE, 0xAF };
    unsigned char i, *ptr = data, nCells;
    nCells = sizeof ( data ) / sizeof ( data[0]);

    

    for ( i = 0 ; i < nCells ; i++ )
      {
        printf ( "value at cell=%d is =0x%X \n", i, *ptr++);
      }
}