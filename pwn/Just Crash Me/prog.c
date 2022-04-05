#include <stdio.h>
#include <signal.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

#define BANNER "__        __   _                          \n\\ \\      / /__| | ___ ___  _ __ ___   ___ \n \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\\n  \\ V  V /  __/ | (_| (_) | | | | | |  __/\n   \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|\n                                          \n"

#define PROMPT "Your goal is to cause a \e[01;91msegmentation fault\e[0m while the program is running on the remote server\nEnter your \e[0;92mname\e[0m >"

void print_flag()
{
	char flag[40];
	int fd = open("flag.txt", O_RDONLY, 0);
	for (int i = 0; i < sizeof(flag) && read(fd, flag+i, 1); i++);
	printf("The flag of this challenge is : \e[01;92m%s\e[0m\n", flag);
	exit(1);
}

int main()
{
	char name[100];
	setvbuf(stdout, NULL, _IONBF, 0);
	signal(SIGSEGV, print_flag);
	
	puts(BANNER);
	
	printf(PROMPT);
	gets(name);
	printf("Welcome \e[0;92m%s\e[0m\n", name);
}
