#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>




int main() {

	int status;

	printf("bumbac bezim\n");
	if ( fork()==0) {
		printf("CHILD\n");
		exit(7);
	} else {
		printf("PARENT\n");
		wait(&status);
		printf("CHILD dobehol status = %d\n",WEXITSTATUS(status));

	}
	printf("kapybara\n");
}
