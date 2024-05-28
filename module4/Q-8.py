#8. Write a python program to find the longest words.

# L = ["one","two","three","pansuriya"]

# file1 = open('test.text','w')
# file1.writelines(L)
# file1.close()

def longestlength(L):
    max1 = len(L[0])
    temp = L[0]


    for i in L:
        if(len(i)>max1):
            max1 = len(i)
            temp = i
    print("The Longest length is :",temp,"and length is ",max1)   


a = ["one","two","Three","four","Fifth"] 

longestlength(a)



