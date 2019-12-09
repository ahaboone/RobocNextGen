import unittest

from lib.map import *


class Test_map(unittest.TestCase):
    def setUp(self):
        self.test_map = Map("easy")
        self.test_position = (5, 5)

    def test_map_discrepancies(self):
        for line in self.test_map.map_list:
            self.assertEqual(line[-1], "\n", "Line should end with a new line char")
            self.assertEqual(len(line), (self.test_map.x_max + 2), "All maps lines should have the same size: "
                             + str(self.test_map.x_max))

    def test_check_door(self):
        self.assertIn(self.test_map.check_door(self.test_position), [True, False],
                      " Returned value should be a boolean")

    def test_check_wall(self):
        self.assertIn(self.test_map.check_wall(self.test_position), [True, False],
                      " Returned value should be a boolean")

