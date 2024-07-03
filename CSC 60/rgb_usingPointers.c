#include <stdio.h>

int main() {
unsigned int buffer[ 16 ] = { 0x00a1b1c1 , 0x00a2b2c2, 0xa3b3c3, 0xa4b4c4, 0xa5b5c5, 0xa6b6c6, 0xa7b7c7, 0x00a8b8c8, 0x00a9b9c9,0x00aabaca, 0x00abbbcb, 0x00acbccc, 0x00adbdcd, 0x00aebece, 0x00afbfcf } ;
unsigned char *ptr ;
ptr = (unsigned char *) &buffer [ 0 ];

/*  Sample code to extract blue, green and red pixel values
unsigned char redValue = *ptr ;
printf ( "redValue at cell 0=%x\n", redValue);

ptr++;
unsigned char greenValue = *ptr ; 
printf ( "greenValue at cell 0=%x\n", greenValue);

ptr++;
unsigned char blueValue = *ptr ;
printf ( "blueValue at cell 0=%x\n", blueValue);
*/

unsigned int i ,  sum = 0;
float average = 0;

// TASK 1 write a for loop to print all red pixel values using the sample code above
// and compute the average of all red values

average = 0, sum = 0;

// TASK 2 write a for loop to print all green pixel values using the sample code above
// and compute the average of all green values and print the average

average = 0, sum = 0 ;
// TASK 3 write a for loop to print all blue pixel values using the sample code above
// and compute the average of all blue values and print the average



return 0;
    
}