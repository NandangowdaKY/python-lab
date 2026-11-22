class Library:
    def __init__(self):
        self.books = {
            "Python": 3,
            "Java": 2,
            "Data Structures": 4,
            "DBMS": 2
        }
        self.borrowed = {}

    def display_books(self):
        print("\nAvailable Books")
        for book, quantity in self.books.items():
            print(f"{book}: {quantity} copies")

    def borrow_book(self, book):
        if book in self.books and self.books[book] > 0:
            self.books[book] -= 1
            self.borrowed[book] = self.borrowed.get(book, 0) + 1
            print(f"{book} borrowed successfully")
        else:
            print("Book is not available")

    def return_book(self, book):
        if self.borrowed.get(book, 0) > 0:
            self.books[book] += 1
            self.borrowed[book] -= 1
            print(f"{book} returned successfully")
        else:
            print("This book was not borrowed")


library = Library()

while True:
    print("\nLIBRARY MANAGEMENT SYSTEM")
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        library.display_books()
        book = input("Enter book name: ").strip().title()
        library.borrow_book(book)

    elif choice == "3":
        book = input("Enter book name: ").strip().title()
        library.return_book(book)

    elif choice == "4":
        print("Thank you for using the Library")
        break

    else:
        print("Invalid choice")
