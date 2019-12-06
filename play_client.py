#! /usr/bin/python3

import socket
import sys
import select


# Socket to communicate to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 11111))

# Ask user to choose a string for his/her robot representation
robot_str = input("Choose a letter to represent your Robot: ")
client_socket.send(robot_str.encode())  # Sent it to the server
print("Initial robot position: \n" + client_socket.recv(1024).decode()
      + " \nWait for all client to connect and enter c to start the game : ")  # Print current status of the map

# Initialize game
continue_game = True
while continue_game:
    # Check if any data received from the server
    data_2_read, wlist, xlist = select.select([client_socket], [], [], 0.1)
    if data_2_read:  # If there is data evaluate it
        recvd_txt = client_socket.recv(1024).decode()
        if recvd_txt == "q" or recvd_txt == "Q":  # If received data ia q (sent by server to end game)
            continue_game = False
            print("######## Ending game. ########")

        if recvd_txt != "q" and recvd_txt != "Q": # If game not ended, print current map
            print(recvd_txt)

    # Look for data to be sent to the sever from stdin and send it if any
    data_2_send, wlist, xlist = select.select([sys.stdin], [], [], 0.5)
    if len(data_2_send):
        cmd_to_send = sys.stdin.readline().rstrip('\n')
        client_socket.send(cmd_to_send.encode())
# Close connection when game is ended.
client_socket.close()
