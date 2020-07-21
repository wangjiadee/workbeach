# 斐波那契数列：1，1，2，3，5，8，13，21..........(第三个数为前两个数的和，但是最开始的1，1是特殊情况，可以单独讨论)

lst = [1]
def func(a=1,b=1):
    lst.append(b)
    if a+b > 100:
        return  lst
    else:
        a,b = (b,a+b)
        # print(a,b)
        return func(a,b)
print(func(1,1))

# 第二种简便的方法：
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return  1
    else:
        return func(n-2)+func(n-1)
for i in range(1,8):
    print(func(i))

# 6.用户输入序号获取对应的斐波那契数字：比如输入6，返回的结果为8

while True:
    num = input("请输入序号（Q|退出）：")
    if num.isdecimal():
        num = int(num)
        lst = [1]
        def func(a=1,b=1):
            lst.append(b)
            if a+b > 100:
                return  lst
            else:
                a,b = (b,a+b)
                # print(a,b)
                return func(a,b)
        print(func(1,1)[num-1])
        print(lst)
    else:
        if num.upper() == "Q":
            break
        else:
            print("输入错误！")


#  第二种简便方法：
num = input("请输入序号：")
num = int(num)
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return  1
    else:
        return func(n-2)+func(n-1)
print(func(num))