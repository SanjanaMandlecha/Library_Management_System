import unittest
from library import Book,Library

class Library_Testing(unittest.TestCase):
    def setUp(self):
        self.Library = Library()

    def test_add_books(self):
        book = Book(isbn="978-93-5163-389-1",title="Data Structure Using C",author="Sharad Kumar Verma",publicationYear=2015)
        self.Library.add_book(book)
        self.assertIn(book,self.Library.books)
    
    def test_borrow_book(self):
        book = Book(isbn="978-93-5163-389-1",title="Data Structure Using C",author="Sharad Kumar Verma",publicationYear=2015)
        self.Library.add_book(book)
        self.Library.borrow_book("978-93-5163-389-1")
        self.assertFalse(book.available)

    def test_borrow_unavailable_book(self):
        book = Book(isbn="978-93-5163-389-1",title="Data Structure Using C",author="Sharad Kumar Verma",publicationYear=2015)
        self.Library.add_book(book)
        self.Library.borrow_book("978-93-5163-389-1")
        with self.assertRaises(Exception) as message:
            self.Library.borrow_book("978-93-5163-389-1")
        self.assertTrue('Book Not Available' in str(message.exception))

if __name__ == '__main__':
    unittest.main()