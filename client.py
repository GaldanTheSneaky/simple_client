import socket


class Client:
    def __init__(self, header, port, host, format='utf-8', disconnect_message="!DISCONNECT"):
        self._header = header
        self._port = port
        self._host = host
        self._addr = (self._host, self._port)
        self._format = format
        self._disconnect_message = disconnect_message
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect(self._addr)

    def send(self, msg):
        message = msg.encode(self._format)
        msg_length = len(message)
        send_length = str(msg_length).encode(self._format)
        send_length += b' ' * (self._header - len(send_length))
        self._client.send(send_length)
        self._client.send(message)
        print(self._client.recv(2048).decode(self._format))

    def run(self):
        self.send("Hello World!")
        input()
        self.send("Hello Everyone!")
        self.send(self._disconnect_message)


