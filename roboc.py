from lib.map import *
from lib.robot import *
from lib.functions import *

victory = False

available_maps = available_maps()
chosen_map_name = choose_map(available_maps)

map = Map(chosen_map_name)
# print(map.x_max, map.y_max)
# map.display_map()
my_robot = Robot("X", map)
my_robot.place_n_display_robot_on_map(map)

while not victory:
    mvmt = input("Veuillez entrer un mouvement: ")
    victory = my_robot.move_robot(map, mvmt)
    my_robot.place_n_display_robot_on_map(map)

if victory:
    print("######################### VOUS AVEZ TROUVE LA SORTIE!!! #########################")