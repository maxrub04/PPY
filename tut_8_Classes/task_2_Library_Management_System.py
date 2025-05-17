"""Objective: Design a system to manage books in a library, where you can add books, check
them in/out, and display information about books in the library.
Instructions:
1. Create a Book class:
o Each book should have the following attributes: title, author, isbn,
and availability (whether the book is available or checked out).
o The Book class should have methods:
§ check_in() to mark the book as available.
§ check_out() to mark the book as checked out.
§ is_available() to check if the book is available.
2. Create a Library class:
o The library should store a list of Book objects.
o The Library class should have methods:
§ add_book(book) to add a book to the library.
§ display_books() to display information about all books in the
library.
§ find_book(isbn) to find a book by its ISBN and display its details.
3. Test the system:
o Create several books, add them to the library, and check some books in and
out.
o Display the books in the library and check availability.
# Create some Book instances
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("1984", "George Orwell", "9780451524935")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")"""


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_in(self):
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out:
            raise ValueError(f"Book '{self.title}' is already checked out")
        self.is_checked_out = True

    def is_available(self):
        return not self.is_checked_out

    def __str__(self):
        status = "available" if self.is_available() else "checked out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Can only add Book objects to the library")
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("1984", "George Orwell", "9780451524935")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")


library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("\n--- Initial Library ---")
library.display_books()

book1.check_in()
book2.check_out()
book3.check_out()

print("\n--- After Some Books Checked Out ---")
library.display_books()

print("\n--- Finding a Book by ISBN ---")
found_book = library.find_book("9780743273565")
if found_book:
    print(found_book)
else:
    print("Book not found.")
