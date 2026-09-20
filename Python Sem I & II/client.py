import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 65499
c.connect((host,port))
c.send(b"It's fucking working yes")
tm = c.recv(1024).decode()
print(f"Message from server: {tm}")
c.close()
print("Server disconnected")
