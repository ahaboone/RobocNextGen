#! /usr/bin/python3

import socket
import select
import time

from lib.map import *
from lib.robot import *
from lib.functions import *

victory = False

# Load available maps from the maps subdir
available_maps = available_maps()
chosen_map_name = choose_map(available_maps)
# Create a map object from the chosen map
my_map = Map(chosen_map_name)

# Create the socket that will handle communication with clients
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 11111))
server_socket.listen(5)

start_game = False  # Value will be used to wait for client connections
continue_game = True  # Value will be used to stop game when needed
client_connections = []  # Will hold all connected clients
existing_robots = {}  # For each client, a robot will exist in this dict

print(readme)
print("\n \n##################################### Waiting for clients to connect #####################################")
while not start_game:
    # Get connection request from clients, and accept them. For each new client, add it to the client_conn list
    connected_clients, wlist, xlist = select.select([server_socket], [], [], 0.1)
    for connection in connected_clients:
        connection_to_client, connection_info = connection.accept()
        if connection_to_client not in client_connections:
            robot_str = connection_to_client.recv(1024).decode()  # First value received from the client is the string
            existing_robots[connection_info[1]] = Robot(robot_str, my_map)
            print("{} Robots connecte(s).".format(len(existing_robots)))
            connection_to_client.send("".join(my_map.robot_on_map).encode())
            client_connections.append(connection_to_client)
    # For all connected clients, look if c is entered to break the wait for clients loop and start the game
    client_a_lire = []
    try:
        client_a_lire, wlist, xlist = select.select(client_connections, [], [], 0.1)
    except select.error:
        pass
    else:
        for client in client_a_lire:
            recvd_cmd = client.recv(1024).decode()
            if recvd_cmd == "c" or recvd_cmd == "C":
                start_game = True
                print("############## Game started #################")
                for client_inner in client_connections:
                    client_inner.send(b"############## Game started ################# \n")
                client_a_lire = []

# Game starts here
while continue_game:
    reply_msg = ""
    recvd_cmd = ""
    # Go through the list of clients, one by one, and ask for a command
    for connected_client in client_connections:
        connected_client.send("#################################################### \n"
                              "A votre tour! Entrez une commande:".encode())
        recvd_cmd = connected_client.recv(1024).decode()
        print("Received command <{}> from robot {}".format(
            recvd_cmd, existing_robots[connected_client.getpeername()[1]].string))
        # Quit if q is entered
        if recvd_cmd == "q" or recvd_cmd == "Q":
            continue_game = False
            # Close all connected client sessions
            for connected_client_inner in client_connections:
                connected_client_inner.send(b"q")
            break
        # If q is not entered, then move the robot according to the entered command.
        # The returned value is victory (bool) in case any client reaches the door
        init_position = existing_robots[connected_client.getpeername()[1]].position
        victory = existing_robots[connected_client.getpeername()[1]].move_robot(my_map, recvd_cmd)
        if init_position == existing_robots[connected_client.getpeername()[1]].position:
            connected_client.send(b"Mouvement impossible, votre robot reste sur place. \n")

        # If one of the clients next position is the door
        if victory:
            # Stop the game
            continue_game = False
            # Broadcast to all clients who found the exit
            reply_msg = "Robot {} has found the exit. Game over!". \
                format(existing_robots[connected_client.getpeername()[1]].string)
            print(reply_msg)
            # Close connection on all clients
            for connected_client_inner in client_connections:
                connected_client_inner.send(reply_msg.encode())
                time.sleep(0.5)
                connected_client_inner.send(b"q")
            break
        # Otherwise, compile the message to be sent: the current status of the map
        else:
            reply_msg = "".join(my_map.robot_on_map)
        # Send the latest map to all clients and close connection.

        for connected_client_inner in client_connections:
            connected_client_inner.send(reply_msg.encode())
            # connected_client_inner.close()

print("Game ended!")
# Close server socket
server_socket.close()
