#29. Write a Python program to unzip a list of tuples into individual lists.

l =[(1,2),(4,5),(8,5)]

result = list(zip(*l))

print(result)