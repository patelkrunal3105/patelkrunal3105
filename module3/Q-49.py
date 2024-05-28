#49.Write a Python function to check whether a number is in a given range

def test_range(n):

    if n in range(3,9):
        print("%s is in the range"% str(n))

    else:

        print("the numberis outside the given range.")   

test_range(5)          