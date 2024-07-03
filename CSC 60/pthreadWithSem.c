// WITH SEMAPHORES

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#include <fcntl.h>           /* For O_* constants */
#include <sys/stat.h>        /* For mode constants */
#include <semaphore.h>

void *increment_counter( void *ptr );

#define NUM_THREADS 20
sem_t *sem;

int main ( int argc, char *argv[ ])
{
  pthread_t pt[NUM_THREADS] ;
  int  tid[NUM_THREADS] ;
  int counter  = 0;
  int flags =  O_CREAT | O_EXCL;

  unsigned int value=1, i;

  sem = sem_open(argv[1], flags, 0660, 1);
  if (sem == SEM_FAILED) {
    perror("sem_open");
    exit(EXIT_FAILURE);
  }

  for ( i = 0 ; i < NUM_THREADS; i++)
    tid[i] = pthread_create( &pt[i], NULL, increment_counter, (void*) &counter);

  for ( i = 0 ; i < NUM_THREADS; i++)
    pthread_join(pt[i] , NULL);
    printf("Counter %d \n", counter);
    exit(0);
}

void *increment_counter( void *ptr )
{
  int i ;
  for ( i = 0 ; i < 1000000; i++ ){
    if (sem_wait(sem) == -1) {
      perror("sem_wait");
      exit(EXIT_FAILURE);
    }

    (*(int *)ptr)++;

    if (sem_post(sem) == -1){
      perror("sem_post");
      exit(EXIT_FAILURE);
    }
  }
}