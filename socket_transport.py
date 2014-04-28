__author__ = 'vinogradov'
import socket
import json


HOST = '127.0.0.1'
PORT = 50008


class SocketServer(object):
    def __init__(self, callback):
        self.callback = callback
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))
        self.s.listen(1)

    def serve_forever(self):
        while True:
            try:
                conn, addr = self.s.accept()
                print 'Connected by', addr

                data = conn.recv(1024)
                if not data:
                    break

                data = json.loads(data)
                res = self.callback(data)
                conn.send(json.dumps(res))
            except:
                import traceback
                traceback.print_exc()
                break


def send_message(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(json.dumps(message))
    data = json.loads(s.recv(1024))
    s.close()
    print 'Received', repr(data)
    return data


