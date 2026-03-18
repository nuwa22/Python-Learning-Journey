words = ["apple", "cat", "elephant", "dog", "banana"]

word_filter = list(filter(lambda word: len(word) < 5, words))
print(word_filter)

# we can also use
word_filter = [word for word in words if len(word) < 5]
print(word_filter)