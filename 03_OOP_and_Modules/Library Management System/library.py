
class Library:
    def __init__(self):
        self.books = []

    # add book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")
    
    # display books
    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(book)
    
    # search book
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print("Book not found.")
        return None

    # borrow book
    def borrow_book(self, title):
        book = self.search_book(title)
        if book and book.is_available:
            book.is_available = False
            print(f"You have borrowed '{book.title}'.")
        else:
            print("Book not found or currently unavailable.")
        
    # return book
    def return_book(self, title):
        book = self.search_book(title)
        if book and not book.is_available:
            book.is_available = True
            print(f"You have returned '{book.title}'.")
        else:
            print("Book not found or was not borrowed.")
    
