from typing import List, Dict, Union
from library import Library
from member import Member
from book import Book

class LibrarySystem:
    def __init__(self):
        self.library = Library()
        self.members: List[Member] = []
        
    def add_member(self, member: Member):
        self.members.append(member)
        
    def remove_member(self, member_id: str):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                break
                
    def search_books(self, query: str) -> List[Dict]:
        # Search for books based on title, author, or genre
        search_result = []
        for book in self.library.library:
            if (query.lower() in book.title.lower() or
                query.lower() in book.author.lower() or
                query.lower() in book.genre.lower()):
                search_result.append(book.to_dict())
        return search_result
    
    def borrow_book(self, member_id: str, book_title: str) -> Union[str, None]:
        # Allows a member to borrow a book
        member = self.find_member_by_id(member_id)
        if member is None:
            return "Member not found."

        book_to_borrow = None
        for book in self.library.library:
            if book.title.lower() == book_title.lower() and book.quantity > 0:
                book_to_borrow = book
                break

        if book_to_borrow is None:
            return "Book '{}' not found or not available for borrowing.".format(book_title)

        borrowing_result = member.borrow_book(self.library, book_to_borrow.title)
        if borrowing_result:
            return borrowing_result

        return "Book '{}' successfully borrowed by {}.".format(book_title, member.name)
        
    def return_book(self, member_id: str, book_title: str) -> Union[str, None]:
        # Allows a member to return a book
        member = self.find_member_by_id(member_id)
        if member is None:
            return "Member not found."
        
        for book in member.books_borrowed:
            if book.title.lower() == book_title.lower():
                member.return_book(self.library, book)
                return None
        
        return "Book '{}' not found in the borrowed books list of {}.".format(book_title, member.name)
    
    def get_library_status(self) -> List[Dict]:
        # Returns the list of available books in the library
        return self.library.to_dict()
    
    def get_member_status(self) -> List[Dict]:
        # Returns the list of members and their borrowed books
        member_status = []
        for member in self.members:
            member_status.append(member.to_dict())
        return member_status
    
    def to_dict(self) -> Dict:
        # Returns a dictionary representation of the entire library system
        return {
            'library': self.library.to_dict(),
            'members': [member.to_dict() for member in self.members]
        }
    
    def find_member_by_id(self, member_id: str) -> Union[Member, None]:
        # Helper method to find a member by ID
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
