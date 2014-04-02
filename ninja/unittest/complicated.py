
class Complicated(object):
    ''' super complicated object '''

    def __init__(self, name="ComplicatedObject", **kwargs):
        self.name = name
        self.indexes = ["name"] + kwargs.keys()
        
        # if keyword arguments are given, set each as an attribute of the object    
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                setattr(self, key, value)

    def __repr__(self):
        return "A super complicated object named %s with attributes: %s" % (self.name, self.indexes)

    def __str__(self):
        return self.__repr__()

    # getters
    def __get(self, attrname):
        ''' get an attribute '''
        try:
            return getattr(self, attrname)
        except AttributeError:
            raise Exception("No such attribute exists. Current attributes are:", self.indexes)

    def get_attr(self, attr):
        return self.__get(attr)


    def get_name(self):
        return self.name

    # setters
    def set_name(self, new_name):
        ''' set a new name ''' 
        self.name = new_name

class Weird(object):
    def __init__(self, id=0):
        self.id = 0

    def __repr__(self):
        return "I'm a really weired object whose ID is %d" % self.id

    def __str__(self):
        return self.__repr__()

def super_complicated_function(comps):
    ''' takes in a list of Complicated objects and returns the list of their names after doing funky things '''

    import random

    def capitalize(li):
        try:
            return map(lambda x: x.capitalize(), li)
        except NameError or SyntaxError:
            return li

    def reverse(li):
        try:
            return map(lambda x: x[::-1], li)
        except NameError or SyntaxError:
            return li

    map(lambda comp, new_name: comp.set_name(new_name), comps, random.choice([capitalize, reverse])([c.name for c in comps]))

    return [c.name for c in comps]

def more_complicated_function(comp):
    ''' takes in a complicated object and returns a dictionary of all its attributes '''
    return dict(zip(comp.indexes, [comp.get_attr(attr) for attr in comp.indexes]))

if __name__ == '__main__':
    comps = [Complicated("CO" + str(i), wut=str(Weird(i))) for i in range(10)]

    print super_complicated_function(comps)