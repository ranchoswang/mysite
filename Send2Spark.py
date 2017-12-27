import time
import os
import sys
from threading import *
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

class SocketServer():

    def __init__(self):
        self.sysBackup = sys.stdout
        self.server = socket()
        try:
            self.server.bind(ADDR)
        except OSError as e:
            print('Address alredy in use.')
            os._exit(1)

    def start_on(self):
        self.server.listen(5)
        print('Listening...')
        self.tcpClientSock, addr = self.server.accept()
        print('Connection accepted. Writing data...')
        self.sysBackup = sys.stdout
        sys.stdout = self.tcpClientSock.makefile('w')
        print_raw()

    def close_off(self):
        self.tcpClientSock.close()
        sys.stdout = self.sysBackup
        print('Connection closed.')


if __name__ == "__main__":
    TcpServer = SocketServer()
    TcpServer.start_on()
    TcpServer.close_off()