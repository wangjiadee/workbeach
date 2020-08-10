'''
Author: Ralph   
Date: 2020-08-10 14:20:09
LastEditTime: 2020-08-10 16:33:34
LastEditors: Please set LastEditors
Description: python 面向对象 封装
FilePath: \workbeach\Object\Object_package.py
'''


"""
Notes：
封装的广义定义：把属性或者方法封装起来，外部不能直接调用，要通过类的名字来调用
封装的狭义定义：把属性和方法藏起来，外部根本不能调用


私有的对象属性：
特点： 只能在类的内部使用
语法： 私有的静态变量、私有的实例变量、私有的绑定方法


"""
import hashlib
class User(object):
    # 所有的封装都是在类的内部所执行的
    __port = '127.0.0.1'                #私有的静态变量
    def __init__(self,UserName, Password):
        self.UserName = UserName
        self.__Password = Password      #私有的实例变量/私有的对象属性
        # 给名字前面加一个双下划线，变量即变成了私有的
    
    def __Get_Md5(self):                #私有的绑定方法
        md5 = hashlib.md5(self.UserName.encode('utf-8'))
        md5.update(self.__Password.encode('utf-8'))
        return md5.hexdigest()
    
    def Get_Password(self):
        return self.__Get_Md5()
    
u = User('ralph','12321')
# print(u.__Password)                     # 报错
# print(User.port)                        # 报错
# print(u.Get_Password())
# u.__Get_Md5()                           # 报错
print(u.Get_Password())
print('^^' * int(50))


# 私有的内容不能被子类继承
class Fucking(object):
    def __init__(self):
        self.__func()
    def __func(self):
        print('FUcking u futher')
class Notice(Fucking):
    def __func(self):
        print("Fucking u")
Notice()
print('^^' * int(50))


# public 公用的  ---> 内外都可以使用 能继承
# private 私有的 ---> 本类的内部使用 不能继承