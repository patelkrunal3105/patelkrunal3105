#25.Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?


class Refrigerator :
   
   price = ""
   company = ""
   Colour = ""


   def __init__(self,price,company,Colour):
    print("Refrigeratore init")
    self.price=price
    self.company=company
    self.Colour=Colour


   def display(self):
        print(f"{self.price},{self.company},{self.Colour}") 

class Air_conditioer(Refrigerator) : 


    capacity = 2

    def __init__(self):
        print("Air_conditioer init")

    def show (self):
        print(f"{self.price},{self.company},{self.Colour},{self.capacity}")     



s = Refrigerator(1000,"LG","Black") 
s.display()  

# s1= Refrigerator(2000,"MI","Red")
# s1.display()

p =Air_conditioer()
p.show()