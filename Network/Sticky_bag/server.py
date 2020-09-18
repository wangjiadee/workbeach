'''
Author: Ralph
Type_file[python//GO//json//Yaml//Other]: [python]
Date: 2020-09-18 09:44:25
LastEditTime: 2020-09-18 10:12:48
FilePath: /pyenv/Sticky_bag/server.py
Effect: s端粘包现象
'''

"""
Notes
粘包 只出现在tcp协议中，因为tcp协议在多条消息之间
没有边界，并且还有一大堆算法

发送端：两条消息很短，发送消息的间隔也很短
接收端：多条信息由于没有及时接收，会导致粘包

解决粘包的本质问题：设置边界
先接收数据的长度 在接收数据
"""
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9002))
sk.listen()

conn, addr = sk.accept()
msg = input('>>>').encode()
ms1 = input('>>>').encode()

num = str(len(msg))
ret = num.zfill(4)
conn.send(ret.encode('utf-8'))
conn.send(msg)
conn.send(ms1)
conn.close()

sk.close()