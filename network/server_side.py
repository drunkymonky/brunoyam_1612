import socket
import threading

HOST = 'localhost'
PORT = 12345


def process_connection(sock, another_sock):
    while True:
        print(sock)
        print(addr)
        data = sock.recv(1024)
        print(data)
        decoded_data = data.decode('utf-8')
        print(decoded_data)
        sock.sendall(data)
        another_sock.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    connection, addr = server.accept()
    another_connection, addr = server.accept()

    threading.Thread(target=process_connection, args=(connection, another_connection)).start()
    threading.Thread(target=process_connection, args=(another_connection, connection)).start()
    # while True:
    #     print(connection)
    #     print(addr)
    #     data = connection.recv(1024)
    #     print(data)
    #     decoded_data = data.decode('utf-8')
    #     print(decoded_data)
    #     connection.sendall(data)
