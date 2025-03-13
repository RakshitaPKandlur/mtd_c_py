#include<stdio.h>
#include<math.h>

int main()
{
    int inputNumber = 0;
    int sum = 0;
    int remainderDigit = 0;
    puts("Enter a number to find the second smallest digit in given number:");
    scanf("%d",&inputNumber);
    while(inputNumber > 0)
    {
        remainderDigit = inputNumber % 10;
        sum = sum + remainderDigit;
        inputNumber = inputNumber / 10;
        // Not yet completed 
        //COMPLETE IT
    }

}