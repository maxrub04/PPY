#Library Book Checkout System (Boolean, While
#Loop, Dictionary, If-Else)

library_books = {
"The Great Gatsby": True,
"1984": False,
"Moby Dick": True,
"To Kill a Mockingbird": False
}

def checkout_system():
    print("Welcome to our library!")
    while True:
        print("\nList of books available:")
        for book, available in library_books.items():
            status = "Available" if available else "Checked out"
            print(f"- {book}: {status}")

        choice = input("\nEnter the name of the book to borrow it (or type 'stop' to exit): ").strip()

        if choice.lower() == 'stop':
            break

        if choice in library_books:
            if library_books[choice]:
                library_books[choice] = False
                print(f"Book '{choice}' has been checked out !")
            else:
                print(f"Sorry, book '{choice}'is already checked out. Please try again later.")
        else:
            print(f"Book ‘{choice}’ is not in the library. Please try again.")

checkout_system()
