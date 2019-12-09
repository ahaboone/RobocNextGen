import unittest
from lib.robot import *
from lib.map import *


class RobotTest(unittest.TestCase):
    def setUp(self):
        self.test_map = Map("easy")
        self.test_robot = Robot("X", self.test_map)

    def test_robot_str_len(self):
        self.assertEqual(len(self.test_robot.string), 1, " Should be 1")

    def test_init_position_len(self):
        self.assertEqual(len(self.test_robot.position), 2, " Should be a list of size 2")

    def test_check_robot_movement(self):
        self.assertIn(self.test_robot.check_robot_movement(self.test_map, (5, 5)), [True, False],
                      "Returned value should be a boolean")

    def test_check_parse_move(self):
        self.assertEqual(len(self.test_robot.parse_move("e5")), 2)

    def test_check_move_robot(self):
        self.assertIn(self.test_robot.check_robot_movement(self.test_map, (5, 5)), [True, False],
                      "Returned value should be a boolean")


if __name__ == "__main__":
    unittest.main()
