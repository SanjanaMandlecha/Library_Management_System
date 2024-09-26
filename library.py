class Book:
    def __init__(self,isbn,title,author,publicationYear) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publicationYear = publicationYear
        self.available  = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def borrow_book(self,isbn):
        book = None
        for b in self.books:
            if b.isbn == isbn:
                book = b
                break
        if book is None:
            raise Exception("Book Not Found")
        if not book.available:
            raise Exception("Book Not Available")
        book.available = False

    def return_book(self,isbn):
        book = None
        for b in self.books:
            if b.isbn == isbn:
                book = b
                break
        if book is None:
            raise Exception("Book Not Found")
        if book.available:
            raise Exception("Book Not Borrowed")
        book.available = True