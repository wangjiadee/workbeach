message1 = """--------------start at this--------------
name : reno
color: Y 
version: v1.0
---------------------------start at this--------------"""

message2 = """--------------start at this--------------
name : find
color: X
version: v2.0
---------------------------start at this--------------"""


message3 = """--------------start at this--------------
name : xp
color: W 
version: v3.0
---------------------------start at this--------------"""

name = input("input name：")
color = input("input color：")
version = input("input version：")

#格式化输出 ： 模板
message = """--------------start at this--------------
name : %s
color: %s
version: %s
---------------------------start at this--------------""" % (name,color,version)
print(message)



# 在格式化输出中 如需要让% 表示它本身的意思
msg = ' 文件%s,当前下载2%%' %(name2)
print(msg)


# 密码库
a = 0
b = 2
while a<3:
    username = input("please input u fucking name:")
    password = input("please input u fucking password:")
    if username == 'mdzz' and password == 'sb':
        print('what fucking lucky!')
        break
    else:
        print(" fucking Error:%s"%(b))
    b -= 1
    a += 1
print("FUCKING Bye!")
