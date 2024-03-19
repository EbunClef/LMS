from book import Book
from library import Library
from member import Member


class LibrarySystem:
    
    def __init__(self):
        
        self.library = Library()
        self.members = []
        
    def add_member(self, member):
         #Adds a member to the system
         self.members.append(member)
    
    def remove_member(self,member_id):
        #removes a member from the system
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member_id)
                break
            
    def search_books(self, query):
        #search for books based on author, title or genre
        self.search_library.search_books(query)
        
    def borrow_book(self,member_id,book_or_title):
        #Allows a member to borrow a book
        member = self.find_member(member_id)
        if member:
            return member.borrow_book(book_or_title, self.library)
        else:
            print("Member not found.")
            return False
    
    def return_book(self, member_id, book):
        # Allows a member to return a book
        member = self.find_member(member_id)
        if member:
            return member.return_book(book)
        else:
            print("Member not found.")
            return False
        
    def get_library_status(self):
        # Returns the list of available books in the library
        return self.library.get_books()
    
    def get_member_status(self):
        # Returns the list of members and their borrowed books
        member_status = {}
        for member in self.members:
            member_status[member.name] = member.get_borrowed_books()
        return member_status
    
    def to_dict(self):
        # Returns a dictionary representation of the entire library system
        library_system_dict = {
            'library': self.library.to_dict(),
            'members': [member.to_dict() for member in self.members]
        }
        return library_system_dict
    
    def find_member(self, member_id):
        # Helper method to find a member by member ID
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

# LibrarySystem Class:

# Attributes:
# library: An instance of the Library class.
# members: A list storing Member instances.

# Methods:
# __init__: Initializes the library and the list of members.
# add_member: Adds a member to the system.
# remove_member: Removes a member from the system.
# search_books: Searches for books based on title, author, or genre.
# borrow_book: Allows a member to borrow a book.
# return_book: Allows a member to return a book.
# get_library_status: Returns the list of available books in the library.
# get_member_status: Returns the list of members and their borrowed books.
# to_dict: Returns a dictionary representation of the entire library system.
