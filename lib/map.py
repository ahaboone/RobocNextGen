class Map:
    """ This class hold the map used during the game.
    Map name, size (x,y), as we as "map as string" are attribute of the class
    """
    def __init__(self, chosen_map_name):
        self.name = chosen_map_name
        with open("maps/" + chosen_map_name + ".txt",'r') as map_file:
            self.map_list = map_file.readlines()
            # for elt in temp:
            #    self.map_list.append(elt.rstrip()
            self.robot_on_map = list()
        for map_line in self.map_list:
            self.robot_on_map += list(map_line)
        self.map_str = "".join(self.map_list)
        self.x_max = len(self.map_list[0]) - 2
        self.y_max = len(self.map_list)-1

    def map_str(self):
        """ Allow to use the print function on a map object"""
        return "".join(self.map_list)

    def display_map(self):
        """ Display a map in its latest status"""
        for char in self.robot_on_map:
            print(char, end="")
        print("\n")

    def print_map_list(self):
        for line in self.map_list:
            print(line, end="")

    def check_door(self, position):
        """ Check if a door is at a specific position on a map"""
        is_door = False
        if self.robot_on_map[position[1] * (self.x_max + 2) + position[0]] == ".":
            is_door = True
        return is_door

    def check_wall(self, position):
        """ Check if a wall has been built at a specific position on a map"""
        is_wall = False
        if self.robot_on_map[position[1] * (self.x_max + 2) + position[0]] == "M":
            is_wall = True
        return is_wall

    def close_open_door(self, action, position):
        """ Method to build a wall or open a door at a specific position"""
        if action == "c":
            self.robot_on_map[position[1] * (self.x_max + 2) + position[0]] = "M"
        elif action == "o":
            self.robot_on_map[position[1] * (self.x_max + 2) + position[0]] = "."
