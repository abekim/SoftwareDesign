# Object Oriented Programming

## Inheritance
--------------

Inheritance refers to a class (or classes) whose implementations are based on a "base" class. Some major reasons for using inheritance is for code reuse and structuring the code (hierarchy).

#### Code Reuse

Consider a program that simulates a pet store. We could simply make a class for all different types of animals at the store and give each class its methods. 
```
class Dog:
    ''' Dog class with dog methods '''

class Cat:
    ''' Cat class with cat methods ''' 
```
However, as animals, pets have similar behaviors, like `eat`, `make_noise`, etc. In our current model, we have to define each of these methods multiple times for each class we create. If you need to make changes to the `eat` method, you have to revisit each class and change each `eat` method.

The better way to implement this is to utilize a "base", or "parent", class and have each pet class inherit from it:
```
class Animal:
    ''' Base Animal class with basic methods shared by all animals '''

class Dog(Animal):
    ''' Dog that inherits from Animal '''

class Cat(Animal):
    ''' Cat that inherits from Animal '''
```
Now if we have to make changes to the `eat` method, we only need to change it once in the Animal class. This is the code reuse factor of inheritance. Look at <a href="animal.py" target="_blank">`animal.py`</a> for how inheritance is implemented in Python.

#### Code Hierarchy

By inheriting from the `Animal` class, we've inherently given our program a hierarchical structure. `Animal` is the base class while `Dog` and `Cat` are __subclasses__ of the base class. There is a number of reason why someone would want to provide structure to their architecture, but we're only going to cover on example of it: use of private classes.

Say you want to publicly release your pet store program, and while you want people to be able to create new classes for various animal types, you don't want them to make any changes to the `Animal` class (because we made it super perfect). If someone modifies the `Animal` class, it'll affect all subclasses of `Animal` and it'll be worse than ours. One way to implement this is by separating your classes into different modules.

Look at <a href="charge.py" target="_blank">`charge.py`</a>. We defined a `Point` base class with a `Charge` subclass.

In <a href="subatomic.py" target="_blank">`subatomic.py`</a>, we define the subatomic particles, `Proton`, `Electron`, and `Neutron`, all subclasses of the `Charge` class. However, when we import from `charge.py`, we write:

```
from charge import Charge
```
This lets us import only the `Charge` class and leave the `Point` class alone. 