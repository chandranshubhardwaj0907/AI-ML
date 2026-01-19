tup = (3, 4, 5, 6)
# """
# This script demonstrates basic operations on a tuple in Python.
# The script performs the following tasks:
# 1. Initializes a tuple `tup` with integer elements.
# 2. Iterates through the tuple to calculate the sum of its elements and prints the result.
# 3. Uses the `index()` method to find the position of a specific element in the tuple.
# 4. Uses the `count()` method to count the occurrences of a specific element in the tuple.
# Key Functions:
# - `tup.index(4)`: Finds the index of the first occurrence of the value `4` in the tuple.
# - `tup.count(5)`: Counts how many times the value `5` appears in the tuple.
# """

sum = 0
for i  in tup:
    sum += i
    
    
print(sum) 


print(tup.index(4))


print(tup.count(5))