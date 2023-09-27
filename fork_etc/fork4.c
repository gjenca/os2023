#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>


int main() {

	int i;
	int status;
	FILE *fp;
	
	fp=fopen("out.txt","w");
	if (fork()) {
		fprintf(fp,"PARENT\n");
	}
	else {
		fprintf(fp,"CHILD\n");
	}	

}
