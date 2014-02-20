SoftwareDesign
==============

The base repository for Olin College's Software Design Spring 2014

### Python tips/notes
-----------------
Python is a super interesting language and there are a lot of neat tricks that you could utilize and new conventions that you should follow when coding in Python. I'll record them on here as the semester goes on / I remember them.

<<<<<<< HEAD
#### Naming
Python doesn't like [CamelCase](http://en.wikipedia.org/wiki/Camelcase). A lot of the functions and methods are written out as `function_that_does_something`.

#### Future Implementation

List Comprehension, String Formatting, Dictionaries, Lambda Functions (Anonymous functions), Ternary Notation, Module Structure
=======
##### Naming
Python doesn't like [CamelCase](http://en.wikipedia.org/wiki/Camelcase). A lot of the functions and methods are written out as `function_that_does_something`.

>>>>>>> beb843b... posted solution to hw4

### Few notes on HW4
-----------------
I think the more interesting problems in our lives involve having to step outside of our comfort zone, like looking at / thinking about something from a perspective we're not used to.

Homework 4 for Software Design does just that. It asks us to take a function, which are normally structured:
```
def my_function (arg1, arg2): 
    # body of function that does something
    return
```
and represent it using lists:
```
f = ['my_function', [ arg1 ], [ arg2 ]] # this is a function
```
And then be able to evaluate this function later.

While there are many ways to do this, I decided to map the string `my_function` to the function itself using dictionaries.
```
# map of all my functions!
functions = {
  'my_function': my_function
}
```
So later on, I can call the function by `functions['my_function'](arg1, arg2)`, which is equivalent to `my_function(arg1, arg2)`.

Another way I've seen done is just call different functions using pattern matching practices, which are generally implemented as `if...else` statements in Python.
```
# given f from above...
if f[0] == 'my_function':
  return my_function( ... ) # run my_function on arg1 and arg2
elif f[0] == 'different_function':
  return different_function( ... ) 
...
```
Both ways work, and it's really interesting to think about and explore these different ways to both represent and evaluate functions.
