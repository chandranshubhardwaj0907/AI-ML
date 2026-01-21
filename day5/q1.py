with open("day5/names.txt" , "w") as f:
    f.write("Alice\n")
    f.write("Bob\n")
    f.write("Charlie\n")
    f.write("David\n")
    f.write("Eve\n")
    
with open("day5/names.txt" , "r") as f:
    names = f.readlines()
    names = [name.strip() for name in names]
    
print(names)