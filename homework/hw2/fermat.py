'''
Fermat's Theorem

a**n + b**n == c**n
'''
# Problem 5.3 - Fermat's Last Theorem
def check_fermat(a, b, c, n):
    # checks if a, b, c, n violate Fermat's Last Theorem    
    if (n <= 2) or not ((a**n + b**n) == (c**n)):
        print "No, that doesn't work."
    else:
        print "Holy smokes, Fermat was wrong!"

def user_fermat():
    # user input in following format: a, b, c, n
    inputs = raw_input("Enter a, b, c, and n (a, b, c, n): ")
    [a, b, c, n] = [int(i.strip()) for i in inputs.split(',')]
    check_fermat(a, b, c, n)
