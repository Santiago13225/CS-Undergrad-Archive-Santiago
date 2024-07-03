#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
pthread_mutex_t myMutex = PTHREAD_MUTEX_INITIALIZER;//KEY

int number = 2;
int counter = 0;

/*
int IsItPrimeorNot(unsigned int value ){
write a function to calculate if a number is prime or not.
if it is prime, return 1
if it is not prime return 0
}
*/
int IsItPrimeorNot(unsigned int value){
  int flag = 0;
  for(int i = 2; i <= value/2; i++){
    if(value%i == 0){//If value is not prime.
      flag = 1;
      break;
    }
  }
  if(flag == 1){//If number is not prime.
    return 0;//Return 0;
  }
  return 1;//If number is prime, return 1.
}
void *calculate(){
  while(number <= 100000){
    pthread_mutex_lock(&myMutex);
    int mycopy = number++;//Picks a number, and increments. 
    pthread_mutex_unlock(&myMutex);
    //Now check if the mycopy is prime or not.
    if(IsItPrimeorNot(mycopy) == 1){
      pthread_mutex_lock(&myMutex);
      counter++;
      pthread_mutex_unlock(&myMutex);
    }
  }
}
//int main (int argc, char *argv[])
int main()
{
  pthread_t t1, t2;//two threads 
  int thread1, thread2;

  thread1 = pthread_create(&t1, NULL, calculate, NULL);
  thread2 = pthread_create(&t2, NULL, calculate, NULL);

  pthread_join(t1, NULL);
  pthread_join(t2, NULL);

  printf ("count is %d \n", counter);
}