import sys, os, time
from multiprocessing import Process
from socket import *


def initListenerSocket(port=50008, host=''):
    """
    初始化在服务器模式下调用者用于监听连接的套接字
    """
    sock = socket()
    try:
        sock.bind((host, port))
    except OSError as e:
        print('Address already in use')
        os._exit(1)
    sock.listen(5)
    conn, addr = sock.accept()
    return conn


def redirecOut(port=50008, host='localhost'):
    """
    在接受之前其他连接都失败，连接调用者标准输出流
    到一个套接字，这个套接字用于gui监听,在收听者启动后，启动调用者
    """
    sock = socket()
    try:
        sock.connect((host, port))
    except ConnectionRefusedError as e:
        print('connection refuse')
        os._exit(1)
    file = sock.makefile('w')
    sys.stdout = file
    return sock


def redirecIn(port=50008, host='localhost'):
    """
    连接调用者标准输入流到用于gui来提供的套接字
    """
    sock = socket()
    try:
        sock.connect((host, port))
    except ConnectionRefusedError as e:
        print('conenction refuse')
        os._exit(1)
    file = sock.makefile('r')
    sys.stdin = file
    return sock


def redirecBothAsClient(port=50008, host='localhost'):
    """
    在这种模式下，连接调用者标准输入和输出流到相同的套接字
    调用者对于服务器来说就是客户端:发送消息，接受响应答复
    """
    sock = socket()
    try:
        sock.connect((host, port))
    except ConnectionRefusedError as e:
        print('connection refuse')
        os._exit(1)
    ofile = sock.makefile('w')
    ifile = sock.makefile('r')
    sys.stdout = ofile
    sys.stdin = ifile
    return sock


def redirecBothAsServer(port=50008, host='localhost'):
    """
    在这种模式下，连接调用者标准输入和输出流到相同的套接字，调用者对于
    服务器来说就是服务端：接受消息，发送响应答复
    """
    sock = socket()
    try:
        sock.bind((host, port))
    except OSError as e:
        print('Address already in use')
        os._exit(1)
    sock.listen(5)
    conn, addr = sock.accept()
    ofile = conn.makefile('w')
    ifile = conn.makefile('r')
    sys.stdout = ofile
    sys.stdin = ifile
    return conn


def server1():
    mypid = os.getpid()
    conn = initListenerSocket()
    file = conn.makefile('r')
    for i in range(3):
        data = file.readline().rstrip()
        print('server %s got [%s]' % (mypid, data))


def client1():
    time.sleep(1)
    mypid = os.getpid()
    redirecOut()
    for i in range(3):
        print('client: %s:%s' % (mypid, i))
        sys.stdout.flush()


def server2():
    mypid = os.getpid()
    conn = initListenerSocket()
    for i in range(3):
        conn.send(('server %s got [%s]\n' % (mypid, i)).encode())


def client2():
    time.sleep(1)
    mypid = os.getpid()
    redirecIn()
    for i in range(3):
        data = input()
        print('client %s got [%s]]' % (mypid, data))


def server3():
    mypid = os.getpid()
    conn = initListenerSocket()
    file = conn.makefile('r')
    for i in range(3):
        data = file.readline().rstrip()
        conn.send(('server %s got [%s]\n' % (mypid, data)).encode())


def client3():
    time.sleep(1)
    mypid = os.getpid()
    redirecBothAsClient()
    for i in range(3):
        print('Client %s: %s' % (mypid, data))
        data = input()
        sys.stderr.write('client %s got [%s]\n' % (mypid, data))


def server4(port=50008, host='localhost'):
    mypid = os.getpid()
    sock = socket()
    try:
        sock.connect((host, port))
    except ConnectionRefusedError as e:
        print('connection refuse')
        os._exit(1)
    file = sock.makefile('r')
    for i in range(3):
        sock.send(('server %s: %S\n' % (mypid, i)).encode())
        data = file.readline().rstrip()
        print('server %s got [%s]' % (mypid, data))


def client4():
    time.sleep(1)
    mypid = os.getpid()
    redirecBothAsServer()
    for i in range(3):
        data = input()
        print('client %s got [%s]' % (mypid, data))
        sys.stdout.flush()


def server5():
    mypid = os.getpid()
    conn = initListenerSocket()
    file = conn.makefile('r')
    for i in range(3):
        conn.send(('server %s:%s\n' % (mypid, i)).encode())
        data = file.readline().rstrip()
        print('server %s got [%s]' % (mypid, data))


def client5():
    mypid = os.getpid()
    s = redirecBothAsClient()
    for i in range(3):
        data = input()
        print('client %s got [%s]' % (mypid, data))
        sys.stdout.flush()


def main():
    server = eval('server' + sys.argv[1])
    client = eval('client' + sys.argv[1])
    Process(target=server).start()
    client()


if __name__ == '__main__':
    main()