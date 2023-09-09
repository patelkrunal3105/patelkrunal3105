#include <stdio.h>

main()
{

    int principal = 10000;
    int rate = 10;
    int time = 3;

    int intrest = (principal * rate * time) / 100;

    printf(" rate of intrest= %d", intrest);
    return 0;
}
