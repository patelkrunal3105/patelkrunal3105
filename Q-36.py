#36. How Do You Check The Presence Of A Key In A Dictionary?

Students = {"Rahul":"Rah", " Krunal":"Krun","Ramesh":"Ram","Hardik":"Har"}

name = input("Enter a name here : ")

if name in Students.keys():
    print("it is present")

else:
    print("not present here")    