// WITHOUT SEMAPHORES
/*

20 threads are incrementing a shared variable without synchronization.
This results in incorrect values

*/
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#include <fcntl.h>           /* For O_* constants */
#include <sys/stat.h>        /* For mode constants */
#include <semaphore.h>

void *increment_counter( void *ptr );

#define NUM_THREADS 20

int main(int argc, char *argv[ ] )
{
  pthread_t pt[NUM_THREADS] ;
  int  tid[NUM_THREADS] ;
  int counter  = 0;

  unsigned int value=1, i;

  for ( i = 0 ; i < NUM_THREADS; i++)
    tid[i] = pthread_create( &pt[i], NULL, increment_counter, (void*) &counter);

  for ( i = 0 ; i < NUM_THREADS; i++)
    pthread_join(pt[i] , NULL);
    printf("Counter %d \n", counter);
    return ( 0 );
}

void *increment_counter( void *ptr )
{
  int i ;
  for ( i = 0 ; i < 1000000; i++ )
    (*(int *)ptr)++;
}
