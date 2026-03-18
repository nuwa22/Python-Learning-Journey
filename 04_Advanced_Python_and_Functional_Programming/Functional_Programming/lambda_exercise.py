# multiply_by_three is a lambda function that takes a user input and multiplies it by three.
# The result is printed to the console. The user is prompted to enter a number, which is
# then converted to an integer before being passed to the lambda function.

multiply_by_three = lambda user_input: user_input * 3
print(multiply_by_three(int(input("Enter a number to multiply by three: "))))

