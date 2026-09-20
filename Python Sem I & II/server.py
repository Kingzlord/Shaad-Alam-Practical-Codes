#Server Code
import socket
srvrsct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"
port = 65499
srvrsct.bind((host,port))
srvrsct.listen(5)
print("Server Started")
while True:
    clientsocket,address = srvrsct.accept()
    print(f"Connection has been established with {address}")
    data = clientsocket.recv(1024).decode()
    print(f"Received: {data}")
    clientsocket.send(b"Hello World")
    clientsocket.close()
    print("Client Disconnected")