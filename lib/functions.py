import re
import os


""" Module containing functions used in the roboc game"""


def available_maps():
    """ This function will check available maps in the maps subfolder and display them"""
    existing_maps = os.listdir("maps")
    # remove file extensions
    temp = []
    for map in existing_maps:
        map = re.sub(r"(.+)\..+", r"\1", map)
        temp.append(map)
    existing_maps = temp
    for i, map in enumerate(existing_maps):
        print("{} - {}".format(i,map))
    return existing_maps


def choose_map(available_maps):
    chosen_map = int(input("Veuillez choisir un numéro de carte: "))
    return available_maps[chosen_map]