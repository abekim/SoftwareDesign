
'''
We're gonna make Point a private class...
'''
class Point(object):
    """ Represents a point in 2-D space """
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)
    
    def __str__(self):
        ''' 
            String representation of a Point object 
            Coordinates are represented in integers
        '''
        return '(%i, %i)' % (self.x, self.y)

    def get_coordinates(self):
        ''' returns a tuple of its x and y coordinates '''
        return self.x, self.y

class Charge(Point):
    """ A point in 2-D space with a charge """
    def __init__(self, t, strength=10, x=0, y=0):
        ''' 
            A Charge object has:
                type of charge
                strength of charge (defaulted at 10)
                x and y coordinates (defaulted at (0,0))
        '''
        self.strength = strength
        self.t = t
        super(Charge, self).__init__(x, y)

    def __str__(self):
        ''' String representation of a Charge object '''
        x, y = self.get_coordinates()
        return 'A %s charge at (%i, %i) with strength %i' % (self.get_type().lower(), x, y, self.get_str())

    def get_type(self):
        ''' returns the type of charge '''
        return self.t
    
    def get_str(self):
        ''' returns the strength of charge '''
        return self.strength

if __name__ == '__main__':
    # new point at -1, 3
    p = Point(-1, 3)
    print p     # this is what __str__ does!
    print "Point p: %s" % p
    print p.get_coordinates()

    c = Charge('Negative')
    print "Charge c: %s" % c
    print c.get_str()