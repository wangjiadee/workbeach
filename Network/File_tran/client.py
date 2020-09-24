import os
import socket
import json
import struct

sk = socket.socket()
sk.connect(('127.0.0.1',9023))

Path = r'/work/oppo_80288284/ota'
File_name = os.path.basename(Path)
File_size = os.path.getsize(Path)


dic = {'File_name':File_name,"File_size":File_size}
Json_dic = json.dumps(dic)
b_dic = Json_dic.encode('utf-8')
mlen =struct.pack('i',len(b_dic))
sk.send(mlen)
sk.send(b_dic)

with open(Path,mode='rb') as f:
    # content = f.read()
    # sk.send(content)
    while File_size > 0:
        content = f.read(1024)
        File_size -=len(content)
        sk.send(content)

sk.close()
