from socket import *
class Server:
    def __init__(self):
        pass
    def init(self):
        self.clients = []
        self.passwds = {}
        self.sock_cli = socket(AF_INET,SOCKET_STREAM)

