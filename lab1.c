#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

void grandChild_process(){
    sleep(5);
    printf("GrandChild Process is with process ID %d\n", getpid());
    exit(0);
}

void child_process() {
    int status;
    int pid;

    pid = fork();
    if (pid == 0){
        grandChild_process();
    }
    waitpid(pid, &status, 0); 
    sleep(5); 
    printf("Child Process is with process ID %d\n", getpid());
    exit(0);
}

int main (int argc, const char * argv[]) {
    int status;
    int pid;

    pid = fork();
    if (pid == 0) {
        child_process();
    };
    waitpid(pid, &status, 0);
    sleep(5);
    printf("Parent Process with process ID %d\n", getpid());
   

}