import socket

sk = socket.socket(type =socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9091))
while True:
    msg,addr = sk.recvfrom(2048)
    print(msg.decode('utf-8'))
    msg  = input(">>>>").encode('utf-8')
    sk.sendto(msg,addr)
    print(msg)
