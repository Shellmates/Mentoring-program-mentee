#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stdio.h>
     
int main()
{
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);

  int check = 0x10101010;
  char buf[40];
  
  fgets(buf,45,stdin);
     
   printf("\n[buf]: %s\n", buf);
   printf("[check] %p\n", check);
     
   if ((check != 0x10101010) && (check != 0xdeadbeef))
     printf ("\nYou are on the right way!\n");
     
   else if (check == 0xdeadbeef)
    {
      printf("Yeah dude! You win!\nOpening your shell...\n");
      setreuid(geteuid(), geteuid());
      system("/bin/bash");
      printf("Shell closed! Bye.\n");
    }
    return 0;
}
