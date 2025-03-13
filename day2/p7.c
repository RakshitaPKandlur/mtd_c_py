#include <stdio.h>
int main() {
    int inputNumber,i = 0;
    puts("Enter a number to print it's Math table:");
    scanf("%d",&inputNumber);
    printf("Math table of %d:\n",inputNumber);
    for(i = 1; i <= 10; i++)
        {
            printf("%d * %02d = %03d\n", inputNumber, i, inputNumber*i);
        }
        return 0;
}