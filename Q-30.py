#30.Write a Python program to convert a list of tuples into a dictionary.

l = [("x",1),("x",34),("y",12),("y",3),("x",54)]

d = {}

for a , b in l:

    d.setdefault(a,[]).append(b)

print(d)