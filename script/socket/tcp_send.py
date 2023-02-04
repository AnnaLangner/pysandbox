import socket

IP = "127.0.0.1"
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((IP, PORT))
    client.send(b"hello from python")
    
