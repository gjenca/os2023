#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int main() {


	int pipefd_A[2];
	int pipefd_B[2];
	static char buf[100];

	pipe(pipefd_A);
	pipe(pipefd_B);
	if ( fork()==0) {
		// Zavriem nepotrebne konce rur
		close(pipefd_A[1]);
		close(pipefd_B[0]);
		dup2(pipefd_A[0],0);
		dup2(pipefd_B[1],1);
		execl("/bin/bc","bc",NULL);
	} else {
		close(pipefd_A[0]);
		close(pipefd_B[1]);
		write(pipefd_A[1],"7*8\n",4);
		read(pipefd_B[0],buf,3);
		printf("%s",buf);
	}
}
