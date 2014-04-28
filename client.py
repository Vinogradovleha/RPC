__author__ = 'vinogradov'


def apply_command_name(command_name, obj):
    def wrapper(*args):
        return obj.send_command(command_name, *args)
    return wrapper


class Client(object):

    def __init__(self, transport):
        self.transport = transport
        super(Client, self)

    def __getattr__(self, item):
        try:
            return self.__getattribute__(item)
        except AttributeError:
            return apply_command_name(item, self)

    def send_command(self, command_name, *args):
        return self.transport.send_message((command_name, args))

import socket_transport
client = Client(socket_transport)
x1 = client.test(1, 2)
x2 = client.test2(1, 2)

print(x1)
print(x2)
