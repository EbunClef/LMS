# Represents each book in the library

from datetime import datetime, timezone


class Book:
    def __init__(self, isbn, title, author, genre, quantity, published_year):
        
        self.isbn = isbn                       # A unique identifier for each book
        self.title = title                     # A string representing the title of the book
        self.author = author                   # A string representing the author of the book
        self.genre = genre                     # A string representing the genre of the book
        self.quantity = quantity               # An integer representing the number of copies available        
        self.published_year = published_year   # An integer representing the year the book was published 

        
    def update(self, quantity=None):
        # Allows updating the quantity of available copies
        
        self.quantity = quantity if quantity is not None else self.quantity
        
    
    def to_dict(self):
        # Returns a dictionary representation of the book
        
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'quantity': self.quantity,
            'published_year': self.published_year
        }