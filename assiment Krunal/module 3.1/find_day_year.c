#include <stdio.h>

int main()
{

    float y,d;

    printf("\n Nos off the day:");
    scanf("%f", &d);

    printf("\n Nos of the year :");
    scanf("%f", &y);

    float year = (d / 365);
    float day = (y * 365);

    printf(" \n Day convert to Years : %.2f", year);
    printf(" \n Year convert to Days: %.2f", day);
   
    return 0;
}