'''
@Author: Ralph
@Type_file: Python
@Date: 2020-07-30 20:02:11
@LastEditTime: 2020-07-30 20:37:31
@FilePath: \workbeach\Object\Object_review.py
@Effect: python面向对象的小结
'''

"""
object 类
所有在python3中的类都继承了object了
"""




from types import FunctionType, MethodType
class A(object):
    pass


a = A()
print('*' * int(40))
# 1:开辟空间
# 2:调用init（object的）
# 3: 好习惯： class A（object） 默认加上 python2 和python3 不一样


class B(object):
    pass


print(B.__bases__)  # 默认输出父类的名字


class C:
    pass


class D(B, C):
    pass


print(D.__bases__)  # 只会显示上一级的父类的名字

print('*' * int(40))
"""
isinstance: 判断类型（和type 一样） 但同时可以判断父类
"""
a = 1
b = 'abc'
print(isinstance(a, int))
print('*' * int(40))


class Animal(object):
    pass


class Cat(Animal):
    pass


小白 = Cat()
print(type(小白) is Cat)         # True
print(type(小白) is Animal)      # False  type 类型判断不了父类
print(isinstance(小白, Cat))     # True
print(isinstance(小白, Animal))  # True isinstane可以判断父类
print('*' * int(40))


"""
绑定方法和普通函数
FunctionType: 函数
MethodType：方法
"""


class A:
    def func(self):
        print('in func')


print(A.func)  # 函数---->类名调用的函数就是函数   <function A.func at 0x0000025CA4839488>
a = A()
# 方法---->方法名调用的韩式就是方法   <bound method A.func of <__main__.A object at 0x0000025CA4829D68>>
print(a.func)
print(isinstance(a.func, FunctionType))  # F
print(isinstance(a.func, MethodType))  # T
print(isinstance(A.func, FunctionType))  # T
print(isinstance(A.func, MethodType))  # F
print('*' * int(40))

"""
一：我们定义的类的属性到底存到哪里了？有两种方式查看
dir(类名)：查出的是一个名字列表
类名.__dict__:查出的是一个字典，key为属性名，value为属性值

二：特殊的类属性
类名.__name__# 类的名字(字符串)
类名.__doc__# 类的文档字符串
类名.__base__# 类的第一个父类(在讲继承时会讲)
类名.__bases__# 类所有父类构成的元组(在讲继承时会讲)
类名.__dict__# 类的字典属性
类名.__module__# 类定义所在的模块
类名.__class__# 实例对应的类(仅新式类中)
"""


class Z:
    role = '法师'
    def func1(self): pass
    def func2(self): pass


class Y:
    pass


class W(Y, Z):
    pass


print(Z.__base__)
print(W.__base__)
print(W.__bases__)
print(Z.__dict__)
print(Z.__name__)
print(Z.__class__)
print(Y.__class__)
print(W.__class__)
print(W.__module__)
print('*' * int(40))


# import module

# __doc__
def Function():
    '''
    函数的注释
    '''


print(Function.__doc__)


class Cat:
    '''
    这个类是用来描述游戏中的猫咪角色
    '''
    pass


print(Cat.__doc__)
