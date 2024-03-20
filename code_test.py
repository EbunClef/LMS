from book import Book
from library import Library
from member import Member
from library_system import LibrarySystem

# Create instances of the Book class
book1 = Book("ISBN123", "Aké: The Years of Childhood", "Wole Soyinka", "Autobiography", 15, 1981)
book2 = Book("ISBN124", "Half of a Yellow Sun", "Chimamanda Ngozi Adichie", "Historical Fiction", 10, 2006)
book3 = Book("ISBN125", "Things Fall Apart", "Chinua Achebe", "Historical Fiction", 20, 1958)
book4 = Book("ISBN126", "The Secret Lives of Baba Segi's Wives", "Lola Shoneyin", "Novel", 5, 2010 )
book5 = Book("ISBN127", "The trials of Brother Jero", "Wole Soyinka", "Satiric Comedy", 10, 1963)
book6 = Book("ISBN128", "The Palm-Wine Drinkard", "Amos Tutuola", "Novel", 5, 1952)
book7 = Book("ISBN129", "Everything Good Will Come", "Sefi Atta", "Novel", 50, 2005)
book8 = Book("ISBN130", "Sozaboy", "Ken Saro-Wiwa", "Novel", 5, 1985)
book9 = Book("ISBN131", "Women of Owu", "Femi Osofisan", "Novel", 25, 2006)
book10 = Book("ISBN132", "The Bride Price", "Buchi Emecheta", "Novel", 7, 1976)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.add_book(book7)
library.add_book(book8)
library.add_book(book9)
library.add_book(book10)

#Create instances of the Members class
member1 = Member("ID001", "Bukola")
member2 = Member("ID002", "Saka")
member3 = Member("ID003", "Osas")
member4 = Member("ID004", "Friday")
member5 = Member("ID005", "Francis")

# Create an instance of the LibrarySystem class
library_system = LibrarySystem()

# Test various methods of the Library class
# print("Library Contents:")
# print(library.to_dict())

# print("\nSearch by author")
# author_to_search = input("Whose book do you want to read today? ")
# search_result = library.search_by_author(author_to_search)

# print("\nSearch Result")
# if search_result:
#     for book in search_result:
#         print(book.to_dict())
# else:
#     print(f"No book found by {author_to_search}")

# print("\nSerach by Book Genre:")
# genre_to_search = input("What book genre would like to read today? ")
# search_result = library.search_by_genre(genre_to_search)

# print("\nSearch Result")
# if search_result:
#     for book in search_result:
#         print(book.to_dict())
# else:
#     print(f"No book with the genre {genre_to_search} \nPlease try another genre.")

# print("\nSearch by book title:")
# book_title = input("What is the title of the book you'd like to read today? ")
# search_result = library.get_book_by_title(book_title)

# print("\nSearch Result")
# if search_result:
#     for book in search_result:
#         print(book.to_dict())
# else:
#     print(f"No book found with the title {book_title}.\nPlease try another book title")

# print("\nWelcome To The Book Lending Portal!!!")


# book_to_borrow = input("Which book will you like to borrow? ")
# lending_processing, quantity_left = member5.borrow_book(library, book_to_borrow)

# print("\nLending in process...")
# print(lending_processing)
# if quantity_left is not None:
#     print("Quantity left after borrowing:", quantity_left)

# # Test get_borrowed_books method
# print("Books borrowed by", member1.name, ":")
# print(member1.get_borrowed_books())


# Add books to the library
library_system.library.add_book(book1)
library_system.library.add_book(book2)
library_system.library.add_book(book3)
library_system.library.add_book(book4)
library_system.library.add_book(book5)
library_system.library.add_book(book6)
library_system.library.add_book(book7)
library_system.library.add_book(book8)
library_system.library.add_book(book9)
library_system.library.add_book(book10)


# Add members to the library system
library_system.add_member(member1)
library_system.add_member(member2)
library_system.add_member(member3)
library_system.add_member(member4)
library_system.add_member(member5)

# # Test searching for books
# print("Searching for books with 'Python' in title, author, or genre:")
# print(library_system.search_books("The Bride Price"))

# # Test borrowing a book
# print("\nBorrowing 'The Bride Price' by Bukola:")
# print(library_system.borrow_book("ID001", "The Bride Price"))

# # Test returning a book
# print("\nReturning 'The Bride Price' by Bukola:")
# print(library_system.return_book("ID001", "The Bride Price"))

# # Test getting library status
# print("\nLibrary Status:")
# print(library_system.get_library_status())

# # Test getting member status
# print("\nMember Status:")
# print(library_system.get_member_status())


