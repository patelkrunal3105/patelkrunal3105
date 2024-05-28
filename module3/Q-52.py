#52. How will you randomizes the items of a list in place?

import random

list1 = [1,2,3,4,5]
print("The original list is : "+ str (list1))

random.shuffle(list1)

print("The shuffled list is : "+str(list1))
