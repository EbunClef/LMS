# Import the Book and Library classes 
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
# Create an instance of the Library class
library = Library()

# Test the add_book method
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
member1 = Member("ID001", "John")
member2 = Member("ID002", "Alice")


# # Print the current library content
# print("Library after adding books:")
# for book in library.library:
#     print(book.to_dict())

# # Test the remove_book method
# library.remove_book("ISBN125")
# library.remove_book("ISBN123")
# library.remove_book("ISBN131")

# # Print the library content after removing a book
# print("\nLibrary after removing a book:")
# for book in library.library:
#     print(book.to_dict())


# # Print the contents of the library
# print("Library Contents:")
# for book in library.library:
#     print(book.to_dict())


# # Test the search_by_author method
# author_to_search = input("What author do you want to search for? ")
# search_result = library.search_by_author(author_to_search)

# print("\nSearch Result:")
# if search_result:
#     for book in search_result:
#         print(book.to_dict())
# else:
#     print(f"No books found by {author_to_search}.")

# # Test the search_by_genre method
# genre_to_search = input("What genre do you want to search for? ")
# search_result = library.search_by_genre(genre_to_search)

# print("\nSearch Result:")
# if search_result:
#     for book in search_result:
#         print(book.to_dict())
# else:
#     print(f"No books found of the genre {genre_to_search}.")
    
# # Test the get_book_by_title method
# title_to_search = input("What book title do you want to get? ")
# search_result = library.get_book_by_title(title_to_search)

# print("\nSearch Result:")
# if search_result:
#     for book in search_result:
#         print(book.to_dict())
# else:
#     print(f"No books found of the genre {title_to_search}.")

# # Test the get_available_books method
# quantity_to_check = int(input("Enter the minimum quantity of available copies: "))
# available_books_result = library.get_available_books(quantity_to_check)

# print("\nAvailable Books:")
# if available_books_result:
#     for book in available_books_result:
#         print(book.to_dict())
# else:
#     print(f"No books with at least {quantity_to_check} available copies.")

# #Test the borrow_book method
# print("Borrowing process for member 1:")
# result_member1 = member1.borrow_book(book1)
# if result_member1:
#     print(f"{member1.name} has borrowed {book1.title}.")
# else:
#     print(f"Failed to borrow {book1.title} for {member1.name}.")

# print("\nBorrowing process for member 2:")
# result_member2 = member2.borrow_book(book10)
# if result_member2:
#     print(f"{member2.name} has borrowed {book1.title}.")
# else:
#     print(f"Failed to borrow {book1.title} for {member2.name}.")

# # Print the list of borrowed books for each member
# print("\nList of borrowed books for member 1:")
# for book in member1.books_borrowed:
#     print(book.to_dict())

# print("\nList of borrowed books for member 2:")
# for book in member2.books_borrowed:
#     print(book.to_dict())


# #second borrow test

# # Create an instance of the Members class
# member = Members("ID001", "John")
# member.library = library.library  # Provide access to the library

# # Test borrowing by book object
# print("Borrowing by book object:")

# book_to_borrow = input('Which book do you want to borrow? ')
# member.borrow_book(book_to_borrow)
# print("Books borrowed by member:", member.get_borrowed_books())

# # Test borrowing by book title
# print("\nBorrowing by title:")
# member.borrow_book("Things Fall Apart")
# print("Books borrowed by member:", member.get_borrowed_books())

######To test Library system

# Create an instance of the LibrarySystem class
library_system = LibrarySystem()

# Add members to the library system
library_system.add_member(member1)
library_system.add_member(member2)

# Test borrowing books
print("Borrowing process:")
library_system.borrow_book("ID001", "Things Fall Apart")
library_system.borrow_book("ID002", book2)

# # Test returning books
# print("\nReturning process:")
# library_system.return_book("ID001", book1)

# # Get library status
# print("\nLibrary status:")
# print(library_system.get_library_status())

# # Get member status
# print("\nMember status:")
# print(library_system.get_member_status())

# Convert library system to dictionary
print("\nLibrary system dictionary:")
print(library_system.to_dict())