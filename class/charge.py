class Charge(object):
    def __init__(self, t, str=10):
        self.str = str
        self.t = t
    def get_type(self):
        return self.t
    def get_str(self):
        return self.str