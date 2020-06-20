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
# count =1
while count < 101:
    if count % 2 == 0:
        print(count)
    count = count + 1

