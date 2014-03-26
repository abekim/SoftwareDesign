"""

Examples with inheritance and class structures

author: @abekim

"""

# we only allow access to Charge class (Point class becomes a private class!)
from charge import Charge

class Proton(Charge):
    ''' Proton is a Charge with positive charge type '''
    def __init__(self, strength=10):
        super(Proton, self).__init__("positive", strength)

class Electron(Charge):
    ''' Electron is a Charge with negative charge type '''
    def __init__(self, strength=10):
        super(Electron, self).__init__("negative", strength)

class Neutron(Charge):
    ''' Neutron is a Charge with neutral charge type '''
    def __init__(self, strength=10):
        super(Neutron, self).__init__("neutral", strength)

if __name__ == '__main__':
    p = Proton(100)
    print p
    print p.get_coordinates()
    print p.get_type()

