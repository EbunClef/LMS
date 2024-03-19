# 

class Library:
    def __init__(self):
        
        self.library = []
        
    def add_book(self, book):
        # Adds a book to the library
        self.library.append(book)
        
    def remove_book(self, isbn):
        # Removes a book from the library
        
        for book in self.library:
            if book.isbn == isbn:
                self.library.remove(book)
                break

    
    def search_by_author(self, author):
        # Retrieves books by a specific author
        
        search_by_author_result = []
        
        for book in self.library:
            if book.author == author:
                search_by_author_result.append(book)
        return search_by_author_result
        
    def search_by_genre(self, genre):
        # Retrieves books by a specific genre
        
        search_by_genre_result = []
        
        for book in self.library:
            if book.genre == genre:
                search_by_genre_result.append(book)
        return search_by_genre_result
    
    def get_book_by_title(self, title):
        # Retrieves books by a specific title
        
        get_book_by_title_result = []
        
        for book in self.library:
            if book.title == title:
                get_book_by_title_result.append(book)
        return get_book_by_title_result
        
    def get_available_books(self, quantity=1):
        # Retrieves books with available copies
        
        available_copies = []
        
        for book in self.library:
            if book.quantity >= quantity:
                available_copies.append(book)
        return available_copies    
    
    def to_dict(self):
        # Returns a list of dictionaries representing each book in the library
        
        library_dict = []
        for book in self.library:
            library_dict.append(book.to_dict())
        return library_dict
    
            
        
        


