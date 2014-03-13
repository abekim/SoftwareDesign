'''
Mid-term Exam
03/13/2014

author: @abekim
'''
def sum_squares_even(n):
    ''' returns the sum of the squares of all even numbers between 0 and n (inclusive) '''
    return sum([i**2 for i in range(n+1) if not i % 2])

def pair_list_to_dictionary(li):
    ''' returns a dictionary that maps elements of even indices to elements of odd indices '''
    keys = [li[i] for i in range(len(li)) if not i % 2]
    values = [li[i] for i in range(len(li)) if i % 2]
    return dict(zip(keys, values))

def split_dictionary(d):
    ''' returns a list that splits d in to keys that start with upper letters and keys that start with lower letters '''
    res = [{}, {}]
    for key in d:
        try:
            if key[0].islower(): res[1][key] = d[key]
            else: res[0][key] = d[key]
        except TypeError:
            raise Exception("key: %s is not a string" % key)
    return res

def pull_middle(s):
    ''' returns the middle two letters of s and s without the two letters '''
    if len(s) == 2: return s, ''
    head = s[:len(s)/2]
    tail = s[len(s)/2:]
    return head[-1] + tail[0], head[:-1] + tail[1:]

def in_language(s):
    ''' returns True iff s begins with some combination of 'a's, followed by equal number of 'b's, with no extra letters '''
    # base cases
    if not len(s): return True
    elif len(s) % 2 : return False

    middle, outer = pull_middle(s)
    return middle == 'ab' and in_language(outer)

class NucleotidePairs(object):
    def __init__(self):
        self.pairs = {
            'A': 'T',
            'C': 'G',
            'G': 'C',
            'T': 'A'
        }

    def get_complement(self, nuc):
        try:
            return self.pairs[nuc]
        except KeyError:
            raise Exception("%s not in list of known nucleotides" % nuc)

class DNASequence(object):
    ''' Represents a sequence of DNA '''
    def __init__(self, nucleotides):
        '''
            contructs a DNASequence with the specified nucleotides.
            nucleotides: the nucleotides represented as a string of
                         capital letters in {'A', 'C', 'G', 'T'}
        '''
        self.nucleotides = nucleotides.upper()
        self.pairs = NucleotidePairs()

    def get_reverse_complement(self):
        '''
            computes the reverse complement of the DNA sequence.
            returns: the reverse complement DNA sequence represented
                     as an object of type DNASequence
        '''
        return ''.join([self.pairs.get_complement(n) for n in self.nucleotides])

    def get_proportion_ACGT(self):
        '''
            computes the proportion of nucleotides in the DNA sequence
            that are 'A', 'C', 'G', 'T'
            returns: a dictionary where each key is a nucleotide and the 
                     corresponding value is the proportion of nucleotides in the
                     DNA sequence that are that nucleotide
        '''
        proportions = {
            'A': 0.,
            'C': 0.,
            'G': 0.,
            'T': 0.
        }
        length = len(self.nucleotides)
        
        for n in self.nucleotides:
            proportions[n] += 1./length

        return proportions

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class FunctionTestCases(unittest.TestCase):
    def setUp(self):
        pass

    def test_sum_squares_even(self):
        self.assertEqual(sum_squares_even(10), 220)
        self.assertEqual(sum_squares_even(5), 20)
        self.assertEqual(sum_squares_even(20), 1540)

    def test_pair_list_to_dictionary(self):
        self.assertEqual(pair_list_to_dictionary([1, 'a', 5]), {1:'a'})
        self.assertEqual(pair_list_to_dictionary(['hello', 'a', 'test', 'b']), {'hello':'a', 'test':'b'})
        self.assertEqual(pair_list_to_dictionary([1, 2, 'a', 'b', 2., 3., 4.]), {'a': 'b', 1: 2, 2.0: 3.0})

    def test_split_dictionary(self):
        self.assertEqual(split_dictionary({'a':2, 'B':'hello', 'c':'t'}),[{'B': 'hello'}, {'a': 2, 'c': 't'}])
        self.assertEqual(split_dictionary({'Abc':1, 'D':2, 'EFG':3}), [{'Abc':1, 'D':2, 'EFG':3}, {}])
        self.assertEqual(split_dictionary({'A':1, 'bc': 2, 'def': 3}), [{'A':1}, {'bc': 2, 'def': 3}])

    def test_pull_middle(self):
        try:
            self.assertEqual(pull_middle('ab'), ('ab', ''))
            self.assertEqual(pull_middle('aaaabbbb'), ('ab', 'aaabbb'))
        except NameError:
            pass

    def test_in_language(self):
        self.assertFalse(in_language('aaab'))
        self.assertFalse(in_language('aaaccc'))
        self.assertTrue(in_language(''))
        self.assertTrue(in_language('aaaabbbb'))
        self.assertFalse(in_language('abcdef'))
        self.assertFalse(in_language('aaabbbb'))
        self.assertTrue(in_language('aaaaaaaabbbbbbbb'))

class DNATestCases(unittest.TestCase):
    def setUp(self):
        self.sequence = DNASequence('atcgggatgctagag')

    def test_reverse_complement(self):
        self.assertEqual(self.sequence.get_reverse_complement(), 'TAGCCCTACGATCTC')

    def test_proportion(self):
        proportions = self.sequence.get_proportion_ACGT()
        self.assertEqual(sum(proportions.values()), 1.)
        expected = [4./15, 2./15, 6./15, 3./15]
        expected = [round(e, 2) for e in expected]
        for value in proportions.values():
            self.assertIn(round(value, 2), expected)

if __name__ == '__main__':
    unittest.main()