'''
@Author: Ralph
@Type_file: Python
@Date: 2020-08-03 12:55:58
@LastEditTime: 2020-08-03 20:20:21
@FilePath: \workbeach\Object\Objec_ Polymorphism.py
@Effect: python 面向对象-多态和鸭子
'''

# 多态和鸭子
"""
一个类型表现出的多种状态
在java语音中 一个参数必须制定类型，所以要2个不同的类型的对象都可以传参 就需要让2个类型继承一个父类来实现

鸭子类型


"""


# def add(a, b):
#     return a + b


# # python里面是有约束的
# print(add(1, 'sdasd'))


class list:
    def __init__(self, *args):
        self.l = [1, 2, 3]

    def __len__(self):
        n = 0
        for i in self.l:
            n += 1
        return n


l = [1, 2, 3]
l.append(4)


def len(obj):

    return obj.__len__()


# 所有实现了__len__方法的类,在调用len函数的时候,obj都说是鸭子类型
# 迭代器协议 __iter__ __next__ 是迭代器
print(dir(str))


class list:
    def __len__(self): pass


class dict:
    def __len__(self): pass


class set:
    def __len__(self): pass


class tuple:
    def __len__(self): pass


class str:
    def __len__(self): pass


def len(鸭子类型看起来有没有实现一个__len__ obj):
    return obj.__len__()
