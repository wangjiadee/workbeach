import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9321)) 
sk.listen()

conn,addr = sk.accept()
conn.send(b'Fucking client,too!')
msg = conn.recv(4096)
print(msg)

conn.close()

sk.close()
