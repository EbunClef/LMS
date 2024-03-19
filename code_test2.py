from dump import Members



# Create instances of the Members class
member1 = Members("ID001", "John")
member2 = Members("ID002", "Alice") 

# Test the borrow_book method with a book object
print("Borrowing process for member 1:")
result_member1 = member1.borrow_book(book1)
if result_member1:
    print(f"{member1.name} has borrowed {book1.title}.")
else:
    print(f"Failed to borrow {book1.title} for {member1.name}.")

# Test the borrow_book method with a title
print("\nBorrowing process for member 2:")
result_member2 = member2.borrow_book(title="Book Title 2")
if result_member2:
    print(f"{member2.name} has borrowed Book Title 2.")
else:
    print(f"Failed to borrow Book Title 2 for {member2.name}.")

# Print the list of borrowed books for each member
print("\nList of borrowed books for member 1:")
for book in member1.books_borrowed:
    print(book.to_dict())

print("\nList of borrowed books for member 2:")
for book in member2.books_borrowed:
    print(book.to_dict())