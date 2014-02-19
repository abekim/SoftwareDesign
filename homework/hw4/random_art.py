# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import *
from PIL import Image
from math import cos, sin, pi

# dictionary that maps function names to the function and the number of argument it takes in
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
        args = [build_random_function(min_depth-1, max_depth-1) for i in range(fs[f]["arg"])] # add as many arguments as there needs to be

        if len(args): return [f] + args
        else: return [f]

def evaluate_random_function(f, x, y):
    '''
    evalues f using x and y
    '''
    fun = f[0] # get the function name

    try:
        if not fs[fun]["arg"]: 
            if fun == "x": return x
            else: return y
        elif fs[fun]["arg"] == 1:
            return fs[fun]["fn"](evaluate_random_function(f[1], x, y))
        else:
            return fs[fun]["fn"](evaluate_random_function(f[1], x, y), evaluate_random_function(f[2], x, y))
    except KeyError:
        raise Exception("No such function in list of base functions.")

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
    inputs = [val, input_interval_start, input_interval_end, output_interval_start, output_interval_end]
    v, i_s, i_e, o_s, o_e = [float(i) for i in inputs] # just in case, floatify everything!
    
    scale = (o_e - o_s)/(i_e - i_s)

    return o_s + ((v - i_s) * scale)

def remap_all(vals, i_s, i_e, o_s, o_e):
    '''
    run remap_interval on all vals
    '''
    return [remap_interval(v, i_s, i_e, o_s, o_e) for v in vals]

if __name__ == '__main__':
    # aliases
    build = build_random_function
    ev = evaluate_random_function
    remap = remap_all

    # image size
    size = 350, 350

    # new image
    image = Image.new("output", size)

    randoms = [build(5, 8) for _ in range(3)]

    # iterate through all xs and ys
    for i in range(size):
        for j in range(size):
            x, y = remap([i, j], 0., size, -1, 1)
            r, g, b = remap([ev(r, x, y) for r in randoms], -1., 1, 0, 255)
            image[x, y] = (r, g, b)

    image.save()
    image.show()
