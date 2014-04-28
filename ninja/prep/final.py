'''
Helping students study for the final

author: @abekim
'''
# sum of all primes up to n (non-inclusive)
def sum_of_primes(n):
  '''
  returns the sum of all primes up to n
  '''
  def is_prime(x):
    ''' returns true if x is prime '''
    # edge cases
    if x == 2: 
      return True
    elif x == 1 or not x % 2: 
      return False

    # all others
    for i in range(3, x, 2):
      if not x % i:
        return False
    return True
  
  return sum([i for i in range(n) if is_prime(i)])

# first non-recurring character
def first_no_repeat(s):
  '''
  Returns the first character in s that's not repeated.
  If all characters are repeated, return None
  '''
  from sets import Set

  checked = Set()
  
  for i in range(len(s)):
    if not s[i] in s[i+1:] and s[i] not in checked:
      return s[i]
    checked.add(s[i])
  
  return None

# depth of nested list
def nest_depth(li):
  '''
  return the depth of list `li`
  no nested lists are considered to have a depth of 0

  hint: think recursively
  '''
  if not True in [isinstance(elem, list) for elem in li]:
    return 0
  return 1 + max(map(lambda x: nest_depth(x) if isinstance(x, list) else 0, li))

# inheritance

# animal class
class Animal(object):
  ''' animal class '''
  def __init__(self, name, noise):
    self.name = name
    self.noise = noise
    self.hunger = 0.

  # abstract class meant to be overridden
  def make_noise(self):
    pass

  def eat(self):
    self.hunger /= 2
    print "new hunger level: %s" % self.hunger

# lion class
class Lion(Animal):
  ''' Lion '''
  def __init__(self, name, noise="ROAR!"):
    super(Lion, self).__init__(name, noise)

  # override make_noise method
  def make_noise(self):
    self.hunger += 0.2
    print self.noise

  # override hunger method to increment by 1/3
  def eat(self):
    self.hunger /= 3
    print "new hunger level: %s" % self.hunger

class Bear(Animal):
  ''' Bear '''
  def __init__(self, name, noise="roar?"):
    super(Bear, self).__init__(name, noise)

  # override make_noise method
  def make_noise(self):
    self.hunger += 0.3
    print self.noise

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
    self.food += amount

  def feed(self, animal):
    self.food -= 1
    animal.eat()

  def add_animal(self, animal):
    animal.make_noise()
    self.animals.append(animal)

  def remove_animal(self, animal):
    for i in range(len(self.animals)):
      if self.animals[i] == animal:
        del self.animals[i]
    print '%s removed from zoo' % animal.name

# aliases
sp = sum_of_primes
nr = first_no_repeat
nd = nest_depth

if __name__ == '__main__':
  # simulate zoo

  simba = Lion('Simba', 'I am the king of the jungle')
  pooh = Bear('Pooh', 'plush')

  abes_zoo = Zoo()
  abes_zoo.add_animal(simba)
  abes_zoo.add_animal(pooh)

  abes_zoo.feed(simba)

