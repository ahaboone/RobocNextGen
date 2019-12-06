#! /usr/bin/python3

import socket
import pickle
import threading
import sys
import select
from queue import Queue

from lib.map import *
from lib.robot import *


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 11112))

robot_str = input("Choose a letter to represent your Robot: ")
client_socket.send(robot_str.encode())
print("Initial robot position: \n" + client_socket.recv(1024).decode()
      + " \nWait for all client to connect and enter c to start the game : ")
# my_robot = Robot(robot_str, chosen_map)


continue_game = True


while continue_game:
    data_2_read, wlist, xlist = select.select([client_socket], [], [], 0.1)
    if data_2_read:
        recvd_txt = client_socket.recv(1024).decode()
        if recvd_txt == "q" or recvd_txt == "Q":
            continue_game = False
            print(" ######## Ending game. ########")
            break
        print(recvd_txt)

    data_2_send, wlist, xlist = select.select([sys.stdin], [], [], 0.5)
    if len(data_2_send):
        cmd_to_send = sys.stdin.readline().rstrip('\n')
        client_socket.send(cmd_to_send.encode())


    # my_queue.put(continue_game)


# input_thread = threading.Thread(send_cmd(client_socket))
# input_thread.start()

# output_thread = threading.Thread(recv_cmd(client_socket, My_queue))
# output_thread.start()

# # continue_game = My_queue.get()
# output_thread.join()
# input_thread.join()
client_socket.close()
