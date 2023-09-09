//WAP to show
// 1. Monday to Sunday using switch case
#include <stdio.h>
int main()

{
    int day ;

    printf("Enter the Day in a Week:");
    scanf("%d", &day);

    switch (day)
    {
    case 1:
        printf("today is monday");
        break;
    case 2:
        printf("today is Tuesday");
        break;
    case 3:
        printf("today is Wednesday");
        break;
    case 4:
        printf("today is Thursday");
        break;
    case 5:
        printf("today is Friday");
        break;
    case 6:
        printf("today is Saturday");
        break;
    default:
        printf("today is Sunday");
        break;
    }
}
