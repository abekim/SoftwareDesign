"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

Updated and edited by: @abekim

"""

class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    def get_coordinates(self):
        return self.x, self.y

p = Point()
print p

class Animal(object):
    def __init__(self, t):
        self.t = t   # type of animal
    def get_type(self):
        return self.t

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        super(Cat, self).__init__("cat")
    def meow(self):
        return "meow"

cynthia = Cat("cynthia")
print cynthia.get_type()
print cynthia.meow()

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        super(Dog, self).__init__("dog")
    def bark(self):
        return "woof"

ponyo = Dog("ponyo")
print ponyo.get_type()
print ponyo.bark()
# print ponyo.meow()

from charge import Charge

class Proton(Charge):
    def __init__(self, str):
        self.str = str
        self.t = "+"

c = Charge("+")
print c.get_type(), c.get_str()

p = Proton(100)
print p.get_type(), p.get_str()

def print_point(p):
    """Print a Point object in human-readable format."""
    print '(%g, %g)' % (p.x, p.y)

def distance_between_points(p1, p2):
    """Finds the distance between two points, p1 and p2."""
    x1, y1 = p1.get_coordinates()
    x2, y2 = p2.get_coordinates()
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """
    def __init__(self, corner=Point(), width=10.0, height=10.0):
        self.corner = corner
        self.width = width
        self.height = height
    def __str__(self):
        x, y = self.corner.get_coordinates()
        return 'A %g x %g rectangle with center at (%g, %g)' % (self.width, self.height, x, y)
    # getters
    def get_corner(self):
        return self.corner
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    # setters
    def set_corner(self, corner):
        self.corner = corner
    def set_width(self, w):
        self.width = w
    def set_height(self, h):
        self.height = h

def find_center(rect):
    """Returns a Point at the center of a Rectangle."""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

# WRONG WAY TO DO IT
def move_rectangle(rect, dx, dy):
    corner = rect.get_corner()
    x, y = corner.get_coordinates()
    corner.x, corner.y = (x+dx, y+dy)

# Better way to do it
def move_rectangle(rect, dx, dy):
    corner = rect.get_corner()
    x, y = corner.get_coordinates()
    rect.set_corner(Point(x+dx, y+dy))

def grow_rectangle(rect, dwidth, dheight):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.set_width(rect.get_width() + dwidth)
    rect.set_height(rect.get_height() + dheight)

# NEVER PROGRAM LIKE THIS
def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print 'blank',
    print_point(blank)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print 'center',
    print_point(center)

    print box.width
    print box.height
    print 'grow'
    grow_rectangle(box, 50, 100)
    print box.width
    print box.height


if __name__ == '__main__':
    p = Point()
    rect = Rectangle(p, 100.0, 200.0)
    print rect
    move_rectangle(rect, 10, 10)
    print rect

