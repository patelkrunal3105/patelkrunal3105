#7. Write a Python program to read a file line by line store it into a variable

f = open ("myfile.text","r")

str = " "

for i in range (0,15):
    str = str + f.read(i)

print(str)    