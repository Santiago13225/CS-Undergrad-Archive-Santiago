#include <stdio.h>
#include <stdlib.h>

#include <fcntl.h>      //For O_* constants
#include <sys/stat.h>   //For mode constants
#include <semaphore.h>

//int main(void) {
int main(int argc, char *argv[]) {
  int flags, opt;
  mode_t perms;
  unsigned int value;
  sem_t *sem;
  flags = 0;
  
  flags |= O_CREAT;
  flags |= O_EXCL;

  sem = sem_open("/open", flags, 0600, 0);
  if(sem == SEM_FAILED){
    perror("sem_open");
    exit(EXIT_FAILURE);
  }

  exit(EXIT_SUCCESS);
}