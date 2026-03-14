class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.__password = password
    
    def check_password(self, input_pass):
        if input_pass == self.__password:
            return True
        else:
            return False

my_user = User("Suresh", "secret123")
user_input = input("Enter your password: ")
result = my_user.check_password(user_input)

if result == True:
    print("Login successful!")
else:
    print("Login failed! Incorrect password.")




