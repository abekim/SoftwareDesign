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
    "x": {
        "fn": lambda x: x,
        "arg": 0
        },
    "y": {
        "fn": lambda y: y,
        "arg": 0
        },
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
<<<<<<< HEAD
<<<<<<< HEAD
    "cube": {
        "fn": lambda x: x**3,
        "arg": 1
=======
    # "cube": {
    #     "fn": lambda x: x**3,
    #     "arg": 1
    #     },
    "x": {
        "fn": lambda x: x,
        "arg": 0
        },
    "y": {
        "fn": lambda y: y,
        "arg": 0
>>>>>>> 6ac5ec9... added images and finalized solution to hw4
=======
    "cube": {
        "fn": lambda x: x**3,
        "arg": 1
>>>>>>> 98131b0... updated readme with python tips
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
        if min_depth > 1:
            fnames = [key for key in fs.keys() if not key in ["x","y"]]
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
<<<<<<< HEAD

def to_int(vals):
    '''
    int-ifies all values in vals
    '''
    return [int(i) for i in vals]
=======
>>>>>>> beb843b... posted solution to hw4

def to_int(vals):
    '''
    int-ifies all values in vals
    '''
    return [int(i) for i in vals]

if __name__ == '__main__':
    # aliases
    build = build_random_function
    ev = evaluate_random_function
    remap = remap_all

    # image size
    size = 350, 350

    # new image
<<<<<<< HEAD
<<<<<<< HEAD
    image = Image.new("RGB", size)

    # copied the example from the website
    def avg(x,y): return (x+y)/2
    def blue(x, y): return avg(sin(pi * (avg(cos(pi * avg((cos(pi * (x * x)) * cos(pi * (x * y))), avg(avg((x * x), avg(y, y)), avg(cos(pi * y), cos(pi * x))))), avg(avg(avg((sin(pi * y) * (x * y)), sin(pi * (x * x))), avg(((x * x) * sin(pi * y)), (avg(x, x) * sin(pi * y)))), avg((cos(pi * sin(pi * y)) * cos(pi * avg(x, x))), sin(pi * avg(sin(pi * y), sin(pi * y)))))) * cos(pi * avg(avg(avg(sin(pi * (x * x)), avg(sin(pi * y), sin(pi * x))), cos(pi * avg(cos(pi * y), avg(y, x)))), (((avg(x, y) * cos(pi * x)) * cos(pi * avg(y, x))) * avg(cos(pi * (y * x)), ((x * x) * (y * x)))))))), avg(((((sin(pi * sin(pi * avg(x, x))) * avg(avg(sin(pi * y), sin(pi * y)), avg(avg(x, x), cos(pi * y)))) * sin(pi * sin(pi * sin(pi * (y * y))))) * avg(cos(pi * avg(avg(avg(x, y), (y * x)), cos(pi * sin(pi * x)))), (sin(pi * sin(pi * sin(pi * x))) * cos(pi * ((y * y) * cos(pi * x)))))) * avg(cos(pi * cos(pi * sin(pi * cos(pi * avg(x, y))))), (sin(pi * (cos(pi * avg(y, x)) * sin(pi * cos(pi * x)))) * ((sin(pi * cos(pi * y)) * avg(avg(x, x), cos(pi * x))) * avg((sin(pi * x) * avg(y, x)), sin(pi * sin(pi * x))))))), ((cos(pi * cos(pi * (sin(pi * (y * y)) * cos(pi * cos(pi * x))))) * avg(sin(pi * avg(cos(pi * sin(pi * y)), (cos(pi * x) * avg(x, x)))), cos(pi * cos(pi * cos(pi * avg(x, y)))))) * sin(pi * (avg((cos(pi * (y * y)) * cos(pi * sin(pi * y))), avg(((x * x) * sin(pi * x)), cos(pi * sin(pi * y)))) * avg(sin(pi * (avg(y, x) * avg(x, x))), cos(pi * avg((y * y), avg(y, y)))))))))
    def green(x,y): return sin(pi * ((avg(avg(cos(pi * (cos(pi * cos(pi * x)) * (cos(pi * x) * avg(y, x)))), ((cos(pi * cos(pi * y)) * (cos(pi * x) * (x * y))) * sin(pi * sin(pi * avg(y, y))))), cos(pi * (avg(sin(pi * sin(pi * x)), sin(pi * sin(pi * x))) * sin(pi * sin(pi * (x * y)))))) * avg((avg(cos(pi * sin(pi * cos(pi * x))), avg((sin(pi * x) * cos(pi * y)), avg(cos(pi * x), cos(pi * x)))) * avg(avg(sin(pi * cos(pi * x)), sin(pi * sin(pi * x))), (avg(cos(pi * x), avg(y, x)) * avg(sin(pi * y), sin(pi * x))))), (cos(pi * cos(pi * (avg(y, y) * (y * x)))) * cos(pi * cos(pi * sin(pi * avg(x, x))))))) * sin(pi * avg(avg(sin(pi * cos(pi * sin(pi * cos(pi * x)))), avg(sin(pi * cos(pi * cos(pi * y))), ((sin(pi * y) * (x * y)) * cos(pi * (y * y))))), cos(pi * avg(((cos(pi * y) * (y * y)) * avg(sin(pi * y), cos(pi * y))), (((x * x) * avg(y, x)) * cos(pi * sin(pi * x)))))))))
    def red(x,y): return sin(pi * avg((((cos(pi * (sin(pi * cos(pi * y)) * avg(avg(x, x), sin(pi * y)))) * avg(sin(pi * (sin(pi * y) * (y * x))), cos(pi * cos(pi * (y * y))))) * sin(pi * (sin(pi * (sin(pi * y) * sin(pi * y))) * cos(pi * ((y * y) * sin(pi * y)))))) * sin(pi * avg(cos(pi * avg(((y * x) * (x * x)), sin(pi * (y * x)))), sin(pi * avg(avg(sin(pi * x), avg(x, x)), sin(pi * avg(x, y))))))), cos(pi * cos(pi * avg(sin(pi * sin(pi * avg((x * x), (x * x)))), sin(pi * sin(pi * sin(pi * sin(pi * y)))))))))

    randoms = [build(randint(5, 10), randint(10, 15)) for _ in range(3)]

    # iterate through all xs and ys
    for i in range(size[0]):
        for j in range(size[1]):
            # assuming the image is a square...
            x, y = remap([i, j], 0., size[0], -1, 1)
            r, g, b = to_int(remap([ev(r, x, y) for r in randoms], -1., 1, 0, 255))
            image.putpixel((i, j), (r, g, b))

    image.save("output5.bmp")
=======
    image = Image.new("output", size)
=======
    image = Image.new("RGB", size)

<<<<<<< HEAD
    randoms = [build(1, randint(10, 20)) for _ in range(3)]
>>>>>>> 6ac5ec9... added images and finalized solution to hw4

=======
>>>>>>> 98131b0... updated readme with python tips
    # copied the example from the website
    def avg(x,y): return (x+y)/2
    def blue(x, y): return avg(sin(pi * (avg(cos(pi * avg((cos(pi * (x * x)) * cos(pi * (x * y))), avg(avg((x * x), avg(y, y)), avg(cos(pi * y), cos(pi * x))))), avg(avg(avg((sin(pi * y) * (x * y)), sin(pi * (x * x))), avg(((x * x) * sin(pi * y)), (avg(x, x) * sin(pi * y)))), avg((cos(pi * sin(pi * y)) * cos(pi * avg(x, x))), sin(pi * avg(sin(pi * y), sin(pi * y)))))) * cos(pi * avg(avg(avg(sin(pi * (x * x)), avg(sin(pi * y), sin(pi * x))), cos(pi * avg(cos(pi * y), avg(y, x)))), (((avg(x, y) * cos(pi * x)) * cos(pi * avg(y, x))) * avg(cos(pi * (y * x)), ((x * x) * (y * x)))))))), avg(((((sin(pi * sin(pi * avg(x, x))) * avg(avg(sin(pi * y), sin(pi * y)), avg(avg(x, x), cos(pi * y)))) * sin(pi * sin(pi * sin(pi * (y * y))))) * avg(cos(pi * avg(avg(avg(x, y), (y * x)), cos(pi * sin(pi * x)))), (sin(pi * sin(pi * sin(pi * x))) * cos(pi * ((y * y) * cos(pi * x)))))) * avg(cos(pi * cos(pi * sin(pi * cos(pi * avg(x, y))))), (sin(pi * (cos(pi * avg(y, x)) * sin(pi * cos(pi * x)))) * ((sin(pi * cos(pi * y)) * avg(avg(x, x), cos(pi * x))) * avg((sin(pi * x) * avg(y, x)), sin(pi * sin(pi * x))))))), ((cos(pi * cos(pi * (sin(pi * (y * y)) * cos(pi * cos(pi * x))))) * avg(sin(pi * avg(cos(pi * sin(pi * y)), (cos(pi * x) * avg(x, x)))), cos(pi * cos(pi * cos(pi * avg(x, y)))))) * sin(pi * (avg((cos(pi * (y * y)) * cos(pi * sin(pi * y))), avg(((x * x) * sin(pi * x)), cos(pi * sin(pi * y)))) * avg(sin(pi * (avg(y, x) * avg(x, x))), cos(pi * avg((y * y), avg(y, y)))))))))
    def green(x,y): return sin(pi * ((avg(avg(cos(pi * (cos(pi * cos(pi * x)) * (cos(pi * x) * avg(y, x)))), ((cos(pi * cos(pi * y)) * (cos(pi * x) * (x * y))) * sin(pi * sin(pi * avg(y, y))))), cos(pi * (avg(sin(pi * sin(pi * x)), sin(pi * sin(pi * x))) * sin(pi * sin(pi * (x * y)))))) * avg((avg(cos(pi * sin(pi * cos(pi * x))), avg((sin(pi * x) * cos(pi * y)), avg(cos(pi * x), cos(pi * x)))) * avg(avg(sin(pi * cos(pi * x)), sin(pi * sin(pi * x))), (avg(cos(pi * x), avg(y, x)) * avg(sin(pi * y), sin(pi * x))))), (cos(pi * cos(pi * (avg(y, y) * (y * x)))) * cos(pi * cos(pi * sin(pi * avg(x, x))))))) * sin(pi * avg(avg(sin(pi * cos(pi * sin(pi * cos(pi * x)))), avg(sin(pi * cos(pi * cos(pi * y))), ((sin(pi * y) * (x * y)) * cos(pi * (y * y))))), cos(pi * avg(((cos(pi * y) * (y * y)) * avg(sin(pi * y), cos(pi * y))), (((x * x) * avg(y, x)) * cos(pi * sin(pi * x)))))))))
    def red(x,y): return sin(pi * avg((((cos(pi * (sin(pi * cos(pi * y)) * avg(avg(x, x), sin(pi * y)))) * avg(sin(pi * (sin(pi * y) * (y * x))), cos(pi * cos(pi * (y * y))))) * sin(pi * (sin(pi * (sin(pi * y) * sin(pi * y))) * cos(pi * ((y * y) * sin(pi * y)))))) * sin(pi * avg(cos(pi * avg(((y * x) * (x * x)), sin(pi * (y * x)))), sin(pi * avg(avg(sin(pi * x), avg(x, x)), sin(pi * avg(x, y))))))), cos(pi * cos(pi * avg(sin(pi * sin(pi * avg((x * x), (x * x)))), sin(pi * sin(pi * sin(pi * sin(pi * y)))))))))

    randoms = [build(randint(5, 10), randint(10, 15)) for _ in range(3)]

    # iterate through all xs and ys
    for i in range(size[0]):
        for j in range(size[1]):
            # assuming the image is a square...
            x, y = remap([i, j], 0., size[0], -1, 1)
            r, g, b = to_int(remap([ev(r, x, y) for r in randoms], -1., 1, 0, 255))
            image.putpixel((i, j), (r, g, b))

<<<<<<< HEAD
<<<<<<< HEAD
    image.save()
>>>>>>> beb843b... posted solution to hw4
=======
    image.save("output.bmp")
>>>>>>> 6ac5ec9... added images and finalized solution to hw4
=======
    image.save("output8.bmp")
>>>>>>> 98131b0... updated readme with python tips
    image.show()
