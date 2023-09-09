#include <stdio.h>
int main()
{
    int a, i, sum=0;
    printf("Please enter the 10 number\n");
    for (int i = 1; i <= 10; i++)
    {
        printf("number %d =", i);
        scanf("%d", &a);
        if (a < 0)
        {
            continue;
        }
         sum = sum + i;
    }
   

   printf("\n the sum of number from 1 to %d = %d",a,sum);
   
}
