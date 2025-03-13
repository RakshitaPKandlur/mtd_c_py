#include<stdio.h>
#include<math.h>
int main() {
int n1 = 89;
int n2 = 067;
int n3 = 0x99;

printf("%d %i %o %x \n", n1, n1, n1, n1); // 89 89 131 59
printf("%d %i %o %x \n", n2, n2, n2, n2); // 55 55 67 37
printf("%d %i %o %x \n", n3, n3, n3, n3); // 153 153 231 99 

}