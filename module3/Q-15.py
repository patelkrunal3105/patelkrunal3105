# 15. Write a Python program to get unique values from a list

def unique(num1):

    list_set = set(num1)

    unique_list = (list(list_set))

    for x in unique_list:
        print(x)

num1 = [10,20,30,45,55,30,45] 
print ("the unique values is :")
unique(num1)
