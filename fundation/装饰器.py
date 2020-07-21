# 装饰器片：

"""
装饰器最终最完美的定义就是：在不改变原被装饰的函数的源代码以及调用方式下，为其添加额外的功能。

标准的函数装饰器模板：
def wrapper(func):
    def inner(*args,**kwargs):
        '''执行被装饰函数之前的操作'''
        ret = func
        '''执行被装饰函数之后的操作'''
        return ret
    return inner
"""

# 分析代码
def wrapper(f):
    def inner(*args,**kwargs):
        print(111)
        ret = f(*args,**kwargs)
        print(222)
        return ret
    return inner
def func():
    print(333)
print(444)
func()
print(555)



# 编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里’。
lst = []

def wrapper(func):
    def inner(*args,**kwargs):
        print("每次执行被装饰函数之前都得先经过这里")
        ret =  func(*args,**kwargs)
        return ret
    return inner

@wrapper
def func():
    for i in range(4):
        lst.append(i)
    return lst
print(func())


# 函数写一个装饰器，把函数的返回值 +100 然后再返回。

def wrapper(func):
    def inner(*args,**kwargs):
        # 这里是函数执行前的操作
        ret = func(*args,**kwargs)
        # 这里是函数执行后的操作
        ret = ret +100
        return ret
    return inner
@wrapper
def func():
    return 7
result = func()
print(result)

# 请实现一个装饰器，通过一次调用使被装饰的函数重复执行5次。

def wrapper(func):
    def inner(*args,**kwargs):
        # 这里是函数执行前的操作
        ret = func(*args,**kwargs)
        # 这里是函数执行后的操作
        for i in range(5):
            print(ret)
        return ret
    return inner

@wrapper
def func():
    return "yaya"
func()



# 请实现一个装饰器，每次调用函数时，将被装饰的函数名以及调用被装饰函数的时间节点打印出来
import time
# start_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",start_time))
#
# def fun():
#     print(fun.__name__)
# fun()

def wrapper(func):
    def inner(*args,**kwargs):
        start_time = time.localtime()
        print(time.strftime("%Y-%m-%d %H:%M:%S",start_time))
        print("-------------------------------------------")
        print("function_name:",func.__name__)
        ret = func(*args,**kwargs)
        return ret
    return inner

@wrapper
def func():
    print("123")
func()





# 请实现一个装饰器，每次调用函数时，将被装饰的函数名以及调用被装饰函数的时间节点写入文件

import time
def wrapper(func):
    def inner():
        ret = func()
        for i in range(5):
            time.sleep(1)
            struct_time = time.localtime()
            t = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
            name = func.__name__
            with open("times.txt","a",encoding="utf-8") as f:
                f.write(f"{name}\t")
                f.write(f"{t}\n")
        return ret
    return inner
@wrapper
def func():
    return "时间节点"
print(func())





# 请实现一个装饰器，限制该函数被调用的频率，如2秒一次（面试题）
import time
def wrapper(f):
    def inner(*args,**kwargs):
        for i in range(5):
            f(*args,**kwargs)
            time.sleep(3)
    return inner

@wrapper
def func():
    print("yaya")
    return "2s"
func()



#代码分析
def say_hi(func):
  def wrapper(*args,**kwargs):
      print("HI")
      ret=func(*args,**kwargs)
      print("BYE")
      return ret
  return wrapper

def say_yo(func):
  def wrapper(*args,**kwargs):
      print("Yo")
      return func(*args,**kwargs)
  return wrapper
@say_hi
@say_yo
def func():
  print("ROCK&ROLL")
func()

# HI
# Yo
# ROCK&ROLL
# BYE

# 使用装饰器

msg = """
>>>> 1.富贵村
>>>> 2.木匠王富贵
>>>> 3.铁匠王富贵
>>>> 4.裁缝王富贵
>>>> 5.网红村
>>>> 6.老八秘制小汉堡
>>>> 7.giao桑，故乡的樱花开了
VVVVVV 请在下面输入数字
"""

login_dic = {"name":None,"flag": False,"app":None}
def auth(argv):
    def wrapper(func):
        def inner(*args,**kwargs):
            if argv == "FG":
                if login_dic["name"] != None:
                    if login_dic["app"] == "FG":
                        func()
                else:
                    user = input(">输入账号")
                    pwd = input(">输入密码")
                    with open("login.txt","r",encoding="utf-8") as f:
                        for line in f:
                            k,v = line.strip().split(":")
                            if user == k and pwd == v:
                                print("welcome to 富贵村！")
                                login_dic["flag"] = True
                                login_dic["app"] = "FG"
                                login_dic["name"] = "FG"
                                func()
                            else:
                                print("ERROR USERNAME OR PASSWORD!")
            elif argv == "WH":
                if login_dic["name"] != None:
                    if login_dic["app"] == "WH":
                        func()
                else:
                    user = input(">输入密码")
                    pwd = input(">输入账号")
                    with open("login2.txt","r",encoding="utf-8") as f:
                        for line in f:
                            k,v = line.strip().split(":")
                            if user == k and pwd == v:
                                print("welcome to 网红圣地")
                                login_dic["flag"] = True
                                login_dic["app"] = "WH"
                                login_dic["name"] = "WH"
                                func()
                            else:
                                print("ERROR USERNAME OR PASSWORD!")
        return inner
    return wrapper


@auth("FG")
def func1():
    print("我是村长王富贵!")

@auth("FG")
def func2():
    print("我是木匠王富贵!")

@auth("FG")
def func3():
    print("我是铁匠王富贵!")

@auth("FG")
def func4():
    print("我是裁缝王富贵!")


@auth("WH")
def func5():
    print("我是网红代表!")

@auth("WH")
def func6():
    print("老八秘制小汉堡!")

@auth("WH")
def func7():
    print("123!")

while 1:
    Choose = input(msg)
    func_dic = {
        "1":func1,
        "2":func2,
        "3":func3,
        "4":func4,
        "5":func5,
        "6":func6,
        "7":func7
    }
    if func_dic.get(Choose):
        func_dic[Choose]()
    else:
        print("ERROR Number!")



