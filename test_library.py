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

    def test_return_book(self):
        book = Book(isbn="978-93-5163-389-1",title="Data Structure Using C",author="Sharad Kumar Verma",publicationYear=2015)
        self.Library.add_book(book)
        self.Library.borrow_book("978-93-5163-389-1")
        self.Library.return_book("978-93-5163-389-1")
        self.assertTrue(book.available)

    def test_view_available_books(self):
        book1 = Book(isbn="978-93-5163-389-1",title="Data Structure Using C",author="Sharad Kumar Verma",publicationYear=2015)
        book2 = Book(isbn="978-93-5019-561-1", title="Junior Level Books Introduction to Computer", author="Amit Garg", publicationYear=2011)
        self.Library.add_book(book1)
        self.Library.add_book(book2)
        self.Library.borrow_book("978-93-5163-389-1")
        available_books = self.Library.view_available_books()
        self.assertIn(book2, available_books)
        self.assertNotIn(book1, available_books)

if __name__ == '__main__':
    unittest.main()