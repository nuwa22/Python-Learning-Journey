# Comprehension
# We can use comprehensions to create new lists, sets, and dictionaries from existing
# iterables in a concise and readable way.

# List Comprehension
number = [1, 2, 3, 4, 5]

doubled = [n * 2 for n in number]

print(doubled)

# ------------ Discount Calculator ----------------

prices = [100, 250, 300, 450, 500]

discounted_prices = [n - 50 for n in prices]

print(discounted_prices)