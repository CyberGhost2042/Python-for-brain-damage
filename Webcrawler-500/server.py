import socket

s = socket.socket()
s.bind(("localhost", 4332))
s.listen(1)

conn, addr = s.accept()
print(f"Server is Connected with {addr} address on {conn}")


while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Client has Sent: {data}")
    conn.send(f"Recieved: {data}".encode())

conn.close()
