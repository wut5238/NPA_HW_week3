import unittest
from router import *

class test_router(unittest.TestCase):
    def test_attribute(self):
        '''test all atribute in router.py'''
        self.assertTrue(self.__init__)
if __name__ == '__main__':
    unittest.main()
