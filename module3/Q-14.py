# 14.Write a Python program to find the second smallest 
# number in a list.



def find_len(num1):
    

    length = len(num1)
    num1.sort()
    print("Largest number is :",num1[length-1])
    print("Smallest number is :",num1[0])
    print("Second Largest number is :",num1[length-2])

num1 = [10,20,30,33,45,1,4,5]
Largest = find_len(num1)    