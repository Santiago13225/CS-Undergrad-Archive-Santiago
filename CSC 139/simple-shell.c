#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <sys/types.h>

#define MAX_LINE 80 // 80 chars per line, per command
#define DELIMITERS " \t\n\v\f\r" //String used to split input into tokens.

void init_args(char *args[]) { //Initializes an array of args to be all NULL.
    for(size_t i = 0; i != MAX_LINE / 2 + 1; ++i) { //Each argument can have at most MAX_LINE/2 characters.
        args[i] = NULL; //Sets arg at position i to be NULL.
    }
}

void init_command(char *command) { //Initializes a string, command, to be an empty string.
    strcpy(command, ""); //Copies an empty string "" into the character array command. 
}

void refresh_args(char *args[]) { //This function frees the memory allocated for each string in the args array.
    while(*args) { //While loop used to refresh content of args.
        free(*args); //Used to avoid memory leaks.
        *args++ = NULL; //Sets each string to NULL.
    }
}

size_t parse_input(char *args[], char *original_command) { //Parses input into an array of strings/args and returns the number of arguments parsed.
    size_t num = 0; //Sets count to 0.
    char command[MAX_LINE + 1]; //Used to create a space to store into.
    strcpy(command, original_command); //Creates a copy since `strtok` will modify it.
    char *token = strtok(command, DELIMITERS); //Strtok splits command into tokens with DELIMITERS as the delimiter.
    while(token != NULL) { //While the token is not null.
        args[num] = malloc(strlen(token) + 1); //Allocates a block of memory that is big enough to hold the string token, including the null terminator character.
        //^Assigns the memory address of the allocated block to the num-th element of the args array.
        strcpy(args[num], token); //Copies the contents of the token string to the args[num] string.
        ++num; //Increases count.
        token = strtok(NULL, DELIMITERS); //Extracts the next token from the string based on the delimiters specified and assigns it to the token variable. 
    }
    return num; //Returns the count.
}

int get_input(char *command) { //Gets command from input of history.
    char input_buffer[MAX_LINE + 1]; //Creates a character array of size MAX_LINE + 1. 
    if(fgets(input_buffer, MAX_LINE + 1, stdin) == NULL) { //Checks if there was an error or end-of-file condition. 
        fprintf(stderr, "Failed to read input!\n"); //Prints error.
        return 0;
    }
    if(strncmp(input_buffer, "!!", 2) == 0) { //If the input is '!!'.
        if(strlen(command) == 0) { //If there is no history yet.
            fprintf(stderr, "No history available yet!\n"); //Print the error.
            return 0;
        }
        printf("%s", command); //Keep the command unchanged and print it.
        return 1;
    }
    strcpy(command, input_buffer); //Update the command.
    return 1;
}

int check_ampersand(char **args, size_t *size) { //Checks for ampersand at the end of arguments.
    size_t len = strlen(args[*size - 1]); //Calculates length of a string.
    if(args[*size - 1][len - 1] != '&') { //If ampersand is at end of argument. 
        return 0;
    }
    if(len == 1) { //Remove this argument if it only contains '&'.
        free(args[*size - 1]); //Frees the memory allocated to the last argument in the args array.
        args[*size - 1] = NULL; //Sets the last element of the args array to NULL.
        --(*size); //Reduce its size.
    } else {
        args[*size - 1][len - 1] = '\0'; //Sets the last character of the last argument to null.
    }
    return 1;
}

unsigned check_redirection(char **args, size_t *size, char **input_file, char **output_file) { //Checks the redirection tokens in arguments and remove such tokens.
    unsigned flag = 0;
    size_t to_remove[4], remove_cnt = 0; //Declares an array of 4 elements of type size_t named to_remove.
    //^Initializes a variable of type size_t named remove_cnt to 0.
    for(size_t i = 0; i != *size; ++i) { //Iterates over the args array, which contains *size elements.
        if(remove_cnt >= 4) { //Checks if there are four or more arguments that need to be removed from the args array.
            break;
        }
        if(strcmp("<", args[i]) == 0) { //Input.
            to_remove[remove_cnt++] = i; //Adds the index i to the to_remove array and then increments the remove_cnt variable.
            if(i == (*size) - 1) { //Checks if the current element i is the last element in the args array.
                fprintf(stderr, "No input file provided!\n"); //Prints error.
                break;
            }
            flag |= 1; //A bitwise OR operator sets the least significant bit of the flag variable to 1.
            *input_file = args[i + 1]; //Assigns the value of args[i + 1] to the variable pointed to by input_file.
            to_remove[remove_cnt++] = ++i; //Add an index i to the to_remove array and to update the count of elements in to_remove stored in remove_cnt.
        } else if(strcmp(">", args[i]) == 0) { //Output.
            to_remove[remove_cnt++] = i; //Adds the index i to the to_remove array and then increments the remove_cnt variable.
            if(i == (*size) - 1) { //Checks if the current element i is the last element in the args array.
                fprintf(stderr, "No output file provided!\n"); //Print error.
                break;
            }
            flag |= 2; //Another bitwise OR operation. 
            *output_file = args[i + 1]; //Makes output_file point to the string in args[i + 1].
            to_remove[remove_cnt++] = ++i; //Adds the current argument (args[i]) and the next argument (args[i+1]) to the list of arguments to be removed and updates the count of arguments to be removed.
        }
    }
    //Remove I/O indicators and filenames from arguments
    for(int i = remove_cnt - 1; i >= 0; --i) {//Iterates over the indices in the to_remove array that have been populated, starting from the last index and ending at the first index.
        size_t pos = to_remove[i]; //The index of arg to remove.
        // printf("%lu %s\n", pos, args[pos]);
        while(pos != *size) { //Loops through the args array from the pos index to the end of the array.
            args[pos] = args[pos + 1]; //Assigns the value of args[pos + 1] to args[pos].
            ++pos; //Increments pos.
        }
        --(*size); //Decrements the value of *size.
    }
    return flag; //Returns IO flag value.
}

