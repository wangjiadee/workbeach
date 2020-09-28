#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import socket
import hashlib

Secret_Key = b'fucking'
sk = socket.socket()
sk.bind(('10.27.92.30',9012))
sk.listen()

conn,addr = sk.accept()
ret = os.urandom(32)
conn.send(ret)

sha = hashlib.sha1(Secret_Key)
sha.update(ret)
res = sha.hexdigest()

res_client =  conn.recv(1024).decode('utf-8')
if res_client == res:
        print('legal client!')
        conn.send(b'Fucking u!')
else:
        print('ERROR: illegal!')
        conn.close()

