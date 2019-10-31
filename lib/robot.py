import random
class Robot:
    def __init__(self, robot_string, map):
        self.robot_string = robot_string
        self.robot_on_map = map.name
        self.robot_position = self.set_robot_init_position(map)
        self.robot_possible_positions = [" ",".","U"]
        self.robot_position_win = "U"

    def set_robot_init_position(self, map):
        initial_position_nok = True
        while initial_position_nok:
            self.x = random.randint(0, map.x_max)
            self.y = random.randint(0, map.y_max)
            if map.map_list[self.x][self.y] in self.robot_possible_positions and map.map_list[self.x][self.y] != "U":
                initial_position_nok = False
        return self.x, self.y

    def place_robot_on_map(self):
        pass

    def move_robot(self):
        pass

