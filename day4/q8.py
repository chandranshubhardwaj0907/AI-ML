#  Create a class Player with: 
# •  a class variable player_count 
# •  instance variables name and level 
# Track how many players were created. 

class player:
    player_count = 0
    def __init__(self , name , level):
        self.name = name 
        self.level = level
        player.player_count += 1

    def count(self):
        print(f"the count is {player.player_count}")
        
p1 = player("Alice" , 5)
p2 = player("Bob" , 10)
print(p1.count())
        