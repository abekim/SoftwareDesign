try:
    import unittest2 as unittest
except ImportError:
    import unittest

from prep import *

class FunctionalTestCases(unittest.TestCase):
    def setUp(self):
        pass

    def test_sum_mults(self):
        self.assertEquals(sum_mults(5), 3)
        self.assertEquals(sum_mults(20), 78)

    def test_flatten(self):
        self.assertEquals(flatten([1, 2, [3, 4], [5, [6, 7]]]), [1, 2, 3, 4, 5, [6, 7]])

    def test_rotate_word(self):
        self.assertEquals(rotate_word('melon', -10), 'cubed')
        self.assertEquals(rotate_word('cheer', 7), 'jolly')
        self.assertEquals(rotate_word('wow', 7), 'dvd')

class StructuralTestCases(unittest.TestCase):
    def setUp(self):
        self.bank = BankAccount(1000.)  # bank account with initial balance of $1000
        self.books = [
            Book('Kavalier & Clay', 'Michael Chabon', 400, 2000),
            Book('1984', 'George Orwell', 100, 1984), 
            Book('Bible', 'No one knows', 10000, -2000),
            Book('Animal Farm', 'George Orwell', 200, 2000),
            Book('Abe\'s Book', 'Abe Kim', 50, 1984),
            Book('newBook', 'No one knows', 45, 1984)
        ]
        self.col = Collection(self.books)

    def test_bank(self):
        self.assertEquals(self.bank.get_balance(), 1000.)
        self.assertEquals(self.bank.withdraw(522), 1000. - 522)
        self.assertEquals(self.bank.deposit(522), 1000.)

    def test_books(self):
        self.assertEquals([b.title for b in self.col.filter_by_published(1984)], ['1984', 'Abe\'s Book', 'newBook'])
        self.assertEquals([b.title for b in self.col.filter_by_author('No one knows')], ['Bible', 'newBook'])
        self.assertEquals([b.title for b in self.col.filter_by_title('A')], ['Animal Farm', 'Abe\'s Book'])

if __name__ == '__main__':
    unittest.main()