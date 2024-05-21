#33. Write a Python script to concatenate following dictionaries 
# to create a new one.

num1 = {1: 10, 2: 20}
num2 = {3: 30, 4: 40}
num3 = {5: 50, 6: 60}

num4 ={}

for d in (num1,num2,num3):
    num4.update(d)

print(num4)    
