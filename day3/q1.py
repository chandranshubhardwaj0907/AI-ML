info = [
    ("alice" , "math"),
    ("bob" , "science"),
    ("charlie" , "history"),
    ("david" , "english"),
    ("eve" , "math"),
    ("frank" , "science"),
    ("grace" , "history"),
    ("henry" , "english")
]  
# // Print only the subjects from the list of tuples

unique_courses = set()
for tup in info:
    unique_courses.add(tup[1])
    
    
print(unique_courses)    


for name , course in info:
    if course == "math":
        print(name)
        
