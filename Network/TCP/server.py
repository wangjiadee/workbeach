import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9099))         #请求操作系统的资源
sk.listen()

# for i in range(10):和10个客户端握手
while True:  
    conn,addr = sk.accept()             #conn存储的是一个c端和s端的链接信息
    print('conn:',conn)
    # conn.send(b'Fucking u,clinet!')
    send_msg = input('>>>')
    conn.send(send_msg.encode('utf-8'))
    if send_msg.upper() == 'Q'
        break
    msg = conn.recv(2048).decode('utf-8')
    print(msg)
    conn.close()


sk.close()                          #归还申请操作系统的资源
