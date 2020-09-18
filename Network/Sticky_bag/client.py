'''
Author: Ralph
Type_file[python//GO//json//Yaml//Other]: [python]
Date: 2020-09-18 09:47:11
LastEditTime: 2020-09-18 10:11:26
FilePath: /pyenv/Sticky_bag/client.py
Effect: c端粘包现象
'''

# 两条发送的数连在一起 就是粘包现象
import  socket

sk = socket.socket()
sk.connect(('127.0.0.1',9002))
length = int(sk.recv(4).decode('utf-8'))
msg1 = sk.recv(length)
print(msg1.decode('utf-8'))

msg2 = sk.recv(1024)
print(msg2.decode('utf-8'))

sk.close()