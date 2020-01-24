import socket
import threading

HOST = 'localhost'
PORT = 12345


def process_connection(sock, all_connections):
    while True:
        print(sock)
        print(addr)
        data = sock.recv(1024)
        print(data)
        decoded_data = data.decode('utf-8')
        print(decoded_data)
        # sock.sendall(data)
        # another_sock.sendall(data)
        # задача
        # отправить всем из списка another_sock полученное сообщение
        for conn in all_connections:
            conn.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    connections = []

    while True:
        connection, addr = server.accept()
        connections.append(connection)
        threading.Thread(target=process_connection, args=(connection, connections)).start()