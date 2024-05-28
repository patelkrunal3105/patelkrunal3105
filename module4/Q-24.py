#24. Write a Python class named Circle constructed by a radius and two 
# methods which will compute the area and the perimeter of a circle


class Circle():
    def __init__(Self , r):
        Self.radius = r

    def area(Self):
        return Self.radius**2*3.14    

    def perimeter(Self):
        return 2*Self.radius*3.14

NewCircle = Circle(6)  
print(NewCircle.area())
print(NewCircle.perimeter())             