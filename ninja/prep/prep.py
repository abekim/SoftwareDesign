'''
Helping students study for the midterm

author: @abekim
'''
def multiple(n):
    ''' checks if n is a multiple of 3 and 5 '''
    return not n % 3 or not n % 5

# sum of multiples
def sum_mults(n):
    ''' return the sum of all multiples of 3 and 5 that are less than n '''
    # regular solution
    # res = 0
    
    # for i in range(1, n):
    #     if multiple(i): res += i

    # return res

    # more elegant way
    return sum([i for i in range(1, n) if multiple(i)])

# flatten
def flatten(li):
    ''' flattens li by one layer '''
    res = []

    for elem in li:
        try:
            res += elem
        except TypeError:
            res.append(elem)

    return res

# ROTn
def rotate_word(s, n):
    ''' rotates the word s by n using ROTn encryption method '''
    rotated = ''
    start = ord('a')
    
    for c in s:
        # flag to check if c is in upper case
        upper = False
        if c.isupper():
            upper = True
            c = c.lower()

        rotatedBy = ((ord(c) + n) - start) % 26
        rotatedChar = chr(start + rotatedBy)

        rotated += rotatedChar if not upper else rotatedChar.upper()
    return rotated

# Bank Account object
class BankAccount:
    ''' A Simple Bank Account Class '''
    def __init__(self, balance = 0.):
        ''' construct a bank account object with beginning balance '''
        self.balance = float(balance)

    def __repr__(self):
        return 'Bank Account with balance of $%.2f' % self.balance

    def __str__(self):
        return self.__repr__

    def get_balance(self):
        ''' return the current balance '''
        return self.balance

    def withdraw(self, amount):
        ''' withdraw amount '''
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        ''' deposit certain amount '''
        self.balance += amount
        return self.balance

# Book
class Book:
    def __init__(self, title, author, length, published):
        ''' construct a book object with given properties '''
        self.title = title
        self.author = author
        self.length = length
        self.published = published

    @property
    def properties(self):
        return { 'title': self.title, 'author': self.author, 'length': self.length, 'published': self.published }

# Collection of Books
class Collection:
    def __init__(self, books=[]):
        self.books = books

    def filter_by_published(self, year):
        ''' return all books in collection published in year '''
        return [b for b in self.books if b.published == year]

    def filter_by_author(self, author):
        ''' return all books in collection by author '''
        return [b for b in self.books if b.author == author]

    def filter_by_title(self, char):
        ''' returns all books in collection whose title starts with char '''
        return [b for b in self.books if b.title[0].lower() == char.lower()]

if __name__ == '__main__':
    books = [
        Book('Kavalier & Clay', 'Michael Chabon', 400, 2000),
        Book('1984', 'George Orwell', 100, 1984), 
        Book('Bible', 'No one knows', 10000, -2000),
        Book('Animal Farm', 'George Orwell', 200, 2000),
        Book('Abe\'s Book', 'Abe Kim', 50, 1984)
    ]

    col = Collection(books)
