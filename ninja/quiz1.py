# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:33:16 2014

@author: abekim
"""

from unum.units import *

# problem 3
#   part a) 
def hinge (n):
    return 0 if n < 0 else n

#   part b)
def print_number_of_days (n):
    print "There are %i days left in the week." % n if n > 1 else "There is 1 day left in the week."

if __name__ == '__main__':
    # 1. 0.00046332 [mile2/h]
    # 2. a) cd && ls 
    #    b) mkdir SoftwareDesign
    #    c) cat homework.txt
    
    # 1. Show 100 m**2 / 5 min in mile**2 / h
    area = 100 * m**2
    time = 5 * min
    
    eff = area / time
    
    print "%i [m2/min] to [mile2/h]:" % (100/5), eff.asUnit(mile**2 / h)
    
    print [hinge(i) for i in range(-2,3)]
    [print_number_of_days (i) for i in range(1,4)]
    
    

