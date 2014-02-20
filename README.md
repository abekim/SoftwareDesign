SoftwareDesign
==============

The base repository for Olin College's Software Design Spring 2014

### Python tips/notes
-----------------
Python is a super interesting language and there are a lot of neat tricks that you could utilize and new conventions that you should follow when coding in Python. I'll record them on here as the semester goes on / I remember them.

#### Naming
Python doesn't like [CamelCase](http://en.wikipedia.org/wiki/Camelcase). A lot of the functions and methods are written out as `function_that_does_something`. As with any other conventions, it's a standard, so use it.

#### Ternary Notation
There are many ternary notations for various programming languages. Ternary notations are a simpler way of writing your `if...else` statements. Python has a very unique, pythonic ternary notation. In other languages, like JS or Java, the syntax is: 

```
boolean ? expression1 : expression2
```

where `boolean` is the conditional and `expression1` and `expression2` are what gets returned if `boolean` is `True` or `False`, respectively.

In Python, it's written as:

```
expression1 if boolean else expression2
```

I find them to be extremely useful when using lambda functions, which don't support multilines. (Read about [why lambda functions don't support multilines](http://stackoverflow.com/a/1233509))

#### Future Implementation

List Comprehension, String Formatting, Dictionaries, Lambda Functions (Anonymous functions), Ternary Notation, Module Structure

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
