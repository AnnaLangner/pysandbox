import socket

HOST = "127.0.0.1"
PORT = 23456

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.sendto(b"Hello from Python", (HOST, PORT))
    
