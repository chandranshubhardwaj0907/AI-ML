# lists

marks = [90, 85, 78, 92, 88]

# Accessing elements
print("First mark:", marks[0])  # Output: 90
print("Last mark:", marks[-1])  # Output: 88

print(len(marks))  # Output: 5

#  strings are immutable but lists are mutable

marks[2] = 80
print("Updated marks:", marks)  # Output: [90, 85, 80, 92, 88]



print(type(marks))  # Output: <class 'list'>
# Adding elements
marks.append(95)
print("After appending:", marks)  # Output: [90, 85, 80, 92, 88, 95]

marks[:]

marks[0:3]
print("Sliced marks:", marks[0:3])  # Output: [90, 85, 80]


#  methods

marks.sort()
print("Sorted marks:", marks)  # Output: [80, 85, 88, 90, 92, 95]

marks.insert(2, 87) # Insert 87 at index 2
print("After insertion:", marks)  # Output: [80, 85, 87, 88, 90, 92, 95]

marks.reverse()
print("Reversed marks:", marks)  # Output: [95, 92, 90, 88, 87, 85, 80]
marks.remove(88)
print("After removing 88:", marks)  # Output: [95, 92,


#  loops in list

for mark in marks:
    print("Mark:", mark)
    print("-----")
    marks2 = [78, 85, 91, 90, 88]
    x = 90
    idx = 0
    
for mark in marks2:
    if (mark == x):
        print(f"Found {x} at index {idx}")
        break
    idx += 1