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


# 利用while语句写出猜大小的游戏：
# 设定一个理想数字比如：50，让用户输入数字，如果比50大，则显示猜测的结果大了；如果比50小，则显示猜测的结果小了;只有等于50，显示猜测结果，然后退出循环。
# 给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，如果三次之内没有猜测正确，则自动退出循环，并显示‘???’。
count = 1
while count < 4:
    num = int(input("please fucking input:"))
    if num < 50:
        print("fucking small!")
    elif num > 50:
        print("fucking bigger!")
    else:
        print("what the fucking lucky!")
        break
    count += 1
else:
    print("？？？")


# while循环 1 2 3 4 5 6 7 9 10
sb = 1
while sb < 11:
    if sb == 8:
        pass
    else:
        print(sb)
    sb += 1
# method2：
zz = 1
while zz < 11:
    if zz == 8:
        zz += 1
    print(zz)
    zz += 1



# 求1-100的所有数的和
sb =0
mdzz = 1
while  mdzz < 101:
    sb = sb + mdzz
    if mdzz == 100:
        print(sb)
    mdzz += 1

# 输出 1-100 内的所有奇数,输出 1-100 内的所有偶数
zz = 0
while zz < 101:
    zz += 1
    if zz % 2 == 0:
        print(zz)

sb = 0
while sb < 100:
    sb += 1
    if sb % 2 != 0:
        print(sb)


# 求1-2+3-4+5 ... 99的所有数的和
sum = 0
sb = 0
while sb < 99:
    sb += 1
    if sb %2 ==0:
        sum -= sb
    elif sb % 2 != 0:
        sum += sb
print(sum)