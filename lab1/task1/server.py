import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8081))
server_socket.listen(1)

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    if request == "Hello, server":
        response = 'Hello, client'
        client_connection.sendall(response.encode())

    else:
        response = "Bye"
        client_connection.sendall(response.encode())
        client_connection.close()
    client_connection.close()

