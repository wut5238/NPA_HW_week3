import unittest
from router import *


class test_router(unittest.TestCase):
    def test_add_inf(self):
        '''test method use to add interaces to router'''
        r1 = Router('Cisco', 'IOSv', "R1")
        r1.add_inf("GigabitEthernet 0/1")
        self.assertTrue([]!= r1.interfaces)

if __name__ == '__main__':
    unittest.main()
