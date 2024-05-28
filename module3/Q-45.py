#45.Write a Python program to find the highest 3 values in a dictionary

from collections import Counter

my_dict = {'t': 3, 'u': 4,'t': 6, 'o':5, 'r':21}

k = Counter (my_dict)

print(my_dict, "\n")

high = k.most_common(3)
print("Dictionary With 3 highest values :")
print("Keys: Values")

for i in high:
    print(i[0]," :",i[1]," ")