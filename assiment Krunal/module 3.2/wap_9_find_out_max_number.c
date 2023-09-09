//Write a program to find out the max from given number
#include <stdio.h>

int max (int mx,int mi){
    if (mx > mi){
        return mx;
    }else{
        return mi;
    }
   } 
   int main (){
   
   int a = 10, b =50, c = -70, d =20;
   int x = max(a ,b);
   int y = max(c ,d);
   int z = max (x , y);
   printf("Maximum number is : %d",z);

   return 0;

   }









