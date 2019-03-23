from PyQt5.QtWidgets import QApplication
import chat
import socket, sys
from threading import Thread

conn = None
app = QApplication(sys.argv)
window = chat.Window()

def send(self):
    text = window.chatText.text()
    font = window.chat.font()
    font.setPointSize(13)
    window.chat.setFont(font)
    textformatted = '{:>80}'.format(text)
    window.chat.append(textformatted)
    global conn
    conn.send(text.encode("utf-8"))
    window.chatText.setText("")


class ServerThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        IP = '0.0.0.0'
        PORT = 80
        BUFFER_SIZE = 20

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((IP, PORT))
        threads = []

        server.listen(5)
        while True:
            print("Waiting to connect with client...")
            global conn
            (conn, (ip, port)) = server.accept()
            newthread = ClientThread(ip, port, window)
            newthread.start()
            threads.append(newthread)

            for thread in threads:
                thread.join()


class ClientThread(Thread):
    def __init__(self, ip, port, window):
        Thread.__init__(self)
        self.window = window
        self.ip = ip
        self.port = port
        print("Come to us new client his ip is: " + ip + ":" + str(port))

    def run(self):
        while True:
            global conn
            data = conn.recv(2048)
            window.chat.append(data.decode("utf-8"))


if __name__ == '__main__':
    window.btnSend.clicked.connect(send)
    window.setWindowTitle("Server Chat")
    server = ServerThread(window)
    server.start()
    window.exec()
    sys.exit(app.exec_())

