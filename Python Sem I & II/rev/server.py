import socket
sct = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "0.0.0.0"
port = 65499
sct.bind((host,port))
sct.listen(5)
print("Server started!!")
while True:
    clientsocket,address = sct.accept()
    print(f"Connect is made: {address}")
    data = clientsocket.recv(1024).decode()
    print(f"MSG recieved: {data}")
    clientsocket.send(b"Kya kr raha hai bhadwe")
    clientsocket.close()
    print("Server is shutting 😭")