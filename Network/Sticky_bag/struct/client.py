'''
Author: Ralph
Type_file[python//GO//json//Yaml//Other]: [python]
Date: 2020-09-18 09:47:11
LastEditTime: 2020-09-18 10:26:47
FilePath: /pyenv/Sticky_bag/struct/client.py
Effect: c端粘包现象
'''

# 两条发送的数连在一起 就是粘包现象
import socket
import struct
sk = socket.socket()
sk.connect(('127.0.0.1', 9001))
length = sk.recv(4)
length = struct.unpack('i',length)[0]
msg1 = sk.recv(length)
print(msg1.decode('utf-8'))

msg2 = sk.recv(1024)
print(msg2.decode('utf-8'))

sk.close()