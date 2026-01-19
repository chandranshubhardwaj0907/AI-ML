# Given a list of integers compute the average of all numbers in the list.

numbers = [10, 20, 30, 40, 50]


sum = 0
for i in numbers:
    sum = sum+i
    average = sum/len(numbers)
    
print("The average is:", average)    