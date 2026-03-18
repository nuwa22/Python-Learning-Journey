from functools import reduce

nums = [2, 3, 4, 5]

multiplication = reduce(lambda x, y: x * y, nums)
print(multiplication)