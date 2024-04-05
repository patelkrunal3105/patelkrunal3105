#22.Write a Python program to get a string made of the first 2 and
# the last 2 chars from a given a string. If the string length is 
# less than 2, return instead of the empty string.

user_string = "krunal"

count = 0

for i in user_string:
    count = count + 1
new_string = user_string [0:2]

print ("user string = " + user_string)
print("new string + " + new_string)