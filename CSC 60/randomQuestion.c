#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void){
  FILE *fp = fopen ("questionBank.txt", "r");
  
  if(fp == NULL){
    perror("Unable to read the file.");
    exit(1);
  }
  
  //50 Qs in all.
  int lowerB = 0;
  int upperB = 49;
  srand(time(0));

  char reject[300];//Buffer needed for ignored questions.
  
  int num = (rand() % (upperB - lowerB + 1)) + lowerB;
  //printf("%d \n", num);
  int i = 0;
  /*Below is a while loop that uses fgets to read through the questions iteratively. Due to formatting, we use fgets 6 times for each i.*/
  while(i < num){
    fgets(reject, 300, fp);
    fgets(reject, 300, fp);
    fgets(reject, 300, fp);
    fgets(reject, 300, fp);
    fgets(reject, 300, fp);
    fgets(reject, 300, fp);
    i++;//Increments i, so we don't get infinite loop.
    //printf("Read past question from fgets: %d\n", i);
  }

  char data[300];//Buffer needed for fgets.

  int ans = 0;//Question answer variable.
  int answer = 0;//User input variable.
  fgets(data, 300, fp);
  printf("Question: %s", data);//Question
  fgets(data, 300, fp);
  printf("%s", data);//Answer 1
  fgets(data, 300, fp);
  printf("%s", data);//Answer 2
  fgets(data, 300, fp);
  printf("%s", data);//Answer 3
  fgets(data, 300, fp);
  printf("%s", data);//Answer 4
  fgets(data, 300, fp);
  printf("Answer key: %s", data);//Shows answer.
  sscanf(data,"%d", &ans);//Reads formatted input from a string.
  scanf("%d", &answer);//Reads user input.
  
  if(ans == answer){//Compares input to answer.
    printf("Great!\n");
  }else
    printf("You suck!\n");
  return 0;
}