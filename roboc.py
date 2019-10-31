from lib.map import *
from lib.robot import *
from lib.functions import *


available_maps = available_maps()
chosen_map_name = choose_map(available_maps)

map = Map(chosen_map_name)
map.display_map()
my_robot = Robot("X"map)