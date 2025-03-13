
#include<stdio.h>
#include<math.h>

int main() {
    int inutNum = 0;
    puts("Enter a number to check if it is Perfect Square");
    scanf("%d", &inutNum);
    int root = floor(sqrt(inutNum));
    if( root * root == inutNum)
        printf("%d is an Perfect Square", inutNum);
    else
        printf("%d is not a Perfect Square", inutNum);
    return 0;
}
