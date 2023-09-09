//WAP to show
// 2. Vowel or Consonant using switch case
#include <stdio.h>
int main()

{
    char alph;

    printf(" Enter the alphabet :");
    scanf("%c", &alph);

    switch (alph)
    {
    case 'a':
        printf("This is a Vowels letter ");
        break;

    case 'A':
        printf("This is a Vowels letter ");
        break;

    case 'e':
        printf("This is a Vowels letter ");
        break;

    case 'E':
         printf("This is a Vowels letter ");
        break;

    case 'i':
         printf("This is a Vowels letter ");
        break;

    case 'I':
        printf("This is a Vowels letter ");
        break;

    case 'o':
        printf("This is a Vowels letter ");
        break;

    case 'O':
         printf("This is a Vowels letter ");
        break;

    case 'u':
        printf("This is a Vowels letter ");
        break;

    case 'U':
         printf("This is a Vowels letter ");
        break;

    default:
        printf("This is a Consonant letter");
        break;

    }
}
