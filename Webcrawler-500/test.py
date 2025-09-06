import socket

clientsoc = socket.socket()
clientsoc.connect(("localhost", 4332))

while True:
    msg = input("Type the msg: ")
    client_req = clientsoc.send(msg.encode())
    server_response = clientsoc.recv(1024).decode()
    print(f"Server: {server_response}")
