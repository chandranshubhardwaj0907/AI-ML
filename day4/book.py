class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isissued = False
        
    def show(self):
        print(f"Title: {self.title}, Author: {self.author}, Issued: {self.isissued}")
        
class student:
    def __init__(self , name):
        self.name = name
        self.issued_books = []
    
    def issue_book(self, book):
        if not book.isissued:
            book.isissued = True
            self.issued_books.append(book.title)
            print(f"{self.name} issued {book.title}")
        else:
            print(f"{book.title} is already issued")        
            
class library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to library")
        
    def show_books(self):
        for book in self.books:
            book.show()
            
lib = library()

b1 = book("Python", "Guido")
b2 = book("Java", "James")

lib.add_book(b1)
lib.add_book(b2)

s1 = student("Chandranshu")

lib.show_books()

s1.issue_book(b1)

lib.show_books()
