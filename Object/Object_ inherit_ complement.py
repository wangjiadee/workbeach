'''
@Author: Ralph
@Date: 2020-07-30 11:08:27
@LastEditTime: 2020-08-03 13:43:23
@LastEditors: Please set LastEditors
@Description: python面向对象的继承的补充
@FilePath: \workbeach\Object\Object_ inherit_ complement.py
'''

# 继承  是通过继承来解决代码重复的问题

# 进阶：
# 多继承的继承顺序问题
# 通过继承的类的开发规划


"""
面向对象的内容回顾
1.类
class 类名：
    静态变量 = '值'
    def 函数（self）：
        "内容"
        pass
    def 函数2

1.1 所有的变量和函数的地址都存储在类的命名空间里面

2.对象
    对象 = 类名（）

3.怎么用
    类的作用： 实例化对象   能操作静态变量
3.1 什么时候是对类中的变量赋值或者使用类的变量
    类名.名字 = ‘值’
    print（类名.名字）
    print（对象名.名字）  
3.2 对对象中的变量赋值
    self.名字
    对象.名字  
    以上2个是一样的意思

4.怎么继承
"""


class Eg(object):
    role = []

    def __init__(self):
        self.list = []

    def append(self, obj):
        self.list.append(obj)

    def pop(self, index=-1):
        self.list.pop(index)


print(Eg.role)  # .前面是找内存地址
a = Eg()  # 重新实例化了一个新的名称空间
# 实例化的时候 是先开辟空间 在调用__init__
# 然后调用init的时候，总是把新开的空间作为参数传递给self

# 所有的对象调用的方法 就是看这个对象是哪一个类的对象 不需要看所有的类的方法名字是否一样，不影响


class Queue(object):
    def __init__(self):
        self.lst = []

    def append(self, value):
        pass

    def pop(self):
        pass


q = Queue()       # []
q.lst.append(10)  # 对列表中添加了append 10 [10]
q.append(5)       # 用的queue类中的append 不是list里面的 所以没有执行
print(q.lst)      # [10]
q.pop()           # 调用了q的pop 没有执行
print(q.lst)      # 不变来是[10]


# 如何继承

# 写代码的时候 从思考的角度上来说：
# 在加载代码的时候 是先加载父类 所以父类写在前面
# 先写子类的全部代码 然后去寻找重复的代码 然后把重发的代码放到父类
class futher(object):
    def futher_func(self):
        print('futher')


class son(futher):
    def son_func(self):
        print('son')


s = son()
s.son_func()
print('*' * int(50))
