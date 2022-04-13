#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <signal.h>
#include <errno.h>
#include <string.h>
void to_kill (){
    long pid;
    int status;
    char *end;
    char buf[10];
    
    printf("Current Process ID# %d \n", getpid());
    printf("Enter Process ID to Kill -> ");

    fgets(buf, sizeof buf, stdin);
    buf[strcspn(buf, "\n")] = '\0';
    pid = strtol(buf, &end, 10);

    if (pid > 0 ) {
        status = kill(pid, SIGKILL);
        if (status != 0) {
            if (errno == 1){
                printf("\n### Not super-user ###\n\n");
                to_kill();
            }
            else if (errno == 3)
            {
                printf("\n### No such process ###\n\n");
                to_kill();
            }
        }   
    }
    else{
        printf("Please Enter a Valid Process ID. \n");
        to_kill();
    }
}

int main () {
    to_kill();

}