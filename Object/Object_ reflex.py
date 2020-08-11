'''
Author: Ralph
Date: 2020-08-11 17:56:08
LastEditTime: 2020-08-11 18:06:47
LastEditors: Please set LastEditors
Description: python 的反射
FilePath: \workbeach\Object\Object_ reflex.py
'''



"""
NOTES: 
用字符串数据类型的名字来操作这个名字的函数、变量、绑定方法等
调用已知的str变量 可以使用反射来调用他


******
被导入的模块叫模块
当前执行的py文件叫脚本

对象名称.属性名称 ==> getattr(对象名.'属性名')


sys.modules['__main__']   ==> 表示当前模块的名称空间 存储当前模块的变量
"""

# name ="vivo"
# age = 30
# n = input(">>>>")
# if n == 'name' :print(name)
# elif n == 'age':print(age)


class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def student(self):
        print("hi,teacher")

tom = Person('tom','001')
ralph = Person('ralph','200')
# print(tom.id)
ret = getattr(tom,'student')
print(ret)
#可以直接调用里面的方法
ret()



class A:
    id = 'B6666'
    def __init__(self):
        self.name = 'vvvv'
        self.age = 11

    def func(self):
        print('fucking')
        return 6


# 反射对象的实例变量
a = A()
print(getattr(a,'name')) 
# 反射对象的绑定方法
print(getattr(a,'func')())
# 反射对象的静态变量
print(getattr(a,'id'))


import a
print(a.lis)
print(getattr(a,'lis'))
print(getattr(a,'ralph')())



