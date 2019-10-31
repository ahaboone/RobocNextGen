import random
class Robot:
    def __init__(self, robot_string, map):
        self.string = robot_string
        self.on_map = map.name
        self.possible_positions = [" ",".","U"]
        self.position = self.set_robot_init_position(map)

    def set_robot_init_position(self, map):
        initial_position_nok = True
        while initial_position_nok:
            self.x = random.randint(0, map.x_max)
            self.y = random.randint(0, map.y_max)
            print(self.x, self.y)
            print(map.map_list[self.y][self.x])
            if map.map_list[self.y][self.x] in self.possible_positions and map.map_list[self.y][self.x] != "U":
                initial_position_nok = False
        return self.x, self.y

    def place_robot_on_map(self):
        pass

    def move_robot(self):
        pass

