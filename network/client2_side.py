import socket
import threading
from tkinter import Tk

from network.gui import Example

HOST = 'localhost'
# HOST = 'aud21-prep'
PORT = 12345


def receive_data(sock, window):
    while True:
        data = sock.recv(1024)
        print(data)
        window.add_input(data.decode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    root = Tk()
    root.geometry('700x700+300+300')
    app = Example(root, lambda x: client.sendall(x))
    threading.Thread(target=receive_data, args=(client, app)).start()
    root.mainloop()


