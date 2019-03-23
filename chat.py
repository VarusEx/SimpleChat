from PyQt5 import QtCore
from PyQt5 import QtWidgets


class Window(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.chatText = QtWidgets.QLineEdit(self)
        self.chatText.resize(480,100)
        self.chatText.move(10, 350)

        self.btnSend = QtWidgets.QPushButton("Send", self)
        self.btnSend.resize(480, 30)
        self.btnSendFont = self.btnSend.font()
        self.btnSendFont.setPointSize(15)
        self.btnSend.setFont(self.btnSendFont)
        self.btnSend.move(10, 460)
        self.btnSend.setStyleSheet("background-color: #D1900E")

        self.layout = QtWidgets.QVBoxLayout(self)
        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)

        self.chat = QtWidgets.QTextEdit()
        self.chat.setReadOnly(True)

        splitter.addWidget(self.chat)
        splitter.addWidget(self.chatText)
        splitter.setSizes([400, 100])

        splitter2 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter)
        splitter2.addWidget(self.btnSend)
        splitter2.setSizes([200, 10])

        self.layout.addWidget(splitter2)

        self.setWindowTitle("Chat Application")
        self.resize(500, 500)
