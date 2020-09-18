'''
Author: Ralph
Type_file[python//GO//json//Yaml//Other]: [python]
Date: 2020-09-18 09:44:25
LastEditTime: 2020-09-18 10:26:00
FilePath: /pyenv/Sticky_bag/struct/server.py
Effect: s端粘包现象
'''
import struct
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

conn, addr = sk.accept()
msg = input('>>>').encode()
ms1 = input('>>>').encode()

ret = struct.pack('i',len(msg))
conn.send(ret)
conn.send(msg)
conn.send(ms1)
conn.close()

sk.close()