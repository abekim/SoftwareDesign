try:
    import unittest2 as unittest
except ImportError:
    import unittest

from prep import *

class FunctionalTestCases(unittest.TestCase):
    def setUp(self):
        self.books = [
            Book('Kavalier & Clay', 'Michael Chabon', 400, 2000),
            Book('1984', 'George Orwell', 100, 1984), 
            Book('Bible', 'No one knows', 10000, -2000),
            Book('Animal Farm', 'George Orwell', 200, 2000),
            Book('Abe\'s Book', 'Abe Kim', 50, 1984)
        ]
        self.col = Collection(books)

    