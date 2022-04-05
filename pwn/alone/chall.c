#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>

int shell() {
    printf("Yeah mate! You win!\nOpening your shell...\n");
    setreuid(geteuid(), geteuid());
    system("/bin/bash");
    printf("Shell closed! Bye.\n");
    exit(0);
}

void Hey(){
    printf("Hola StackSmasher : ");
	char buf[30];
    gets(buf);
	return ;
}


int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
	
    Hey();
    return 0;
}

