from book import Book
from library import Library

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []

    def borrow_book(self, book_or_title, library):
        if isinstance(book_or_title, str):
            # Borrow a book by title
            book_to_borrow = library.get_book_by_title(book_or_title)
            if book_to_borrow is None:
                print(f"Book with title '{book_or_title}' not found in the library.")
                return False
        elif isinstance(book_or_title, Book):
            # Borrow a book by book object
            book_to_borrow = book_or_title
        else:
            print("Invalid argument. Please provide a book object or a book title.")
            return False

        if book_to_borrow.quantity <= 0:
            print("No available copies of the book.")
            return False
        
        book_to_borrow.quantity -= 1
        self.books_borrowed.append(book_to_borrow)
        print("Book borrowed successfully.")
        return True

    def return_book(self, book):
        if book in self.books_borrowed:
            book.quantity += 1
            self.books_borrowed.remove(book)
            print("Book returned successfully.")
            return True
        else:
            print("Book not borrowed by this member.")
            return False

    def get_borrowed_books(self):
        borrowed_books_info = []
        for book in self.books_borrowed:
            borrowed_books_info.append(book.to_dict())
        return borrowed_books_info

    def to_dict(self):
        return {
            'member_id': self.member_id,
            'name': self.name,
            'books_borrowed': [book.to_dict() for book in self.books_borrowed]
        }
