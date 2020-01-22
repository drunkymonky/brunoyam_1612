import socket
import threading

HOST = 'localhost'
# HOST = 'aud21-prep'
PORT = 12345


def receive_data(sock):
    while True:
        data = sock.recv(1024)
        print(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    threading.Thread(target=receive_data, args=(client,)).start()
    while True:
        user_input = input()
        client.sendall(bytes(user_input.encode('utf-8')))

