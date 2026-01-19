color = input("Enter a color: ")

match color:
    case " green":
        print("You chose green.")
    case " red":   
        print("You chose red.")
    case " blue":
        print("You chose blue.")
    case _:
        print("You chose an unknown color.")