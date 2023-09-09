// wap to print fibonacci series up to given number.
#include <stdio.h>
int main()

{
    int a = 0, b = 1;

    printf("%d, %d \n", a, b);
    int fibonacci;

    for (int i = 0; i < 10; i++)
    {
        fibonacci= a + b;
        a = b;
        b = fibonacci;

        printf("%d \t", fibonacci);
    }

    return 0;
}