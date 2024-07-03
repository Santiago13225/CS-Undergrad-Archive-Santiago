#include <stdio.h>
 
#define MAX_PRIMES 5 //Constant variable of 5.
 
int main() {
   unsigned char data[MAX_PRIMES] = {0};//Here, we declare a 5 cell unsigned char array.
   int y;//Here, we declare an integer to use in our 1st for loop.
   for(y = 0; y < MAX_PRIMES; y++){//For loop that iterates 5 times.
       unsigned char number;//Declares unsigned char num for use in array.
       printf ( "Enter a number from 2 to 255: \n");
       scanf ("%hhu", &number);//Gets user input.
       int i, flag = 0;
       for ( i = 2; i < number /2 ; i++ ) {//For loop to check if prime.
         if ( number % i == 0 ) {//Modulus helps determine "primeness" of number.
           flag = 1;//If not prime, set to 1.
           break;
         }
       }
     if ( flag == 0) {//If prime, store in array.
       printf ( "%hhu is a prime number\n", number);
       data[y] = number;
     } else //Else, ignore.
       printf ( "%hhu is not a prime number\n", number);
   }
  
   unsigned char x, *ptr = data, nCells;
   nCells = sizeof (data) / sizeof (data[0]);
   for(x = 0; x < nCells; x++){//For loop to print array.
       printf("Value at cell %d is %x \n", x, *ptr++);
   }
  
   return 0;
}