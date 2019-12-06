import random


class Robot:
    """ THis class hold a robot object.
    The robot string representation, it position on the chosen map, Positions it can occupy ...
    """
    def __init__(self, robot_string, my_map):
        self.string = robot_string
        self.on_map = my_map.name
        self.possible_positions = [" ",".","U"]
        self.position = self.robot_init_position(my_map)
        my_map.robot_on_map[self.position[1] * (my_map.x_max + 2) + self.position[0]] = self.string

    def robot_init_position(self, my_map):
        """Method to randomly place a robot on a map"""
        initial_position_nok = True
        while initial_position_nok:
            # Generate random values, less than the size of the chosen map
            x = random.randint(0, my_map.x_max)
            y = random.randint(0, my_map.y_max)
            # Check that the random position can be used by the robot
            if my_map.map_list[y][x] in self.possible_positions and my_map.map_list[y][x] != "U":
                initial_position_nok = False
        # If ok, return the calculated position, which will be used as default initial position.
        return [x, y]

    def check_robot_movement(self, map, position):
        """ Method to check that a chosen movement is possible"""
        sign = lambda x: (1, -1)[x < 0]
        victory = lambda x: (True, False)[x == "U"]

        movement_possible = True
        i = j = 1
        # Check that movement doesn't go out of map limits
        if position[0] > map.x_max or position[1] > map.y_max:
            print("out of map ranges.")
            movement_possible = False

        elif position[0] != self.position[0]:  # Case where movement is in the x direction
            for i in range(1, abs(position[0] - self.position[0])+1):
                if map.robot_on_map[self.position[1] * (map.x_max + 2) + self.position[0] + sign(position[0]\
                                                      - self.position[0]) * i] not in self.possible_positions:
                    movement_possible = False
                    break

        elif position[1] != self.position[1]:  # Case where movement is in the y direction
            for i in range(1, abs(position[1] -  self.position[1])+1):
                if map.robot_on_map[(self.position[1] + sign(position[1] - self.position[1]) * i) * (map.x_max+2) + self.position[0]] \
                            not in self.possible_positions:
                    movement_possible = False
                    break
        return movement_possible

    def place_n_display_robot_on_map(self, map):
        """ Methode to display robot on map """
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
        if direction in ["m", "M", "p", "P"]:
            steps = movement[1:]
        else:
            if len(movement) > 1:
                steps = int(movement[1:])

        return direction, steps

    def move_robot(self, my_map, mvmt):
        """ Method to move a robot to a new position"""
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
        elif direction.lower() in ["m", "p"]:
            if steps.lower() == "n":
                y -= 1
            elif steps.lower() == "s":
                y += 1
            elif steps.lower() == "e":
                x += 1
            elif steps.lower() == "o":
                x -= 1
            if direction.lower() == "m":
                if my_map.check_door((x, y)):
                    my_map.close_open_door("c", (x, y))
            elif direction.lower() == "p":
                if my_map.check_wall((x, y)):
                    my_map.close_open_door("o", (x, y))

        new_position = (x, y)
        if direction not in ["m", "p"] and self.check_robot_movement(my_map, new_position):
            my_map.robot_on_map[self.position[1] * (my_map.x_max + 2) + self.position[0]] \
                = my_map.map_list[self.position[1]][self.position[0]]
            self.position = new_position
            my_map.robot_on_map[new_position[1] * (my_map.x_max + 2) + new_position[0]] = self.string
            if my_map.map_list[new_position[1]][new_position[0]] == "U":
                victory = True
        else:
            print("Cette commande est impossible.")
        return victory
