#42. Write a Python program to print all unique values in a dictionary.


L = [{"V": "S001"},{"V":"S002"},{"V":"S001"},{"V":"S005"},{"V":"S004"}]

print("Original List :",L)

u_value = set(val for dic in L for val in dic.Values())

print("Unique Values:",u_value)