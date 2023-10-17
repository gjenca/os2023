#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int main() {

	int i;
	int status;
	pid_t pid;

	for (i=0;i<3;i++) {
		pid=fork();
		if (pid == 0) {
			printf("Child:%d\n",i);
		}
		else if (pid > 0 ) {
			wait(&status);
			printf("Child ended %d\n",i);
		}
		else {
			printf("Chyba fork()\n");
		}
	}
	//exit(0);
}
