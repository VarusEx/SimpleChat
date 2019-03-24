import socket


def ping(server_ip, port=80):
    try:
        s = socket.socket()
        s.connect((server_ip, port))
    except Exception as e:
        return e
