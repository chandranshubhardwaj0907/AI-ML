info = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "surname": "Doe",
}

print("Keys:", info.keys())
print("Values:", info.values())
print("Items:", info.items())


print(info.get("name"))  # Output: Johnn

print(info["age"])  # Output: 25

info.update({"age": 26})
print("Updated age:", info["age"])  # Output: 26