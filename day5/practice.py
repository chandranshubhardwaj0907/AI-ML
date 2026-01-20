with open("day5/sample.txt", "r") as f:
    while True:
        content = f.readline()
        
        if content == "":
            print("Word not found")
            break

        if "python" in content.lower():
            print("Found the word 'python'!")
            break

        print(content)
