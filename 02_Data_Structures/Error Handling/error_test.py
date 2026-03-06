try:
    number = int(input("Enter a number: "))
    result = 100/number
    print("Answer is", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("This block will always execute.")

# We can use:
# ZeroDivisionError to handle division by zero errors.
# ValueError to handle invalid input errors.
# TypeError to handle type errors.
# IndexError to handle index errors.
# FileNotFoundError to handle file not found errors.
# NameError to handle name errors.
