# -*- coding: utf-8 -*-
"""
Basic Python problems

author: abe kim
"""

# takes a user input and prints a statement using the input
def hello():
    name = raw_input("Hello! What's your name? ")
    print "Nice to meet you,", name + "!"
    return
    
# negates a number
def negative(n):
    return n*(-1)

# checks if n is even
def is_even(n):
    return not(n%2)  # in other words, if n%2 == 0

# prints 99 bottles
# TODO: change to 99 bugs
def n_bottles(n):
    lines = ""
    for num in range(1,n+1)[::-1]:
        if not(num%10):
            chant = raw_input("STOP! Decide on who you'll call and what you'll say to them: ")
            lines += chant + "\n"
        print """
        %i bottles of beer on the wall,
        %i bottles of beer.\n
        you take one down,\n 
        pass it around,\n
        put it on the wall,\n 
        advance the slide,\n
        grab another beer,\n
        %s\n
        %i bottles of beer on the wall!
        """ % (num, num, lines, num-1)
        num -= 1
        raw_input("Press any key for next slide.")
    return

# prints all elements in a list
def read_list(li):
    for i, elem in enumerate(li):
        print "index: %i, element:" % (i), elem
    return

# reverses a list iteratively
# We can also use `li[::-1]` (using step parameter)
def reverse(li):
    rev = []
    for i in range(len(li)):
        rev.append(li.pop())
    return rev

# minimum of two numbers - using conditionals
#def minimum(x,y):
#    if x <= y: return x
#    else: return y

# minimum of two numbers - using ternary notation
#def minimum(x,y):
#    return x if (x <= y) else y

# minimum of two numbers - using built-in function
def minimum(x,y):
    return min(x,y)

# order a list
def order(li):
    return sorted(li)
#    return li.sort()

# checks if n is a multiple of 3 and 5
def multiple(n):
    return not(n%3) or not(n%5)

# returns the sum of all multiples of 3 and 5 less than n
def sum_mults(n):
    res = 0
    
    for i in range(1, n):
        if multiple(i): res += i

    return res        

# pythagorean
def pyth(a, b):
    return (a**2 + b**2)**.5

# factorials - iterative
def fact(n):
    res = 1 # initialize result
    
    # the for loop does:
    #   1 * 2 * 3 * 4 * ... * n
    for i in range(n):
        res *= (i+1)
    
    return res

if __name__ == "__main__":
    print "Run"












