#! /usr/bin/python3

import socket
import select
import pickle

from lib.map import *
from lib.robot import *
from lib.functions import *


victory = False

available_maps = available_maps()
chosen_map_name = choose_map(available_maps)

my_map = Map(chosen_map_name)

# my_map_stream = pickle.dumps(my_map)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 11111))
server_socket.listen(5)

start_game = False
continue_game = True

client_connections = []
existing_robots = {}
client_a_lire = []

print("##################################### Waiting for clients to connect #####################################")
while not start_game:
    connected_clients, wlist, xlist = select.select([server_socket], [], [], 0.1)
    for connection in connected_clients:
        connection_to_client, connection_info = connection.accept()
        if connection_to_client not in client_connections:
            # connection_to_client.send(my_map_stream)
            robot_str = connection_to_client.recv(1024).decode()
            existing_robots[connection_info[1]] = Robot(robot_str, my_map)
            print(existing_robots)
            connection_to_client.send("".join(my_map.robot_on_map).encode())
            client_connections.append(connection_to_client)

    try:
        client_a_lire, wlist, xlist = select.select(client_connections, [], [], 0.1)
    except select.error:
        pass
    else:
        for client in client_a_lire:
            recvd_cmd = client.recv(1024).decode()
            if recvd_cmd == "c" or recvd_cmd == "C":
                start_game = True
                for client_inner in client_connections:
                    client_inner.send(b"############## Game started ################# \n")
                client_a_lire = []

while continue_game:
    reply_msg = ""
    recvd_cmd = ""
    for connected_client in client_connections:
        connected_client.send("########################## \nYour turn! Entrez une commande:".encode())
        recvd_cmd = connected_client.recv(1024).decode()
        print(recvd_cmd)
        if recvd_cmd == "q" or recvd_cmd == "Q":
            break

        victory = existing_robots[connected_client.getpeername()[1]].move_robot(my_map, recvd_cmd)
        if victory:
            reply_msg = "Robot {} has found the exit. Game over!".\
                format(existing_robots[connected_client.getpeername()[1]].string)
            continue_game = False
        else:
            reply_msg = "".join(my_map.robot_on_map)
            # reply_msg += "\n########################## \n Entrez une commande: "

        my_map.display_map()

        for connected_client_inner in client_connections:
            connected_client_inner.send(reply_msg.encode())

    if recvd_cmd == "q" or recvd_cmd == "Q":
        for connected_client in client_connections:
            client.send(b"q")
        continue_game = False

print("Game ended!")

server_socket.close()
