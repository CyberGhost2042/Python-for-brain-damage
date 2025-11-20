from socketserver import BaseRequestHandler

CHUNK_SIZE = 1024


class FileHandler(BaseRequestHandler):
    def handle(self):
        print("Server is about to recieve")
        data = bytes()
        while True:
            latest = self.request.recv(CHUNK_SIZE)
            print(f"Server has just recieved {len(latest)} bytes of data")
            data += latest
            if len(latest) < CHUNK_SIZE:
                print("I Think we are Done ?....")
                break
        print("Server has finished recieved, about to reply..")
        self.request.sendall(bytes(f"{len(data)}", "utf-8"))
