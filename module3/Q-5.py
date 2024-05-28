#.5 How will you compare two lists?

num1 = [10,20,30,35,40]

num2 = [20,35,40]


s = set(num2)
num3 = [x for x in num1 if x not in s]
print(num3)