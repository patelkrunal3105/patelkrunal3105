#10 Write a Python program that will return true if the two given integer
#values are equal or their sum or difference is 5.

def test_number(x ,y):
    if x == y or abs (x - y) == 5 or (x + y) == 5:
        return True
    else:
        return False


print (test_number(2 , 10)) 
print (test_number(2 , 3))
print (test_number(2 , 2))
print (test_number(8 , 1))
print (test_number(20 , 10))
       