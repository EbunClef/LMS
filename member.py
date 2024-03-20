class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []
        
    def borrow_book(self, library, book_title):
        # Find the book in the library by title
        book_to_borrow = None
        for book in library.library:
            if book.title == book_title:
                book_to_borrow = book
                break
        
        if book_to_borrow is None:
            return "Book with title '{}' not found in the library.".format(book_title), None
        
        # Check if the book is available
        if book_to_borrow.quantity > 0:
            # Reduce the quantity of available copies
            book_to_borrow.quantity -= 1
            # Add the book to the member's list of borrowed books
            self.books_borrowed.append(book_to_borrow)
            return "Book '{}' successfully borrowed by {}. Quantity left: {}.".format(book_title, self.name, book_to_borrow.quantity), book_to_borrow.quantity
        else:
            return "Book '{}' is not available for borrowing.".format(book_title), None
    
        
    def return_book(self, book):
        # Allows a member to return a book
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
        
    def get_borrowed_books(self):
        # Returns a list of dictionaries representing the books borrowed by the member
        borrowed_books_info = []
        for book in self.books_borrowed:
            borrowed_books_info.append(book.to_dict())
        return borrowed_books_info
    
    def to_dict(self):
        # Returns a dictionary representation of the member
        return {
            'member_id': self.member_id,
            'name': self.name,
            'books_borrowed': [book.to_dict() for book in self.books_borrowed]
        }