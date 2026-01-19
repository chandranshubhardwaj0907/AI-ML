#  unique elements in a collection is called set

my_set = {1, 2, 3, 4, 5, 5, 6, 6}
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Adding an element to the set
my_set.add(7)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

# empty_set = set()  method to create empty set
empty_set = set()
print(type(empty_set))  # Output: <class 'set'> 

#  methods

my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6, 7}
my_set.discard(10)  # Does not raise an error if element not found
print(my_set)  # Output: {1, 2, 4, 5, 6, 7}

my_set.pop()  # Removes and returns an random element
print(my_set)