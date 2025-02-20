class Book:
    def __init__(self, title, author, genre, status="Wish List"):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status

    def mark_as_read(self):
        self.status = "Completed"
    
    def mark_as_reading(self):
        self.status = "Currently Reading"

    def __str__(self):
        return f"{self.title} by {self.author} [{self.status}]"

    
book_list = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    book = Book(title, author, genre)
    book_list.append(book)
    print(f"\n'{title} added to your book list!\n")

def view_books():
    if not book_list: 
        print("\nYour book list is empty.\n")
    else:
        print("\nYour Book List: ")
        for idx, book in enumerate(book_list, start=1):
            print(f"{idx}. {book}")
        print()

def remove_book():
    view_books()
    if book_list:
        try:
            index = int(input("Enter the number of the book to remove: "))
            removed_book = book_list.pop(index)
            print(f"\n'{removed_book.title}' removed from your list.\n")
        except (IndexError, ValueError):
            print("\nInvalid selection.\n")

def update_status():
    view_books()
    if book_list:
        try:
            index = int(input("Enter the number of the book to update: ")) - 1
            book = book_list[index]
            choice = input("Mark as (1) Completed or (2) Currently Reading? ")
            if choice == "1":
                book.mark_as_read()
            elif choice == "2":
                book.mark_as_reading()
            else:
                print("\nInvalid choice.\n")

def main_menu():
    while True:
        print("\nBook Tracker Menu: ")
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Update Status")
        print("5. Quit")
        choice = input("\nChoose an option: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            remove_book()
        elif choice == '4':
            update_status()
        elif choice == '5':
            print("\nGoodbye! Happy reading! 📚")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main menu()

