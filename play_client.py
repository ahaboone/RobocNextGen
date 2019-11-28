import socket
import pickle
from lib.map import *

from lib.robot import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 11111))

# chosen_map_stream = client_socket.recv(4096)
# chosen_map = pickle.loads(chosen_map_stream)

# print(chosen_map.name)
# print(chosen_map.map_str)

robot_str = input("Choose a letter to represent your Robot: ")
client_socket.send(robot_str.encode())
print("Initial robot position: \n" + client_socket.recv(1024).decode())
# my_robot = Robot(robot_str, chosen_map)

continue_game = True
while continue_game:
    cmd_to_send = input("Veuillez entrer une commande: ")
    cmd_to_send = cmd_to_send.encode()
    client_socket.send(cmd_to_send)
    recvd_msg = client_socket.recv(1024)
    recvd_msg = recvd_msg.decode()
    if recvd_msg == "q" or recvd_msg == "Q":
        continue_game = False
        recvd_msg = " ######## Ending game. ########"
    print(recvd_msg)


client_socket.close()
