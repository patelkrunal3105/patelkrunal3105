# 8. Write a Python program to check a list is empty or not.


def detail(liss):
    if not liss:
        return 1
    else:
        return 0


liss = ["rahu"]

if detail(liss):
    print("the list is empty")

else:
    print("the list is not empty")    