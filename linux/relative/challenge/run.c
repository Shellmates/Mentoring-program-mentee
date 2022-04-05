#define _GNU_SOURCE

#include <unistd.h>
#include <string.h>
#include <stdio.h>

int main(int arc, char** arv) {
    char *argv[] = { "/bin/bash", "-p", "/home/ctf/guess", arv[1], NULL };
    char *path;
    asprintf(&path, "%s%s", "PATH=", arv[2]);
    
    char *envp[] 
=    {
        path,
        0
    };
    execve(argv[0], argv, envp);
    return 0;
}
