'''
Author: your name
Date: 2020-09-11 15:00:50
LastEditTime: 2020-09-11 15:00:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \workbeach\Object\Object_new.py
'''
i# __new__


class Demo:
    def __new__(cls,*args,**kwargs):  #构造方法
        print('Run new')
        return super().__new__(cls)
    
    def __init__(self):
        print("Run init")
        
Demo()

# 实例化 先创建空间 有一个指针能指向类   ----> __new__ 来完成
# 然后在调用init


#设计模式 --- 单例模式
#一个类从头到尾只会创建一次self的空间

class Demo1:
        def __new__(cls,*args,**kwargs):
            obj = super().__new__(cls)
            return obj
        def __init__(self,a,b):
            self.a = a 
            self.b = b

b1 = Demo1('1','2')
b2 = Demo1('3','4')
print(b1,b2) # <__main__.Demo1 object at 0x04ADD208> <__main__.Demo1 object at 0x04ADD340>


class Demo2:
        __instance = None
        def __new__(cls,*args,**kwargs):
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
            return cls.__instance
        def __init__(self,a,b):
            self.a = a 
            self.b = b


b1 = Demo2('1','2')
print(b1.a)
b2 = Demo2('3','4')   # <__main__.Demo2 object at 0x0471D400>  <__main__.Demo2 object at 0x0471D400>
print(b1,b2)
print(b1.a,b2.a)