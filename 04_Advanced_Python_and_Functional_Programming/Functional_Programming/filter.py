# Filter function in Python is used to filter out elements from an iterable
# (like a list) based on a specified condition. It takes two arguments: a function
# that defines the condition and an iterable to filter. The function should return
# True for elements that should be included in the result and False for those that should be excluded.

# syntax: filter(function, iterable)
numbers = [10, 55, 30, 80, 25]

big_numbers = list(filter(lambda x: x > 50, numbers))

print(big_numbers)