int redirect_io(unsigned io_flag, char *input_file, char *output_file, int *input_desc, int *output_desc) { //Open files and redirect I/O.
    // printf("IO flag: %u\n", io_flag);
    if(io_flag & 2) { //Redirecting output.
        *output_desc = open(output_file, O_WRONLY | O_CREAT | O_TRUNC, 644); //Opens a file in write-only mode, creates the file if it does not exist, and truncates the file to length 0 if it already exists (O_TRUNC).
        if(*output_desc < 0) { //Checks whether the file descriptor returned by the open function is negative.
            fprintf(stderr, "Failed to open the output file: %s\n", output_file); //Prints error.
            return 0;
        }
        // printf("Output To: %s %d\n", output_file, *output_desc);
        dup2(*output_desc, STDOUT_FILENO); //Duplicate an existing file descriptor onto another file descriptor number.
    }
    if(io_flag & 1) { //Redirecting input.
        *input_desc = open(input_file, O_RDONLY, 0644); //Open the file specified by input_file in read-only mode.
        if(*input_desc < 0) { //Checks if negative.
            fprintf(stderr, "Failed to open the input file: %s\n", input_file); //Prints error.
            return 0;
        }
        // printf("Input from: %s %d\n", input_file, *input_desc);
        dup2(*input_desc, STDIN_FILENO); //Duplicate an existing file descriptor onto another file descriptor number.
    }
    return 1;
}

void close_file(unsigned io_flag, int input_desc, int output_desc) { //Closes files for input and output.
    if(io_flag & 2) { //Checks if the second bit of io_flag is set to 1 or not.
        close(output_desc); //Close the file descriptor associated with the output file. 
    }
    if(io_flag & 1) { //Checks if the first bit of io_flag is set to 1 or not.
        close(input_desc); //Close the file descriptor associated with the input file.
    }
}

void detect_pipe(char **args, size_t *args_num, char ***args2, size_t *args_num2) { //Detects the pipe '|' and split aruguments into two parts accordingly.
    for(size_t i = 0; i != *args_num; ++i) { //Iterates over the elements in the args array.
        if (strcmp(args[i], "|") == 0) { //If the current argument is a pipe symbol.
            free(args[i]); //Used to release the memory that was allocated for a string.
            args[i] = NULL; //Sets the i-th element of the args array to NULL. 
            *args_num2 = *args_num - i - 1; //Calculates the number of arguments in the second command after the pipe.
            *args_num = i; //This line sets the value pointed to by the pointer args_num to i.
            *args2 = args + i + 1; //Creates a pointer to a new array of command-line arguments.
            break;
        }
    }
}

