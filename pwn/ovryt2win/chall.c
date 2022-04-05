
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
     
void shell() {
    setreuid(geteuid(), geteuid());
    system("/bin/bash");
    exit(0);
}
     
void mate() {
    printf("Hey Mate ! How u Doin ?!\n");
    exit(0);
}
     
int main()
{
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    int var;
    void (*func)()=mate;
    char buf[128];
    printf("> ");
    fgets(buf,133,stdin);
    printf("Func adress  : %x\n",func );
    func();
    return 0;
}

