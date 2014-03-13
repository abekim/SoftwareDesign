'''
Helping students study for the midterm

author: @abekim
'''
# sum of multiples
def sum_mults(n):
    ''' return the sum of all multiples of 3 and 5 less than n '''
    return

# flatten
def flatten(li):
    ''' flattens li by one layer '''
    return

# ROTn
def rotate_word(s, n):
    ''' rotates the word s by n using ROTn encryption method '''
    
# Bank Account object
class BankAccount:
    ''' A Simple Bank Account '''
    def __init__(self, balance=0.):
        ''' construct a bank account object with beginning balance '''

    def get_balance(self):
        ''' return the current balance '''
        return 

    def withdraw(self, amount):
        ''' withdraw amount and return new balance '''
        return 

    def deposit(self, amount):
        ''' deposit certain amount and return new balance '''
        return 

# Book
class Book:
    def __init__(self, title, author, length, published):
        ''' construct a book object with given properties '''

# Collection of Books
class Collection:
    def __init__(self, books=[]):
        self.books = books

    def filter_by_published(self, year):
        ''' return all books in collection published in year '''

    def filter_by_author(self, author):
        ''' return all books in collection by author '''

    def filter_by_title(self, char):
        ''' returns all books in collection whose title starts with char '''

if __name__ == '__main__':
    books = [
        Book('Kavalier & Clay', 'Michael Chabon', 400, 2000),
        Book('1984', 'George Orwell', 100, 1984), 
        Book('Bible', 'No one knows', 10000, -2000),
        Book('Animal Farm', 'George Orwell', 200, 2000),
        Book('Abe\'s Book', 'Abe Kim', 50, 1984)
    ]
    
    col = Collection(books)