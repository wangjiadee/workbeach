# server 接受
import json
import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1',9023))
sk.listen()


conn,_ = sk.accept()
msg_len = conn.recv(4)
dic_len = struct.unpack('i',msg_len)[0]
msg = conn.recv(dic_len).decode('utf-8')
msg = json.loads(msg)

with open(msg["File_name"],'wb') as f:
    # content = conn.recv(msg['File_size'])
    # print('Check Size:',len(content))
    # f.write(content)    
    while msg["File_size"] > 0:
        content = conn.recv(1024)
        msg["File_size"] -= len(content)
        # Solve the problem of unpacking
        f.write(content)

conn.close()
sk.close()
