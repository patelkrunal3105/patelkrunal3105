// 2.WAP to swap two numbers without using third variable
#include<stdio.h>

int main(){
int a = 20, b=30;
printf(" Befor swap \n a = %d , \n b = %d", a,b);
a = a + b;
b = a - b;
a = a - b;

printf("\n after swap \n a = %d ,\n b = %d", a,b);



    return 0;
}