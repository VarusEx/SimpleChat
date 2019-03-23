from PyQt5.QtWidgets import QApplication
import chat
import socket, sys
from threading import Thread


client_conn = None
app = QApplication(sys.argv)
window = chat.Window()


def send():
    text = window.chatText.text()
    font = window.chat.font()
    font.setPointSize(13)
    window.chat.setFont(font)
    try:
        global client_conn
        client_conn.send(text.encode("utf-8"))
    except ConnectionResetError:
        return window.chat.append("Server lost connection with you...")
    textformatted = '{:>80}'.format(text)
    window.chat.append(textformatted)
    window.chatText.setText("")


class ClientThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        host = socket.gethostname()
        port = 80
        buffer_size = 2000
        global client_conn
        client_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_conn.connect((host, port))
        while True:
            try:
                data = client_conn.recv(buffer_size)
                window.chat.append(data.decode("utf-8"))
            except ConnectionResetError:
                pass




if __name__ == '__main__':
    window.btnSend.clicked.connect(send)
    window.setWindowTitle("Client Chat")
    client = ClientThread(window)
    client.start()
    window.exec()
    sys.exit(app.exec_())
