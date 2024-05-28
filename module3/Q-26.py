 # 26. Write a Python program to replace last value of tuples in a list.

 
num = [(10,20,30),(40,50,60),(70,80,90)]

print([t[:-1]+(99,) for t in num ])