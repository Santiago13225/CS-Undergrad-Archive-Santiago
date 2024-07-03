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
  int value;
  if(sem_getvalue(sem, &value)){
    perror("sem_getvalue");
    exit(EXIT_FAILURE);
  }

  printf("%d \n", value);
  exit(EXIT_SUCCESS);
}