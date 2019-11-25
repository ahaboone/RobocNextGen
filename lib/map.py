class Map:
    def __init__(self, chosen_map_name):
        self.name = chosen_map_name
        with open("maps/"+ chosen_map_name + ".txt",'r') as map_file:
            self.map_list =  map_file.readlines()
            #for elt in temp:
            #    self.map_list.append(elt.rstrip()
        self.map_str = "".join(self.map_list)
        self.x_max = len(self.map_list[0]) - 2
        self.y_max = len(self.map_list)-1

    def map_str(self):
        return("".join(self.map_list))

    def display_map(self):
        print(self.map_str)
