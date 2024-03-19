from book import Book
from library import Library

class Members:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []

    def borrow_book(self, book_or_title, library):
        if isinstance(book_or_title, Book):
            return self._borrow_book_by_book(book_or_title)
        elif isinstance(book_or_title, str):
            return self._borrow_book_by_title(book_or_title, library)
        else:
            print("Invalid argument.")
            return False

    def _borrow_book_by_book(self, book):
        if book.quantity <= 0:
            print("No available copies of the book.")
            return False

        book.quantity -= 1
        self.books_borrowed.append(book)
        print("Book borrowed successfully.")
        return True

    def _borrow_book_by_title(self, title, library):
        book_to_borrow = None
        for book in library:
            if book.title == title:
                book_to_borrow = book
                break

        if not book_to_borrow:
            print("Book not found in the library.")
            return False

        if book_to_borrow.quantity <= 0:
            print("No available copies of the book.")
            return False

        book_to_borrow.quantity -= 1
        self.books_borrowed.append(book_to_borrow)
        print("Book borrowed successfully.")
        return True


# Create instances of the Book class
book1 = Book("ISBN123", "Aké: The Years of Childhood", "Wole Soyinka", "Autobiography", 15, 1981)
book2 = Book("ISBN124", "Half of a Yellow Sun", "Chimamanda Ngozi Adichie", "Historical Fiction", 10, 2006)
book3 = Book("ISBN125", "Things Fall Apart", "Chinua Achebe", "Historical Fiction", 20, 1958)
# Create an instance of the Library class
library = Library()

# Test the add_book method
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

#Create instances of the Members class
member1 = Members("ID001", "John")
member2 = Members("ID002", "Alice")

# Test borrowing by book object
print("Borrowing process for member 1 by book object:")
result_member1_book = member1.borrow_book(book1)
if result_member1_book:
    print(f"{member1.name} has borrowed {book1.title}.")
else:
    print(f"Failed to borrow {book1.title} for {member1.name}.")

# Test borrowing by title
print("\nBorrowing process for member 2 by title:")
result_member2_title = member2.borrow_book("Things Fall Apart", library.library)
if result_member2_title:
    print(f"{member2.name} has borrowed Things Fall Apart.")
else:
    print(f"Failed to borrow Things Fall Apart for {member2.name}.")


# Print the list of borrowed books for each member
print("\nList of borrowed books for member 1:")
if member1.books_borrowed:
    for book in member1.books_borrowed:
        print(book.to_dict())
else:
    print("No books borrowed.")

print("\nList of borrowed books for member 2:")
if member2.books_borrowed:
    for book in member2.books_borrowed:
        print(book.to_dict())
else:
    print("No books borrowed.")
