# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import *
import Image
from math import cos, sin, pi

fs = {
    "prod": {
        "fn": lambda a, b: a * b,
        "arg": 2
        },
    "cos_pi": {
        "fn": lambda a: cos(pi * a),
        "arg": 1
        },
    "sin_pi": {
        "fn": lambda a: sin(pi * a),
        "arg": 1
        },
    "cube": {
        "fn": lambda x: x**3,
        "arg": 1
        },
    "x": {
        "fn": lambda x: x,
        "arg": 0
        },
    "y": {
        "fn": lambda y: y,
        "arg": 0
        },
    "avg": {
        "fn": lambda a, b: (a + b) / 2,
        "arg": 2
    }
}

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
        args = [build_random_function(min_depth-1, max_depth-1) for i in range(fs[f]["arg"])] # add as many arguments as there needs to be

        return [f].append(args)

def evaluate_random_function(f, x, y):
    # your doc string goes here

    # your code goes here
    return

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

    im = Image.new('wut', (350,350))
    
