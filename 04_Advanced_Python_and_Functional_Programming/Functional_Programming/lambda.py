# this is a regular function that adds 10 to the input value

def add_ten(x):
    return x + 10

print(add_ten(5))  # Output: 15

# this is a lambda function that does the same thing as add_ten
# syntax: lambda arguments: expression

my_lambda = lambda x: x + 10

print(my_lambda(5))  # Output: 15