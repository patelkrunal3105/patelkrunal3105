// Looping programs:
// Sum of even numbers
#include <stdio.h>
int main()
{
  int i, number, sum = 0;
  printf("please enter max value :");
  scanf("%d", &number);

  printf("\n Even numbers between 1 and  %d are : \n", number);
  for (i = 2; i <= number; i += 2)
  {
    if (i % 2 == 0)
    {
      printf("%d \n", i);
      sum = sum + i;
    }
  }
  printf("\n the sum of odd number from 1 to %d = %d", number, sum);

  return 0;

}