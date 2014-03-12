'''
Quiz 4

author: @abekim

## Dictionaries

Write a Python function called `exclusive_or_dict` that takes 
two dictionaries (`d1` and `d2`) as input and returns a new dictionary 
that contains all key-value pairs from both `d1` and `d2` except those
where the corresponding key occurs in both dictionaries.
'''

try:
    import unittest2 as unittest
except ImportError:
    import unittest

# test cases for TDD!
class Test(unittest.TestCase):
    def test_find_dups(self):
        response = find_dups([1,2,3,1,2,3,4,5,6])
        self.assertEquals(response, [1,2,3])

    def test_exclusive_or_dict(self):
        d1 = {'a':5, 'b':3}
        d2 = {'a':3, 'c':7}

        response = exclusive_or_dict(d1, d2)
        self.assertEquals(response, {'b':3, 'c':7})

def find_dups(li):
    """ Returns all duplicate entries in list li """
    res = []
    for i in range(len(li)):
        if li[i] in li[i+1:]:
            res.append(li[i])
    return res

def exclusive_or_dict(d1, d2):
    """ Returns all key-value pairs from both d1 and d2 except ones in both dictionaries """
    res = {}
    remove = find_dups(d1.keys() + d2.keys())

    # search for non-duplicate keys
    keys = [key for key in d1.keys() + d2.keys() if not key in remove]
    
    # append key, val to res
    for key in keys:
        try:
            res[key] = d1[key]
        except KeyError:
            res[key] = d2[key]
    
    return res

if __name__ == '__main__':
    unittest.main()