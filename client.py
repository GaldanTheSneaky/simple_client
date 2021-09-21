import socket


class Client:
    def __init__(self, header, port, host, format='utf-8', disconnect_message="!DISCONNECT"):
        self._header = header
        self._port = port
        self._host = host
        self._addr = (self._host, self._port)
        self._format = format
        self._disconnect_message = disconnect_message
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind(self._addr)

    def send(self, msg):
        message = msg.encode(self._format)
        msg_length = len(message)
        send_length = str(msg_length).encode(self._format)
        send_length += b' ' * (self._header - len(send_length))
        client.send(send_length)
        client.send(message)
        print(client.recv(2048).decode(self._format))

    def run(self):
        self.send("Hello World!")
        input()
        self.send("Hello Everyone!")

        self.send(self._disconnect_message)

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.4"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World!")
input()
send("Hello Everyone!")

send(DISCONNECT_MESSAGE)