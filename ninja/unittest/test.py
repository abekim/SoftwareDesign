'''
Test for complicated module

author: @abekim
'''

try:
    import unittest2 as unittest2
except ImportError: 
    import unittest

from complicated import *

class ComplicatedTestCases(unittest.TestCase):
    def setUp(self):
        ''' 
            Unittest runs a setup method to initialize all test environment.
            It runs it before every test, making it easier for all of us to not 
            have to worry about resetting to initial test environment.
        '''
        testable_complicated_objects = [Complicated('CO' + str(i), wut=str(Weird(i)), swag_attr="swag", id=i) for i in range(10)]

        # set up items to run tests on __whose expected outcomes we know__
        self.comps = testable_complicated_objects
        self.weirdo = Weird(id=0)

    def test_abe_awesomeness(self):
        '''
            This is a given test for all your unit tests. Just kidding.
        '''
        print 'Testing Abe\'s awesomeness'

        self.assertTrue('Abe is awesome')
        self.assertTrue('so are his ninjees')

    def test_complicated_function(self):
        print 'Testing super_complicated_function'
        
        # flag to check which random funky function ran in super_complicated_function
        flag = 1 # 1 if capitalize else 0

        response = super_complicated_function(self.comps)

        expected_capitalize = ['Co' + str(i) for i in range(10)]
        expected_reverse = [str(i) + 'OC' for i in range(10)]

        try:
            self.assertEquals(response, expected_capitalize)
        except AssertionError:
            self.assertEquals(response, expected_reverse)
            flag = 0

        print 'funky function: %s' % ('capitalize' if flag else 'reverse')

        # super_complicated_function utilizes the setters of Complicated objects. We should test for this functionality as well.

        names = [comp.name for comp in self.comps]

        if flag:
            self.assertEquals(sorted(names), sorted(expected_capitalize))
        else:
            self.assertEquals(sorted(names), sorted(expected_reverse))

    def test_more_complicated_function(self):
        print 'Testing more_complicated_function'

        response = more_complicated_function(self.comps[0])
        expected = {'name':"CO0", 'wut':str(self.weirdo), 'swag_attr':"swag", 'id':0}

        self.assertEquals(sorted(response.keys()), sorted(expected.keys()))
        self.assertEquals(sorted(response.values()), sorted(expected.values()))

if __name__ == '__main__':
    unittest.main()