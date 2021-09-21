from client import Client


def main():
    client = Client(64, 5050, "192.168.1.4")
    client.run()


if __name__ == '__main__':
    main()
