__author__ = 'vinogradov'


class Client(object):

    def __init__(self, transport):
        self.transport = transport
        super(Client, self)

    def __getattr__(self, item):

        def wrapper(*args):
            return self.send_command(item, *args)

        try:
            return self.__getattribute__(item)
        except AttributeError:
            return wrapper

    def send_command(self, command_name, *args):
        return self.transport.send_message((command_name, args))

import socket_transport
client = Client(socket_transport)
x1 = client.test(1, 2)
x2 = client.test2(1, 2)

print(x1)
print(x2)
