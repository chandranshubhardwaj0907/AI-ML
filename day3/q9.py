# Write a program to check whether two lists share no common elements.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
common_elements = False
for item in list1:
    if item in list2:
        common_elements = True
        break
if not common_elements:
    print("The lists share no common elements.")
else:
    print("The lists share at least one common element.")
    
    #  using set 
set1 = set(list1)
set2 = set(list2)
if set1.isdisjoint(set2): # remember isdisjoint method
         print("The lists share no common elements.")
else:
    print("The lists share at least one common element.")