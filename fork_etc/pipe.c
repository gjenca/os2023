#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>


int main() {

	int fd[2];
	char buf[10];
	
	pipe(fd);
	if (!fork()) {
		sleep(1); 
		write(fd[1],"bum",4);
	} else {
		read(fd[0],buf,4);
		printf("%s\n",buf);
	}
}
