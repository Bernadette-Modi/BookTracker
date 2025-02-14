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

    
