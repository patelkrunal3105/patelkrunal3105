# Write a Python script to check if a given key already 
# exists in a dictionary.
import operator


d = {'A':1 ,'B':2 ,'C':3}

key = raw_input("Enter key to check :")

if key in d.keys():
    print("key is present and Value of the key is :")
    print(d[key])

else:
    print("key not presrnt!")
