import socket

serv = socket.socket()

def starthttpmod(port = 80):
    serv.bind(('', port))
    serv.listen()
