#include <stdio.h>
#include <stdlib.h>

#include <fcntl.h>      //For O_* constants
#include <sys/stat.h>   //For mode constants
#include <semaphore.h>

//int main(void) {
int main(int argc, char *argv[]) {
  sem_t *sem;
  sem = sem_open("/demo", 0);
  if(sem == SEM_FAILED) {
    perror("sem_open");
    exit(EXIT_FAILURE);
  }

  if(sem_wait(sem) == -1) {
    perror("sem_wait");
    exit(EXIT_FAILURE);
  }

  printf("%ld sem_wait() succeeded\n", (long) getpid());
  exit(EXIT_SUCCESS);
}