import socket
import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 11111))
server_socket.listen(5)

continue_game = True
client_connections = []

while continue_game:
    reply_msg = b"Message recu"
    connected_clients, wlist, xlist = select.select([server_socket], [], [], 1)
    for connection in connected_clients:
        connection_to_client, connection_info = connection.accept()
        client_connections.append(connection_to_client)

        client_a_lire = []
    try:
        client_a_lire, wlist, xlist = select.select(client_connections, [], [], 1)
    except select.error:
        pass
    else:
        for client in client_a_lire:
            recvd_cmd = client.recv(1024).decode()
            print(recvd_cmd)
            if recvd_cmd == "q" or recvd_cmd == "Q":
                continue_game = False
                reply_msg = b"q"
            client.send(reply_msg)


print("Game ended!")
for client in client_connections:
    client.close()
server_socket.close()
