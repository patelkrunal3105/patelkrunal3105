#3.Differentiate between append () and extend () methods?

# Append()                                                                  

# To add a single entry to the           
# end of a list, use the append() 
# function.


# accepts only one input element.


# The append() function adds the full 
# input to the list as a single item.

# Since append() only executes one operation,
# it is typically quicker and more effective than extend().

# Append has constant time complexity i.e.,O(1)



# Extend()

# To add additional elements or an iterable to the end of a list,
# use the extend() function.

# accepts as input an iterable (such as a list or tuple).

# extend() adds each item to the list independently after 
# iterating through each one in the input.

# When adding elements from numerous iterables or with huge inputs, 
# extend() could take longer.

# Extend has a time complexity of O(k). Where k is the length of the 
# list which need to be added.