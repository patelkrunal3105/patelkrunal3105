#include <stdio.h>
int main()
{
    int startyear, endyear, i;

    printf("Enter the Year to start searching the leap years : ");

    scanf("%d", &startyear);

    printf("Enter the Year to end search of the leap years : ");

    scanf("%d", &endyear);

    printf("leap years between %d to %d\n ", startyear, endyear);

    for (i = startyear; i <= endyear; i++)

    {
        if (i % 400 == 0)
        {
            printf("%d is a leap year.\n",i);
        }
        else if (i % 100 == 0)
        {
            printf("%d is not a leap year.\n",i);
        }
        else if (i % 4 == 0)
        {
            printf("%d is a leap year.\n",i);
        }
        else
        {
            printf("%d is not a leap year.\n",i);
        }
    }

    return 0;
}