#10.Write a Python program to count the frequency of words in a file.

from collections import Counter 
def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())

print("Number of Words in the fil :",word_count("abc.txt"))