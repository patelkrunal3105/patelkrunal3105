#27.What is used to check whether an object o is an instance of class A?

class myobj:

    name = "rahul"

y = myobj()
x = isinstance(y, myobj)

print(x)