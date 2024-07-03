#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/times.h>
#include <time.h>
#include <unistd.h>



int current_number = 2;  // SHARED VARIABLE AMONG THREADS
pthread_mutex_t count_mutex = PTHREAD_MUTEX_INITIALIZER;
  int numberOfPrimeNumber = 0;

void *PrintPrimeNumbers( void *ptr )  // FUNCTION PASSED TO THREADS
{
  pthread_t  id = pthread_self( ) ;
  int myCopy = 0;
  int num  ;

  do {
           pthread_mutex_lock(&count_mutex); // FUNCTION CALL
                           // When two threads access lock, only one of them
                           // can lock, the others would have to wait.
           myCopy = current_number++;   // critical section
           pthread_mutex_unlock(&count_mutex);

   for ( num = 2 ; num < myCopy ; num++ )
      {
         if ( myCopy%num == 0 )
            break;
      }
   if ( num == myCopy) {
           pthread_mutex_lock(&count_mutex); // FUNCTION CALL
    numberOfPrimeNumber++;
           pthread_mutex_unlock(&count_mutex);
    //printf ( "prime number 0x%8x: %d %d \n",  id, numberOfPrimeNumber,  myCopy  );
  }


  } while ( current_number < 500000 );
   pthread_exit((void*) 0);
}

main( )
{
   clock_t start, end;

   struct tms st_start, st_end;
   start = times (&st_start);

     pthread_t T1, T2, T3, T4, T5;

     int  id1, id2, id3, id4, id5;

     id1 = pthread_create( &T1, NULL, PrintPrimeNumbers, (void*) NULL);
     id2 = pthread_create( &T2, NULL, PrintPrimeNumbers, (void*) NULL);
     id3 = pthread_create( &T3, NULL, PrintPrimeNumbers, (void*) NULL);
     id4 = pthread_create( &T4, NULL, PrintPrimeNumbers, (void*) NULL);
     id5 = pthread_create( &T5, NULL, PrintPrimeNumbers, (void*) NULL);

     pthread_join( T1, NULL);
     pthread_join( T2, NULL);
     pthread_join( T3, NULL);
     pthread_join( T4, NULL);
     pthread_join( T5, NULL);

     end = times (&st_end);
printf ( "Time taken by system command %6.2f \n", (float)( end-start)/sysconf( _SC_CLK_TCK ) );

printf ( "Time taken by parent process in User mode %6.2f \n", (float)( st_end.tms_utime-st_start.tms_utime)/sysconf( _SC_CLK_TCK ) );
printf ( "Time taken by parent process in kernel mode %6.2f \n", (float)( st_end.tms_stime-st_start.tms_stime)/sysconf( _SC_CLK_TCK ) );

printf ( "Time taken by child process in user mode %6.2f \n", (float)( st_end.tms_cutime-st_start.tms_cutime)/sysconf( _SC_CLK_TCK ) );
printf ( "Time taken by child process in kernel mode %6.2f \n", (float)( st_end.tms_cstime-st_start.tms_cstime)/sysconf( _SC_CLK_TCK ) );

     printf ( "prime number %d \n",   numberOfPrimeNumber    );


pthread_exit(NULL);
}