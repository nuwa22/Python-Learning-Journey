import sys
# Generator Expression
prices = [100, 250, 300, 450, 500]

discounted_prices = (n - 50 for n in prices)

# we can use next() function to get the next value from the generator expression
print(next(discounted_prices))
print(next(discounted_prices))
print(next(discounted_prices))
print(next(discounted_prices))
print(next(discounted_prices))

# we can also use a for loop to iterate over the generator expression

for price in discounted_prices:
    print(price)

# Using the generator expression

# -----------------------------------------------

# Genarator Expression
my_gen = (x for x in range(10000))
print(sys.getsizeof(my_gen), "bytes")

# List Comprehension
my_list = [x for x in range(10000)]
print(sys.getsizeof(my_list), "bytes")

# we use the generator expression when we want to save memory and we don't need
# to store all the values in memory at once. The generator expression will generate
# the values on-the-fly as we iterate over it, while the list comprehension will create
# a list in memory that contains all the values.


