import socketserver
from handler import FileHandler

SERVER_ADDRESS = ("localhost", 8080)

if __name__ == "__main__":
    with socketserver.TCPServer(SERVER_ADDRESS, FileHandler) as server:
        print("Server has Started")
        server.serve_forever()
