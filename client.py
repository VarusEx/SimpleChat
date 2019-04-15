from PyQt5.QtWidgets import QApplication, QMessageBox
import chat
import socket
import sys
import net_utils
from threading import Thread


client_conn = None
app = QApplication(sys.argv)
window = chat.Window()


def send():
    text = window.chatText.text()
    font = window.chat.font()
    font.setPointSize(13)
    window.chat.setFont(font)
    global client_conn
    client_conn.send(text.encode("utf-8"))
    textformatted = '{:>80}'.format(text)
    window.chat.append(textformatted)
    window.chatText.setText("")


class ClientThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        while True:
            try:
                host = socket.gethostname()
                port = 80
                buffer_size = 2000
                global client_conn
                client_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_conn.connect((host, port))
                #QMessageBox.information(QMessageBox(), "Status Connect", "Connected with server", QMessageBox.Ok)
                while True:
                        data = client_conn.recv(buffer_size)
                        window.chat.append(data.decode("utf-8"))
            except ConnectionError as error:
                print(error)
                print("Error with connect")



if __name__ == '__main__':
    window.btnSend.clicked.connect(send)
    window.setWindowTitle("Client Chat")
    client = ClientThread(window)
    client.start()
    window.exec()
    sys.exit(app.exec_())

