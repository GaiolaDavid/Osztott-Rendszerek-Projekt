import socket

HOST = '127.0.0.1'
PORT = 8080

class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = HOST
        self.port = PORT
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f'Server is listening at {self.host}:{self.port}')

    