#16. Can one block of except statements handle multiple exception?

try:
    x =int(input("enter First number:"))
    y =int(input("enter second number:"))
    
    print("The result:",x/y)
except (ZeroDivisionError,ValueError) as msg:
        print("The Raised Exception :",msg.___class__.__Name__)
        print("Description of Exception",msg)
        print("Plz provide velid input only... ")
        


