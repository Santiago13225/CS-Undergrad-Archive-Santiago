#include <stdio.h>
#include <stdlib.h>

#include <fcntl.h>      //For O_* constants
#include <sys/stat.h>   //For mode constants
#include <semaphore.h>

//int main(void) {
int main(int argc, char *argv[]) {
  //sem_t *sem;

  //sem_close("demo");

  if(sem_unlink("/demo") == -1){
    perror("sem_unlink");
    exit(EXIT_FAILURE);
  }

  exit(EXIT_SUCCESS);
}