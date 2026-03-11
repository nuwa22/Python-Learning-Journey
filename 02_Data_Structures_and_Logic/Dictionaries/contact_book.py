phone_book = {
    "Kamal" : "071-2345678",
    "Nimal" : "071-9876543",
    "Sunil" : "071-4567890"
}

user_input = input("Enter the name to search for: ")

result = phone_book.get(user_input, "Name not found in phone book")
print(user_input + "'s phone number is: " + result)
