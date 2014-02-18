# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import *
import Image
from math import cos, sin, pi

# dictionary that maps function names to the function and the number of argument it takes in
fs = {
  "prod": lambda x, y: x * y,
"cos_pi": lambda x, _: cos(pi * x),
"sin_pi": lambda x, _: sin(pi * x),
  "cube": lambda x, _: x**3,
     "x": lambda x, _: x,
     "y": lambda _, y: y,
   "avg": lambda x, y: (x + y) / 2
}

# issues with min_depth
def build_random_function(min_depth, max_depth):
    '''
    generates a random function with nested layers between min_depth and max_depth
    '''
    fnames = fs.keys() # get the names of the functions

    # base case
    if max_depth == 1:
        return ["x"] if random() < 0.5 else ["y"] 
    else:
        f = fnames[randint(0, len(fnames)-1)] # randomly select a function
        args = [build_random_function(min_depth-1, max_depth-1) for _ in range(2)] # add as many arguments as there needs to be

        if len(args): return [f] + args
        else: return [f]

def evaluate_random_function(f, x, y):
    '''
    evalues f using x and y
    '''
    fun = f[0] # get the function name

    try:
        if fun in ['x', 'y']: return fs[fun](x, y)
        else: return fs[fun](evaluate_random_function(f[1]), evaluate_random_function(f[2]))
    except KeyError:
        raise Exception("No such function in list of base functions.")

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
    return
    # your code goes here

if __name__ == '__main__':
    # aliases 
    build = build_random_function
    ev = evaluate_random_function
    remap = remap_interval

    # im = Image.new('wut', (350,350))

    # print build(2, 3)
    print ev(build(2, 3))
    
