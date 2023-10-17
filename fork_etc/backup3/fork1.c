#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>




int main() {

	int status;

	printf("bumbac bezim\n");
	if ( fork()==0) {
		printf("CHILD\n");
		execl("/bin/ls","ls","/tmpp",NULL);
	} else {
		printf("PARENT\n");
		wait(&status);
		printf("CHILD dobehol status = %d\n",status);

	}
	printf("kapybara\n");
}
