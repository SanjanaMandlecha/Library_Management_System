import unittest
from library import Book,Library

class Library_Testing(unittest.TestCase):
    def setUp(self):
        self.Library = Library()

    def test_add_books(self):
        book = Book(isbn="978-93-5163-389-1",title="Data Structure Using C",author="Sharad Kumar Verma",publicationYear=2015)
        self.Library.add_book(book)
        self.assertIn(book,self.Library.books)

if __name__ == '__main__':
    unittest.main()