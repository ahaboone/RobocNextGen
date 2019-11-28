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


continue_game = True
client_connections = []
existing_robots = {}

while continue_game:
    reply_msg = ""
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

    client_a_lire = []
    try:
        client_a_lire, wlist, xlist = select.select(client_connections, [], [], 0.1)
    except select.error:
        pass
    else:
        recvd_cmd = ""
        for client in client_a_lire:

            recvd_cmd = client.recv(1024).decode()
            print(recvd_cmd)
            if recvd_cmd == "q" or recvd_cmd == "Q":
                break
            victory = existing_robots[client.getpeername()[1]].move_robot(my_map, recvd_cmd)

            # existing_robots[client.getpeername()[1]].place_n_display_robot_on_map(my_map)
            #my_map.print_map_list()
            if victory:
                reply_msg = "Robot {} has found the exit. Game over!".format\
                    (existing_robots[client.getpeername()[1]].string)
                continue_game = False
            else:
                reply_msg = "".join(my_map.robot_on_map)

            my_map.display_map()
            client.send(reply_msg.encode())
        if recvd_cmd == "q" or recvd_cmd == "Q":
            for client in client_a_lire:
                client.send(b"q")
            continue_game = False

print("Game ended!")
for client in client_connections:
    client.send(b"q")
    client.close()
server_socket.close()
