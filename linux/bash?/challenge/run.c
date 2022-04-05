#define _GNU_SOURCE

#include <unistd.h>
#include <string.h>
#include <stdio.h>

int main(int arc, char** arv) {
    char *argv[] = { "/info", NULL };
    char *path;
    char *home;
    asprintf(&path, "%s%s", "PATH=", arv[1]);
    asprintf(&home, "%s%s", "HOME=", arv[2]);
    
    char *envp[] =
    {
        home,
        path,
        0
    };
    execve(argv[0], argv, envp);
    return 0;
}
