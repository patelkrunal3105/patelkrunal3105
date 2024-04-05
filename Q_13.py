#13.Write a Python program to count the number of characters
#  (character frequency) in a string.

test_str = "Krunalpatel"

all_freq ={}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print("count of all characters in rahulpansuriya is :\n" + str(all_freq))       