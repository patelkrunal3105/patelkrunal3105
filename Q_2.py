# Write a Python program to get the Factorial number of given 
# number.

def Factorial(n):

    return 1 if (n==1 or n==0) else n * Factorial(n-1)

num =5
print("Factorial of",num,"is",Factorial(num))