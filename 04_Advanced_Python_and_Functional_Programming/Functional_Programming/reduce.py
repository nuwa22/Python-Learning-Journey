# Reduce is a function that takes a function and a sequence and returns a single value that
# is the result of applying the function to the elements of the sequence. It is part of the
# functools module in Python.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)

