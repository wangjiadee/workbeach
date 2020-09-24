import socket
User_List = {'ralph':'32','tom':'33'}
Other_User_List = {}
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9012))

while True:
    msg,addr = sk.recvfrom(1500)
    msg = msg.decode('utf-8')
    name,message = msg.split('|')
    print('%s:%s'%(name,message))
    content = input('>>>>')

    sk.sendto(content.encode('utf-8'),addr)
    if content.upper() == 'Q':break
