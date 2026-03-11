while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        print("The answer is: ", result)
        break
    except ZeroDivisionError:
        print("You cannot divide by zero! Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")