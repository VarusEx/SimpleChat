import socket, sys
from threading import Thread , active_count

conn = None
clients = []
threads = []


def send(text, writer):
    print(active_count())
    try:
        for c in clients:
            if c is not writer:
                c.send(text.encode("utf-8"))
    except ConnectionResetError:
        return print("Something is bad")


class ServerThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        IP = '0.0.0.0'
        PORT = 80

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server.bind((IP, PORT))
        self.adduser(server)

    def adduser(self, arg):

        arg.listen(5)
        while True:
            print("Waiting to connect with client...")
            global conn
            (conn, (ip, port)) = arg.accept()
            newthread = ClientThread(ip, port)
            newthread.start()
            threads.append(newthread)

            for thread in threads:
                thread.join()


class ClientThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port

        print("Come to us new client his ip is: " + ip + ":" + str(port))

    def run(self):
        while True:
            try:
                global conn
                data = conn.recv(2048)
                clients.append(conn)
                send(data.decode("utf-8"), conn)
                print(data.decode("utf-8"))
            except ConnectionResetError:
                print("User: " + self.ip + " disconnect")
                break


if __name__ == '__main__':
    server = ServerThread()
    server.start()

