import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9321))  #和server端口 保持一样


msg = sk.recv(4096)
print(msg)

sk.send(b'Fucking u,server')

sk.close()


