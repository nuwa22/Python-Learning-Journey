# map is a built-in function that applies a given function to each item of an
# iterable (like a list) and returns an iterator that yields the results.

# syntax: map(function, iterable, ...)

numbers = [1, 2, 3, 4, 5]

# using a regular function with map
# use list to convert the map object to a list
double = list(map(lambda x: x * 2, numbers))
print(double)
