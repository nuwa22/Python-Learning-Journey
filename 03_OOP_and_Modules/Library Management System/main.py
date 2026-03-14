from book import Book
from library import Library

def main():
    my_library = Library()
    
    # choose action
    while True:
        print("\n-------Library Menu-------")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        user_input = int(input("Enter your choice: "))

        if user_input == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            new_book = Book(title, author, isbn)
            my_library.add_book(new_book)
        elif user_input == 2:
            my_library.display_books()
        elif user_input == 3:
            title = input("Enter book title to borrow: ")
            my_library.borrow_book(title)
        elif user_input == 4:
            title = input("Enter book title to return: ")
            my_library.return_book(title)
        elif user_input == 5:
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()