int run_command(char **args, size_t args_num) { //Runs the command.
    int run_concurrently = check_ampersand(args, &args_num); //Detect '&' to determine whether to run concurrently.
    // Detect pipe.
    char **args2;//Declares a variable args2 that is a pointer to a pointer to char. 
    size_t args_num2 = 0;//Declares a variable args_num2 of type size_t and initializes it to 0.
    detect_pipe(args, &args_num, &args2, &args_num2);//Function call to detect_pipe method.
    //Create a child process and execute the command.
    pid_t pid = fork();
    if(pid < 0) { //Fork failed.
        fprintf(stderr, "Failed to fork!\n"); //Print error.
        return 0;
    } else if (pid == 0) { //Child process.
        if(args_num2 != 0) { //Pipe stuff.
            //Create pipe.
            int fd[2];//Declares an array named fd of type int with a size of 2. The array fd is being used to create a pipe for inter-process communication.
            pipe(fd);//Creates a pipe and assigns the file descriptors to the array fd.
            pid_t pid2 = fork(); //Fork into another two processes.
            if(pid2 > 0) { //Child process for the second command.
                //Redirect I/O.
                char *input_file, *output_file;//Create two pointers to char variables named input_file and output_file, respectively.
                int input_desc, output_desc;//Variables created to store file descriptors, which are integer values associated with open files in a computer program.
                unsigned io_flag = check_redirection(args2, &args_num2, &input_file, &output_file); //Bit 1 for output, bit 0 for input.
                io_flag &= 2; //Disable input redirection.
                if(redirect_io(io_flag, input_file, output_file, &input_desc, &output_desc) == 0) {//Checks whether the function redirect_io() returns a zero value.
                    return 0;
                }
                close(fd[1]);//Close the write end of a pipe.
                dup2(fd[0], STDIN_FILENO);//Duplicate the read end of a pipe and associate it with the standard input file descriptor (STDIN_FILENO), which has a value of 0.
                wait(NULL); //Waits for the first command to finish.
                execvp(args2[0], args2);//Executes the specified command with the provided argument list, replacing the current process with the command process.
                close_file(io_flag, input_desc, output_desc);//Used to close file descriptors associated with input and output files.
                close(fd[0]);//Close the read end of a pipe.
                fflush(stdin);//Used to flush (clear) the input buffer associated with the standard input stream (stdin).
            } else if(pid2 == 0) { //Grandchild process for the first command.
                //Redirect I/O.
                char *input_file, *output_file;//Create two pointers to char variables named input_file and output_file, respectively.
                int input_desc, output_desc;//Variables created to store file descriptors, which are integer values associated with open files in a computer program.
                unsigned io_flag = check_redirection(args, &args_num, &input_file, &output_file); //Bit 1 for output, bit 0 for input.
                io_flag &= 1; //Disable output redirection.
                if(redirect_io(io_flag, input_file, output_file, &input_desc, &output_desc) == 0) { //Checks whether the function redirect_io() returns a zero value.
                    return 0;
                }
                close(fd[0]);//Close the read end of a pipe.
                dup2(fd[1], STDOUT_FILENO);//Duplicate the file descriptor fd[1] (which represents the write end of a pipe) onto the file descriptor STDOUT_FILENO.
                execvp(args[0], args);//Used to execute a program specified by the args[0] argument, along with any additional arguments passed in the args array.
                close_file(io_flag, input_desc, output_desc);//Call to close_file function.
                close(fd[1]);//Close the write end of a pipe.
                fflush(stdin);//Used to flush (clear) the input buffer associated with the standard input stream (stdin).
            }
        } else { //No pipe.
            //Redirect I/O.
            char *input_file, *output_file;//Create two pointers to char variables named input_file and output_file, respectively.
            int input_desc, output_desc;////Variables created to store file descriptors, which are integer values associated with open files in a computer program.
            unsigned io_flag = check_redirection(args, &args_num, &input_file, &output_file); //Bit 1 for output, bit 0 for input.
            if(redirect_io(io_flag, input_file, output_file, &input_desc, &output_desc) == 0) { //Checks whether the function redirect_io() returns a zero value.
                return 0;
            }
            execvp(args[0], args);//Used to execute a program specified by the args[0] argument, along with any additional arguments passed in the args array.
            close_file(io_flag, input_desc, output_desc);//Call to close_file function.
            fflush(stdin);//Used to flush (clear) the input buffer associated with the standard input stream (stdin).
        }
    } else {//Parent process.
        if(!run_concurrently) {//Parent and child run concurrently.
            wait(NULL);//Wait for any child process to finish execution.
        }
    }
    return 1;
}

int main(void) {
    char *args[MAX_LINE / 2 + 1];//Command line (of 80) has max of 40 arguments.
    char command[MAX_LINE + 1];//Declares a character array named command with a size of MAX_LINE + 1. This array is typically used to store a command or input line entered by the user.
    init_args(args);//Call to init_args function.
    init_command(command);//Call to init_command function.
    while (1) {//Basically an infinite loop.
        printf("osh>");//Print the command prompt.
        fflush(stdout);//Used to flush the output buffer associated with the stdout stream.
        fflush(stdin);
        //Make args empty before parsing.
        refresh_args(args);//Call to refresh_args function.
        //Get input and parse it.
        if(!get_input(command)) {//Checking whether the get_input function call was successful.
            continue;
        }
        size_t args_num = parse_input(args, command);//Declare a variable args_num of type size_t and initialize it with the return value of the parse_input function.
        //Continue or exit.
        if(args_num == 0) {//Empty input.
            printf("Please enter the command! (or type \"exit\" to exit)\n");
            continue;
        }
        if(strcmp(args[0], "exit") == 0) {//Checks if the first argument in the args array is equal to the string "exit".
            break;
        }
        run_command(args, args_num);//Run command.
    }
    refresh_args(args);//Used to avoid memory leaks!
    return 0;
}