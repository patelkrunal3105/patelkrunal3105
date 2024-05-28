 # 28.Write a Python program to remove an empty tuple(s) 
 # from a list of tuples.

L = [(),(),('1','2'),('a','b'),()]

L =[t for t in L if t]

print(L)


