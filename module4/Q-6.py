#6. Write a Python program to read a file line by line and store it into a list

L = ["honda\n","for\n","honda\n"]

file1 = open('myfile.text','w')
file1.writelines(L)
file1.close()

file1 = open('myfile.text','r')
Lines = file1.readlines()

count = 0


for line in Lines:
    count += 1
    print("Lines{}: {}".format(count,line.strip()))