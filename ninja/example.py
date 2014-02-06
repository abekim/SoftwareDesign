'''
Some examples of common malpractices in Python programming

author: @abekim
'''

# misuse of main script
def do_something():
  print "I'm doing something"

do_something()

'''
---------------------------------------------------------------------
## Main script

When writing Python modules, instead of writing scripts to test your functions,
place them in the main block of the module. 

The block of code in the main script will only be run when someone specifically 
runs the Python file directly (ie. from terminal or by using "Run"/"Build" commands on IDE):

# from script
`python example.py`

Any script outside of the main script gets run every time you import the module.
In this specific example, if I import the module from Python in script mode, it'll
print "I'm doing something" because of the script on line 11.

  >>> import example
  I'm doing something

-----------------------------------------------------------------------
## Documentation

You always hear people telling you to document your code, but what does that actually mean? 
What does it entail?

The purpose of documentation is simple: anyone with basic understanding of the language
you're using should be able to read through your code and understand what each line is doing.

Deciding whether someone could understand your code or not is very subjective, but when in doubt,
just put a simple quote/comment to let the readers know what's going on. I mean, it couldn't hurt
to be more informative.

Standard practice is to write a description for every class and their methods, functions, and 
ambiguous lines. Look through the example code below for a simple example
'''
def average(li):
  '''
  finds the average of all values in list `li`
  '''
  # get the sum of the list and divide by the number of elements in the list
  try:
    return sum(li) / len(li)
  except TypeError: # catch TypeError when sum(li) doesn't work
    raise Exception("Elements of list not numbers")

# main script
if __name__ == '__main__':
  # block of code
  print 'Running main script'