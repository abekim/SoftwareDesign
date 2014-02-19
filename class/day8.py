from swampy.TurtleWorld import *

def snow_flake_side(turtle, l, level=0):
  """ Draw a side of the snowflake curve with side length l and recursion depth of level """
  if not level:
    fd(turtle, l)
    turtle.lt(60)
    fd(turtle, l)
    turtle.rt(120)
    fd(turtle, l)
    turtle.lt(60)
    fd(turtle,l)
  else:
    snow_flake_side(turtle,l/3,level-1)
    turtle.lt(60)
    snow_flake_side(turtle,l/3,level-1)
    turtle.rt(120)
    snow_flake_side(turtle,l/3,level-1)
    turtle.lt(60)
    snow_flake_side(turtle,l/3,level-1)
 
def snowflake(turtle,l):
  for i in range(3):
    snow_flake_side(turtle,l,3)
    rt(turtle,120)

def recursive_tree(turtle, branch_length, level=0):
  """ Draw a tree with branch length branch_length and recursion depth of level """
  if not level:
    fd(turtle, branch_length)
  else:
    fd(turtle, branch_length)
    
    # clone turtle
    t = Turtle()
    t.x, t.y, t.heading = turtle.x, turtle.y, turtle.heading

    t.lt(30)
    recursive_tree(t, branch_length*.6, level-1)
    t.undraw()

    bk(turtle, branch_length/3.0)

    # reclone turtle
    t2 = Turtle()
    t2.x, t2.y, t2.heading = turtle.x, turtle.y, turtle.heading

    t2.rt(40)
    recursive_tree(t2, branch_length*.64, level-1)
    t2.undraw()

    bob.undraw()

if __name__ == '__main__':
  print 'running main script'

  world = TurtleWorld()
  bob = Turtle()

  bob.set_delay(0)
  bob.x = -100
  # bob.y = -100

  print "Bob's current dirs: \n", dir(bob)

  # snowflake
  snowflake(bob, 100)

  # bob.heading = 90
  # recursive_tree(bob, 100, 10)

  wait_for_user()