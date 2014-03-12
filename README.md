SoftwareDesign
==============
The base repository for Olin College's Software Design Spring 2014

### Best Git Practices
--------------
While there are many other Git practices out there, there is one that I found works exceptionally well with most others I've worked with. There are only a handful of things that really matter when using Git to make sure nothing breaks.

I will continue to update this as I come across good Git practices. 

#### Basic Git
- Commit a lot, push once. Git's `commit` tool is like `ctrl+s` / `command+s` on any text editor. Git won't have any of your changes if you don't commit them. Having said that, it's nice to have logical commits, but it's secondary to making sure your important changes aren't discarded.
```
> git commit -m "A short description of what changes were made with this commit"
```  
- Always and only work on separate branches. Never make changes directly on the master branch.
- Once you've commited your final changes, push your changes to GitHub. Your changes will only reflect on your local repo if you never push your changes. When pushing, always specify to which branch you're pushing your changes. For example, if I'm on branch `my_branch`, run:  
```
> git push origin my_branch
```  

#### Branching
Here's an outline of what works really well when branching: I use specific terms, but I'm not sure if they're the standard, so here's a simple scenario that covers all the terms I use when describing best Git practices:

If I'm on branch `orig_branch` and I created a new branch `new_branch` while I was on `orig_branch`, `orig_branch` is what I call the "parent branch", and `new_branch` is what I call the "child branch".

- Always have a very clear understanding of what your parent branch is. One great way to enforce this is to make sure that when you're making a new branch, you either:
```
> git checkout parent_branch  
> git checkout -b child_branch
```  
OR  
```
> git fetch origin
> git checkout -b child_branch origin/parent_branch
```
- When you first start working, always run `git pull origin <branch_name>`, where `<branch_name>` is the name of the parent branch.
- Only merge back to the parent branch. If on a team with multiple developers, always merge via pull requests, and that should be a PR that compares the child branch to the parent branch. Here's how I merge a child branch `new_branch` to its parents `orig_branch`:
```
> git checkout orig_branch  
> git merge origin/new_branch  
> git push origin orig_branch
```  
The only time I'll ever get a merge conflict is if I didn't follow the previous advice. Otherwise, `new_branch` should already have any new changes made to `orig_branch`.

- Once it's merged, _**DON'T TOUCH IT**_. If, for some God-forsaken reason, someone needs to make changes to the commit history of the parent branch (or any other changes that'll screw everyone else on children branches), do it when all children branches are merged back into the parent branch.

If you follow the above practices, you shouldn't ever run into unexpected merge conflicts. This, of course, doesn't mean you won't run into any. If you're making changes to the same file, you _are_ going to run into merge conflicts and they should be expected.

#### Resources

- [A successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/)
- [Branch naming conventions](http://stackoverflow.com/questions/273695/git-branch-naming-best-practices/6065944#6065944)


### Python tips/notes (and other general coding practices)
--------------

Python is a super interesting language and there are a lot of neat tricks that you could utilize and new conventions that you should follow when coding in Python. I'll record them on here as the semester goes on / I remember them.

#### Naming
Python doesn't like [CamelCase](http://en.wikipedia.org/wiki/Camelcase). A lot of the functions and methods are written out as `function_that_does_something`. As with any other conventions, it's a standard, so use it.

_**Deprecated.**_ Apparently, this isn't true, and I'm embarrassed.

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

##### A simple example
This should print `1`:
```
print 1 if True else 2
```
Had it been written as
```
print 1 if False else 2
```
it'll print `2`.

I find them to be extremely useful when using lambda functions and basic list functions (`map`, `filter`, and `reduce`), which don't support multilines. (Read about [why lambda functions don't support multilines](http://stackoverflow.com/a/1233509))

#### String Formatting
Python, along with many other great programming languages (like JS) has something called String Formatting. It lets users include variables into strings. I'm sure there are better explanations of this in the internet, but I think the examples will make it self-explanatory.

You could (and should) learn more about basic string formatting operation and the various conversion types in the [Python documentation](http://docs.python.org/2/library/stdtypes.html#string-formatting).

##### A Simple Example
The following script will print `"My name is Abe."`
```
name = "Abe"

print "My name is %s." % name 
```

String formatting is very useful for writing `__str__` (and sometimes `__repr__`) methods in classes. The purpose of the `__str__` method in a class is to make the object readable, and that might involve stringifying some of the object's attributes. (Side note: read more about the [difference between `__str__` and `__repr__` methods in a class](http://stackoverflow.com/a/2626364).)

Look at this `Animal` class as an example.
```
class Animal(object):
    def __init__(self, t, noise):
        self.t = t          # type of animal
        self.noise = noise  # noise this animal type makes
    def __str__(self):
        return "Animal of type %s that makes %s noise" % (self.t, self.noise)
```
My Dog animal object would look like
```
myDog = Animal("dog", "woof")
```
and `print myDog` would print out `"Animal of type dog that makes woof noise"`.

#### Future Implementation

List Comprehension, Dictionaries, Lambda Functions (Anonymous functions), Module Structure

### Few notes on HW4
--------------
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
