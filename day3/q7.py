# Given a list of words:
# Q6
# words
# =
# [
# "apple",
# "banana",
# "kiwi",
# "cherry",
# "mango"
# ]
# Create a dictionary that maps each word to its length.
# Example:
# {"apple": 5, "banana": 6, "kiwi": 4, ...}

words = ["apple", "banana", "kiwi", "cherry", "mango"]
word_length_dict = {}

for word in words:
    word_length_dict[word] = len(word)
print("Dictionary mapping words to their lengths:", word_length_dict)
8