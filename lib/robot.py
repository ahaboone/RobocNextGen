import random
import math

class Robot:
    def __init__(self, robot_string, map):
        self.string = robot_string
        self.on_map = map.name
        self.possible_positions = [" ",".","U"]
        self.position = self.robot_init_position(map)

    def robot_init_position(self, map):
        initial_position_nok = True
        while initial_position_nok:
            x = random.randint(0, map.x_max)
            y = random.randint(0, map.y_max)
            # print(self.x, self.y)
            # print(map.map_list[self.y][self.x])
            if map.map_list[y][x] in self.possible_positions and map.map_list[y][x] != "U":
                initial_position_nok = False
        return [x, y]

    def check_robot_movement(self, map, position):
        sign = lambda x: (1, -1)[x < 0]
        victory = lambda x: (True, False)[x == "U"]

        movement_possible = True
        i = j = 1
        if position[0] > map.x_max or position[1] > map.y_max:
            print("out of map ranges.")
            movement_possible = False

        elif position[0] != self.position[0]:
            for i in range(1, abs(position[0] - self.position[0])+1):
                # if map.map_str[(map.x_max+2) * (position[1]) + sign(self.position[0] - position[0]) *i]
                # not in self.possible_positions:
                if map.map_list[self.position[1]][self.position[0]+sign(position[0] - self.position[0])*i] not in self.possible_positions:
                    # print("mouvement impossible")
                    movement_possible = False
                    break

        elif position[1] != self.position[1]:
            for i in range(1, abs(position[1] -  self.position[1])+1):
                # if map.map_str[(map.x_max+2) * (self.position[1] + sign(position[1] - self.position[1]) * i) +
                # self.position[0]] not in self.possible_positions:
                if map.map_list[self.position[1]+ sign(position[1] - self.position[1]) * i][self.position[0]] not in self.possible_positions:
                    # print("mouvement impossible")
                    movement_possible = False
                    break
        return movement_possible

    def place_n_display_robot_on_map(self, map):
        # map_line = list(map.map_list[self.position[1]])
        # map_line[self.position[0]] = self.string
        current_map = list(map.map_list)
        temp_line = current_map[self.position[1]]
        temp_line = list(temp_line)
        temp_line[self.position[0]] = self.string
        temp_line = "".join(temp_line)
        current_map[self.position[1]] = temp_line
        current_map_str = "".join(current_map)
        print(current_map_str)

    def parse_move(self, movement):
        """Fonction servant à transformer le mouvement entré par l'utilisateur en direction et nbr de pas"""
        direction = ""
        steps = 1
        direction = movement[0]
        if len(movement) > 1:
            steps = int(movement[1:])
        return direction, steps

    def move_robot(self, map, mvmt):
        victory = False
        direction, steps = self.parse_move(mvmt)
        y = self.position[1]
        x = self.position[0]
        if direction.lower() == "n":
            y -= steps
        elif direction.lower() == "s":
            y += steps
        elif direction.lower() == "e":
            x += steps
        elif direction.lower() == "o":
            x -= steps
        new_position = (x,y)
        if self.check_robot_movement(map, new_position):
            # self.position[0] = x
            # self.position[1] = y
            self.position = new_position
            if map.map_list[new_position[1]][new_position[0]]== "U":
                victory = True
        else:
            print("Ce mouvement est impossible.")
        return victory

    """ def update_robot_position(self, map, position):
        victory = False
        if self.check_robot_movement(map, position):
            self.position = position
            if map.map_list[position[1]][position[0]]:
                victory = True
        else:
            print("Ce mouvement est impossible.")
        return victory"""
