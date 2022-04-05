#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFFERSIZE 15

int check_pass(char* input){
    if (input[0] == 'A')
    if (input[1] == '5')
    if (input[2] == 'd')
    if (input[3] == 'S')
    if (input[4] == '-')
    if (input[5] == 'C')
    if (input[6] == '2')
    if (input[7] == '2')
    if (input[8] == '1')
    if (input[9] == '-')
    if (input[10] == 'a')
    if (input[11] == 'v')
    if (input[12] == '4')
    if (input[13] == 'x')
        return 0;

    return 1;
}

int main(){
    char input[BUFFERSIZE];

    printf("Give the key : ");
    fgets(input, BUFFERSIZE, stdin);

    if (check_pass(input) == 0) 
        printf("You got the key !\nThe flag to submit is shellmates{key}", input);
    else 
        printf("no way ! you can't crack it !");
}