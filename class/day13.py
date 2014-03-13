'''
Day 13 - Midterm Prep

author: @abekim
'''

mem = {
    'ack': {
    },
    'fact': {
        0.:1.
    }
}

# Ackermann
def ack(m, n):
    ''' evalues the Ackermann number of m and n '''
    global mem

    if m < 0 or n < 0: raise Exception("m or n cannot be negative.")
    try:
        return mem['ack'][m][n]
    except KeyError:
        if not m in mem['ack']:
            mem['ack'][m] = {}
        if not m:
            mem['ack'][m][n] = n+1
            return n+1
        elif not n: 
            mem['ack'][m][n] = ack(m-1, 1)
            return mem['ack'][m][n]
        mem['ack'][m][n] = ack(m-1, ack(m, n-1))
        return mem['ack'][m][n]

def fact(n):
    ''' returns the factorial of n '''
    global mem

    try:
        return mem['fact'][n]
    except KeyError:
        mem['fact'][n] = n * fact(n-1)
        return mem['fact'][n]

def estimate_pi():
    ''' estimates the value of pi using Srinivasa Ramanujan's infinite series '''
    res = 0
    coef = 2.*(2**.5)*(1./9801)
    k = 0
    while True:
        den = (fact(k)**4)*(396**(4*k))
        num = fact(4*k)*(1103 + 26490*k)
        res += coef * num/den

        if (coef * num/den) < 10**-15: break
        k += 1
    return 1/res

def rotate_word(s, n):
    ''' rotates the word s by n using ROTn encryption method '''
    rotated = ''
    start = ord('a')
    
    for c in s:
        # flag to check if c is in upper case
        upper = False
        if c.isupper():
            upper = True
            c = c.lower()

        rotatedBy = ((ord(c) + n) - start) % 26
        rotatedChar = chr(start + rotatedBy)

        rotated += rotatedChar if not upper else rotatedChar.upper()
    return rotated

def flatten(li):
    ''' flattens li by one layer '''
    res = []

    for elem in li:
        try:
            res += elem
        except TypeError:
            res.append(elem)

    return res

def has_double(word):
    ''' checks if word has double letter '''
    if len(word) <= 1: return False
    for n in range(len(word)-1):
        if word[n] == word[n+1]: return True
    return False

def double_letters(path="words.txt"):
    ''' 
        scans through file in path and returns a dictionary 
        that maps all words with at least one double letter
    '''
    with open(path, 'rb') as f:
        duplicates = [(word, len(word)) for word in f if has_double(word)]
        return dict(duplicates)

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class FunctionalTestCases(unittest.TestCase):
    def setUp(self):
        pass

    def test_ackermann(self):
        tests = [ack(0, n) for n in range(3)]
        self.assertEqual(tests[0], 1)
        self.assertEqual(tests[1], 2)
        self.assertEqual(tests[2], 3)
        tests = [ack(m, 0) for m in range(3)]
        self.assertEqual(tests[0], 1)
        self.assertEqual(tests[1], 2)
        self.assertEqual(tests[2], 3)

    def test_factorial(self):
        import math
        test = [fact(n) for n in range(5)]
        expected = [math.factorial(n) for n in range(5)]
        map(lambda n: self.assertEqual(test[n], expected[n]), range(5))

    def test_pi_estimate(self):
        import math
        e_pi = estimate_pi()
        n = 0
        while True:
            if (round(e_pi, n) == round(math.pi, n)):
                try:
                    self.assertEqual(round(e_pi, n+1), round(math.pi, n+1))
                    n += 1
                except AssertionError:
                    print 'Our estimation of pi is accurate up to %i decimal places!' % n
                    break

    def test_brotate_word(self):
        self.assertEqual(rotate_word('Melon', -10), 'Cubed')
        self.assertEqual(rotate_word('cheer', 7), 'jolly')

    def test_flatten(self):
        self.assertEqual(flatten([1,2,3]), [1,2,3])
        self.assertEqual(flatten([1,[2,5],3]), [1,2,5,3])
        self.assertEqual(flatten([1,[2,[4,5]],3]), [1,2,[4,5],3])

    def test_has_double(self):
        self.assertFalse(has_double('a'))
        self.assertTrue(has_double('aa'))
        self.assertTrue(has_double('wdfkuhwglkjdfaa'))

if __name__ == '__main__':
    # print double_letters()

    unittest.main()
