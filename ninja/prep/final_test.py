'''
Unittest for finals prep

author: @abekim
'''

try:
  import unittest2 as unittest
except ImportError:
  import unittest

from final import *

class FunctionTestCases(unittest.TestCase):
  def setUp(self):
    pass

  def test_sum_of_primes(self):
    self.assertEquals(sp(20), 77)
    self.assertEquals(sp(40), 197)
    self.assertEquals(sp(100), 1060)

  def test_first_no_repeat(self):
    self.assertFalse(nr('aaaaaaa'))
    self.assertEquals(nr('abcdeefgdbacf'), 'g')

  def test_nest_depth(self):
    self.assertEquals(nd([0, [1], 0, [1, [2, [3], 2], 1]]), 3)
    self.assertEquals(nd([0,0,[1],0,[1,[2,[3,[4,[5]]]]]]), 5)

if __name__ == '__main__':
  unittest.main()
