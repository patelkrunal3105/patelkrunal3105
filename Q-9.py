# 9. Write a Python function that takes two lists and returns true 
# if they have at least one common number.


num1 = [1, 2, 3, 44, 45]
num2 = [2, 4, 1, 33]


num = any(check in num1 for check in num2)

if num:
    print("true")
else: 
    print("false")   