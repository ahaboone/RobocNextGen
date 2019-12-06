import re
import os
from threading import Thread

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
    """ Function to get input from user for choosing a map"""
    chosen_map = int(input("Veuillez choisir un numéro de carte: "))
    return available_maps[chosen_map]


readme = """
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
This game is played in a client/server model.
First start the server. Then all clients.
Server is started with play_server - Only once.
Clients are started with play_client. As many as wished.
When (and only when) all clients are connected,
you can enter "c" (without the quotes), on any of the 
clients, to start the game.

Once the game is started, clients send commands to 
move their robot on the map, each at their turn.
Possible commands are:
- mX: build a wall. X is the direction in FR(n,s,e,o)
- pX: build a door. X is the direction in FR(n,s,e,o)
- xX: Move in direction x with X steps
        direction can be n,s,e,o
        step can be any integer
        
Game ends when one of the robots finds the exit or
when one of the clients sends a q command.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""