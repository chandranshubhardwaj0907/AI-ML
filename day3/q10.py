# Given a list, print all elements that appear more than once in the list.

numbers = [1, 2, 3, 4, 2, 5, 1, 6, 3]
duplicates = set()
seen = set()
for number in numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)
        
print("Elements that appear more than once:", duplicates)