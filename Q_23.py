#23.Write a Python function to insert a string in 
# the middle of a string.

def insert_string(str,word):

    return str[:2] + word + str[2:]


print (insert_string('[[]]','Nirav'))    
print (insert_string('{{}}','Babu'))
print (insert_string('<<>>','Kalpesh'))