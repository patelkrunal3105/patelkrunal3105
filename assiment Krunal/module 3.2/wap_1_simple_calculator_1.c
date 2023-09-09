//1. WAP to make simple calculator (operation include Addition, Subtraction,Multiplication, Division, modulo)
#include <stdio.h>

int main()
{
    int a, b;
    char oprt;
    float result;

    printf("Choose the operator (+,-,*,/) for calculator: \n");
    scanf("%c", &oprt);
    printf("enter the first Value: \n");
    scanf("%d", &a);
    printf("enter the Secound Value: \n");
    scanf("%d", &b);

    if (oprt == '+')
    {
        result = a + b;
        printf("addition of %d + %d = %.2f\n", a, b, result);
    }
    else if (oprt == '-')
    {
        result = a - b;
        printf("subtraction of %d - %d = %.2f\n", a, b, result);
    }
    else if (oprt == '*')
    {
        result = a * b;
        printf("multiplication of %d * %d = %f\n", a, b, result);
    }
    else if (oprt == '/')
    {
        if (b == 0)
        {
            printf("\n division cannot be zero please enter another value");
            scanf("%d", b);
        }

        result = a / b;
        printf("division of %d / %d = %.2f\n", a, b, result);
    }
    else
    {
        printf("\n you input wrong value");
    }
    return 0;
}