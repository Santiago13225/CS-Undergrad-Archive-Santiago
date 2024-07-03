#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

void main(void)
{
        //Program #1

        /*
        pid_t pid;

        pid = fork();
        if(pid == 0){//Return value is 0 for child process.
                printf("Parent process id of current child process: %d\n", getppid());
                sleep(5);
        }else{
                printf("Child process id of current parent: %d\n", pid);
        }
        */

        //Program #2

        /*
        pid_t pid;
        int status;
        pid = fork();
        if (pid == 0){//Return value is 0 for child process.
                printf("Child process ID is: %d \n", getpid());
                execl("/bin/pwd", "pwd", NULL);
        }
        */

        //Program #3

        /*
        pid_t pid;
        int status;
        pid = fork();
        if (pid == 0){//Return value is 0 for child process.
                printf("Child process ID is: %d \n", getpid());
                execl("/bin/cal", "cal", NULL);
        }
        */

        //Program #4

        /*
        pid_t pid;

        pid = fork();
        if (pid == 0){//Return value is 0 for child process.
                printf("Child process ID is: %d \n", getpid());
                sleep(5);
                _exit(0);
        }else{
                int status;
                wait(&status);
                if(WIFEXITED(status))
                        printf("Child exited normally %d \n", WEXITSTATUS(status));
                else if(WIFSIGNALED(status))
                        printf("Child exited by a signal #%d \n", WTERMSIG(status));
        }
        */

}
