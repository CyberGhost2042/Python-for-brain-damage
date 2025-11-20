import socket

SERVER_ADDRESS = ("localhost", 8080)
CHUNK_SIZE = 1024


def makesocket(host, port):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((host, port))
    return conn


def sendfile(connsock: socket.socket, filename):
    with open(file=f"{filename}.txt") as file:
        data = file.read()
        totalfile = len(data)
        totalsent = 0
        print(f"Client Sending {totalfile} data")
        while totalsent < totalfile:
            sent = connsock.send(bytes(data[totalsent:], "utf-8"))
            print(f"Client sent {sent} bytes")
            if sent == 0:
                break
            totalsent += sent
        return totalsent


def recieveack(connsock: socket.socket):
    with connsock as connection:
        recieved = connection.recv(CHUNK_SIZE)
        return int(str(recieved, "utf-8"))


def main(host, port, filename):
    conn = makesocket(host, port)
    bytes_sent = sendfile(conn, filename)
    print(f"Client has sent {bytes_sent} to Server")
    bytes_recieved = recieveack(conn)
    print(f"Client has recieved {bytes_recieved} from Server")
    if bytes_sent == bytes_recieved:
        print("YIPEE !!! GOOD TRANSFER")
    else:
        print("AWWW! BAD TRANSFER")


if __name__ == "__main__":
    main("localhost", 8080, "textfile")
