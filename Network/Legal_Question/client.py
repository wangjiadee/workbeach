import hashlib
import socket
Secret_Key = b'fucking'
sk = socket.socket()
sk.connect(('10.27.92.30',9012))

ret = sk.recv(32)
sha = hashlib.sha1(Secret_Key)
sha.update(ret)
res = sha.hexdigest()

sk.send(res.encode('utf-8'))

message = sk.recv(1024)
print(message)


