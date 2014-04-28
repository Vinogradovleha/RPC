__author__ = 'vinogradov'


class Client(object):

    def __init__(self, transport):
        self.transport = transport
        self.command_name = ''
        super(Client, self)

    def __getattr__(self, item):
        try:
            return self.__getattribute__(item)
        except AttributeError:
            self.command_name = item
            return self.send_command

    def send_command(self, *args):
        return self.transport.send_message((self.command_name, args))

import socket_transport
client = Client(socket_transport)
print('RESULT=' + str(client.test(7, 12)))

print('RESULT=' + str(client.test(1, 157)))
print('RESULT=' + str(client.test(3, 2)))
print('RESULT=' + str(client.test(54, 23)))