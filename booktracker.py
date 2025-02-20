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
    