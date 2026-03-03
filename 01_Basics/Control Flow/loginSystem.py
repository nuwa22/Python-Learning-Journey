username = input("Enter your username: ") # usewrname is admin
password = input("Enter your password: ") # password is password123

if username == "admin" and password == "password123":
    print("Login successful! Welcome, admin.")
else:
    print("Login failed! Invalid username or password.")