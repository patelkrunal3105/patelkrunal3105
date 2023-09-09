// Looping programs:
// Sum of odd numbers WAP to print table up to given numbers

#include<stdio.h>
int main()


{
int i, number, sum=0;
printf("please enter max value :");
scanf("%d",&number);

printf("\n odd numbers between 0 and  %d are : \n",number);
for (i = 1; i <= number; i++)
{
    if (i%2 !=0)
    {
        printf("%d \n",i);
        sum = sum + i;
    }
}
   printf("\n the sum of odd number from 1 to %d = %d",number,sum);
   
   return 0;

}