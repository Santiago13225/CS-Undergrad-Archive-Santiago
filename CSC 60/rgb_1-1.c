#include <stdio.h>

int main() {
unsigned int buffer[ 16 ] = { 0x00a0b0c0, 0x00a1b1c1 , 
0x00a2b2c2, 0xa3b3c3, 0xa4b4c4, 0xa5b5c5, 0xa6b6c6, 
0xa7b7c7, 0x00a8b8c8, 0x00a9b9c9,0x00aabaca, 0x00abbbcb, 
0x00acbccc, 0x00adbdcd, 0x00aebece, 0x00afbfcf } ;

/*  Sample code to extract blue, green and red pixel values 
unsigned char redValue = buffer[ 0] & 0xff ;
printf ( "redValue at cell 0=%x\n", redValue);

unsigned char greenValue = (buffer[ 0] & 0x0000ff00 ) >> 8 ;  // You have to shift 8 to the right
printf ( "greenValue at cell 0=%x\n", greenValue);

unsigned char blueValue = ( buffer[ 0] & 0x00ff0000)  >> 16 ; // You have to shift 16 to the right
printf ( "blueValue at cell 0=%x\n", blueValue);
*/

unsigned int i ,  sum = 0;
float average = 0;

// TASK 1 write a for loop to print all red pixel values using the sample code above
// and compute the average of all red values


// TASK 3 write a for loop to print all blue pixel values using the sample code above
// and compute the average of all blue values and print the average

 
for ( i =0, sum = 0 ; i < 16 ; i++ )
  {
    sum = sum +   (buffer[ i] & 0xff) ;
  }
  printf ( "Sum of red value =%x\n", sum);
  printf ( "Average of red values =%f\n", sum/16.0);

  for ( i =0 , sum = 0 ; i < 16 ; i++ )
  {
    sum = sum +   ((buffer[ i] & 0x0000ff00 ) >> 8) ;
  }
  printf ( "Sum of blue value =%x\n", sum);
  printf ( "Average of blue values =%f\n", sum/16.0);

   for ( i =0 , sum = 0 ; i < 16 ; i++ )
  {
    sum = sum +   (( buffer[ i] & 0x00ff0000)  >> 16) ;
  }
  printf ( "Sum of green value =%x\n", sum);
  printf ( "Average of green values =%f\n", sum/16.0);

return 0;
    
}