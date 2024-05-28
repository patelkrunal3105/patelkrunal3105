#3. Write a Python program to append text to a file and display the text.

def file_read(fname):
    from itertools import islice
    with open(fname,"w") as myfile:
        myfile.write("python Exercises\n")
        myfile.write("Java Exercises")
    txt = open(fname) 
    print(txt.read())   
file_read('abc.txt')    