import time
import sys
import os
from socket import *

HOST = 'localhost'
PORT = 18288
ADDR = (HOST, PORT)
BUFSIZ = 4096

def print_raw():
    with open('python.txt') as f:
        lines = f.readlines()
        length = len(lines)
        for i in range(length):
            print(lines[i])
            time.sleep(1)


class TcpClient():
    def __init__(self):
        self.client = socket()
        try:
            self.client.connect(ADDR)
        except ConnectionRefusedError as e:
            print('Connection refused.')
            os._exit(1)

    def start_on(self):
        self.sysBackup = sys.stdout
        sys.stdout = self.client.makefile('w')
        print_raw()

    def disconnect(self):
        self.client.close()
        sys.stdout = self.sysBackup


class  TcpServer():
    def __init__(self):
        self.server = socket()
        try:
            self.server.bind(ADDR)
        except OSError as e:
            print('Address alredy in use.')
            os._exit(1)


    def start_on(self):
        self.server.listen(5)
        print('Listening...')
        tcpClientSock, addr = self.server.accept()
        while True:
            try:
                data = tcpClientSock.recv(BUFSIZ)
                print(data)
            except:
                tcpClientSock.close()
                break
            if not data:
                break

    def disconnect(self):
        self.server.close()


if __name__ == "__main__":
    if sys.argv[1] == 'server':
        server = TcpServer()
        server.start_on()
    elif sys.argv[1] == 'client':
        client = TcpClient()
        client.start_on()