__author__ = 'vinogradov'


class Server(object):
    proc_list = dict()

    def __init__(self, transport):
        self.transport = transport

    def register(self, proc_name):
        self.proc_list[proc_name.func_name] = proc_name

    def serve_forever(self):
        self.transport.SocketServer(self.resolve_func).serve_forever()

    def resolve_func(self, (name, args)):
        if name in self.proc_list:
            return self.proc_list[name](*args)

#============


def test(x, y):
    return x + y


def test2(x, y):
    return x*2 + y

import socket_transport
server = Server(socket_transport)
server.register(test)
server.register(test2)
server.serve_forever()

