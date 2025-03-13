#include<stdio.h>

int main() {
    int averageScore = 0;
    puts("Enter average score of the student to print the result");
    scanf("%d", &averageScore);
    if(averageScore >= 0 && averageScore <= 49)
        puts("Result is Fail");
    else if(averageScore <= 70)
        puts("Result is Second Class");    
    else if(averageScore <= 90)
        puts("Result is First Class");
    else if(averageScore <= 100)
        puts("Result is Distinction");
    else 
        puts("Invalid Score Entered");
    return 0;
}
