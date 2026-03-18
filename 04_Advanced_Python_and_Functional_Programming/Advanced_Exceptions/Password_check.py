class ShortPasswordError(Exception):
    pass

def check_password(password):
    if len(password) < 8:
        raise ShortPasswordError("Password must be at least 8 characters long")
    print("Password is valid")

check_password("12345")