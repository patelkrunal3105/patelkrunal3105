#23.Write a Python class named Rectangle constructed by a length and width and a method which will 
# compute the area of a rectangle

class Rectangle():
    def __init__(Self, l ,w):
        Self.length = l
        Self.width = w


    def rectangle_area(Self):
        return Self.length*Self.width    


newRectangle = Rectangle(12 , 10)   
print(newRectangle.rectangle_area())     