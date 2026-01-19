# Given a tuple of integers, create:
 
# A tuple of all even numbers

# A tuple of all odd numbers


tuple = (1,2,3,4,5,6,7,8,9,10)

evennumbertuple = ()
oddnumbertuple = ()


for i in tuple:
    if i%2 == 0:
        evennumbertuple += (i,) # for creating tuple with single element
    else:
        oddnumbertuple += (i,)

print("Tuple of even numbers:", evennumbertuple)
print("Tuple of odd numbers:", oddnumbertuple)