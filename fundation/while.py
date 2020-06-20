"""
this is studing for while


while 条件：
    循环体

"""

# 无限循环
while True:  # judge condition
    print("MDZZ")
    print("sb")
    print("zz")


# end the cycle for changes condition
f = True
while f:
    print("123")
    print("412")
    f = False
    print("222")


# 输出1-100的所有的数字
count = 1
f = True
while f:
    print(count)
    count = count + 1
    if count == 101:
        break        #break 终止循环


# 输出1到100的集合
s = 0
c = 1
while c < 101:
    s = s + c
    c = c + 1
print(s)


# 输出100内的偶数
while True:
    print(count)
    count = count + 2
    if count == 102:
        break        #break 终止循环

#方法2
count =1
while count < 101:
    if count % 2 == 0:
        print(count)
    count = count + 1

continue 退出本次循环
while True:
    print(110)
    print(112)
    continue  #遇到continue 等于遇到while底部
    print(119)


#while else  组合 记住用法：
#while循环被break打断 就不执行else
count = 1
while count < 4:
    print(count)
    if count == 2:
        break
    count = count + 1
else:
    print("mdzz")


#实例：
count = 1
while count <= 3:
    username = input("input fucking name:")
    password = input("input fucking password:")
    code = 'Mdzz'
    md_code  = input("input fucking code:")
    if md_code == code:
        if username == 'sb' and password == 'zz':
            print("loading success!")
        else:
            print('username or password Error!')
    else:
        print("fucking code Error!")
    count = count + 1
