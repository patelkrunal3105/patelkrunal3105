#15. When will the else part of try-except-else be executed?

def divide (x, y):
    try:

         result = x//y
         
    except ZeroDivisionError:
        print ("sorry ! your are dividing by zero")

    else:
        print(" yes ! your Answer is :",result)  

divide (3, 2)             
divide (3, 0)