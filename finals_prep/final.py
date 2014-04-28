'''
Helping students study for the final

author: @abekim
'''
# sum of all primes up to n (non-inclusive)
def sum_of_primes(n):
  '''
  returns the sum of all primes up to n
  '''
  pass

# first non-recurring character
def first_no_repeat(s):
  '''
  Returns the first character in s that's not repeated.
  If all characters are repeated, return None
  '''
  pass

# depth of nested list
def nest_depth(li):
  '''
  return the depth of list `li`
  no nested lists are considered to have a depth of 0

  hint: think recursively
  '''
  pass

## INHERITANCE

'''
Implement the constructors for each class
'''
# animal class
class Animal(object):
  ''' animal class '''
  def __init__(self, name, noise):
    # implement something here
    pass

    # initialize a hunger factor
    self.hunger = 0.

  # abstract method meant to be overridden
  def make_noise(self):
    pass

  def eat(self):
    ''' eating will make its hunger decrease by half. '''
    # your implementation here
    print "new hunger level: %s" % self.hunger

# lion class
class Lion(Animal):
  ''' Lion '''
  def __init__(self, name, noise="ROAR!"):
    pass

  # override make_noise method
  def make_noise(self):
    '''
    make noise should increase hunger level by 0.2.
    also print the animal's noise afterwards
    '''
    pass

# bear class
class Bear(Animal):
  ''' Bear '''
  def __init__(self, name, noise="roar?"):
    pass

  # override make_noise method
  def make_noise(self):
    '''
    make noise should increase hunger level by 0.3.
    also print the animal's noise afterwards
    '''
    pass

# zoo class
class Zoo(object):
  ''' Zoo '''
  def __init__(self, animals=None, food=10):
    '''
    animals: animals in zoo
    food: supplies at zoo
    '''
    if not animals:
      self.animals = []
    self.food = food

  def resupply(self, amount=10):
    ''' increment food by amount '''
    pass

  def feed(self, animal):
    ''' decrement food by 1 and have the animal eat '''
    pass

  def add_animal(self, animal):
    ''' simple add method '''
    animal.make_noise()
    self.animals.append(animal)

  def remove_animal(self, animal):
    ''' a similar remove method '''
    for i in range(len(self.animals)):
      if self.animals[i] == animal:
        del self.animals[i]
    print '%s removed from zoo' % animal.name

if __name__ == '__main__':
  # simulate zoo

  simba = Lion('Simba', 'I am the king of the jungle')
  pooh = Bear('Pooh', 'plush')

  abes_zoo = Zoo()
  abes_zoo.add_animal(simba)
  abes_zoo.add_animal(pooh)

  abes_zoo.feed(simba)

