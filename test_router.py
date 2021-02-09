import unittest
from router import *


class test_router(unittest.TestCase):
    def test_add_inf(self):
        '''test method use to add interaces to router'''
        r1 = Router('Cisco', 'IOSv', "R1")
        r1.add_inf("GigabitEthernet 0/1")
        self.assertTrue([]!= r1.interfaces)
    
    def test_connect(self):
        '''test method connect between interface of router'''
        r1 = Router('Cisco', 'IOSv', "R1")
        r1.add_inf("GigabitEthernet 0/1")
        r1.add_inf("GigabitEthernet 0/2")

        r2 = Router('Cisco', 'IOSv', "R2")
        r2.add_inf("GigabitEthernet 0/2")

        r1.connect("GigabitEthernet 0/1", r2, "GigabitEthernet 0/2")
        self.assertTrue({} != r2.connection)
        self.assertTrue(list(r2.connection.keys())[0] == "R1")

if __name__ == '__main__':
    unittest.main()
