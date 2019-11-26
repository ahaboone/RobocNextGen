import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 11111))

continue_game = True
while continue_game:
    cmd_to_send = input("Veuillez entrer une commande: ")
    cmd_to_send = cmd_to_send.encode()
    client_socket.send(cmd_to_send)
    recvd_msg = client_socket.recv(1024)
    recvd_msg = recvd_msg.decode()
    if recvd_msg == "q" or recvd_msg =="Q":
        continue_game = False
        recvd_msg = " ######## Ending game. ########"

    print(recvd_msg)

client_socket.close()
