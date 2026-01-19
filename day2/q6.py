# Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        
        
# Write a program to print all numbers from 1 to 100 that are divisible by both 3 or 5.
print("Numbers divisible by 3 or 5:")
for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        