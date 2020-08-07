'''
@Author: Ralph
@Type_file: Python
@Date: 2020-07-28 10:30:54
LastEditTime: 2020-08-07 14:08:59
@FilePath: \workbeach\Object\Object_namespaces.py
@Effect: python 面向对象的命名空间
'''
"""
# 命名空间
    # 在类的命名空间里 : 静态变量 绑定方法
    # 在对象的命名空间里 : 类指针 对象的属性(实例变量)

    # 调用的习惯
        # 类名.静态变量
        # 对象.静态变量 (对象调用静态变量的时候,不能对变量进行赋值操作 对象.静态变量 = 1UI27)

        # 绑定方法
        # 对象.绑定方法() # ==> 类名.绑定方法(对象)

"""
class A:
    # 静态变量/静态属性 存储在类命名空间里面
    Compass = 'oppo'
    # 绑定方法 存储在类的命名空间里面

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print(self)
    Compass = 'mdzz'
    print(Compass)


# print(A.__dict__)
# a = A('ralph', 100)
# print(A.Compass)
# a.func()  #  == A.func1(a)
"""
对象和类之间的关系：
1.对象总是可以找到自己的类，但是类不能反向找到自己的指针
2.类指针 存储在了类所在的内存地址
"""


class B:
    Compass = 'Oppo'

    def __init__(self, name, age, Compass):
        self.name = name
        self.age = age
        self.Compass = Compass

    def func(self):
        print(self)


# b = B('ralph', 22, 'tx')
# print(b)  # <__main__.B object at 0x0000022CBF3D9C88>
# print(b.Compass)
# print(B.Compass)


class C:
    Compass = 'Oppo'

    def __init__(self, name, age, Compass):
        self.name = name
        self.age = age
        self.Compass = Compass

    def func(self):
        print(self)


c = C('ralph', 12, 'vivo')
c1 = C('tom', 13, 'huawei')
c.Compass = 'zte'
print(c.Compass)  # zte
print(c1.Compass)  # huawei
print(C.Compass)  # Oppo


"""
类中的变量是静态变量
1:对象中的变量只属于对象本身,每个对象有属于自己的空间来存储对象的变量
2:当使用对象名去调用某一个属性的时候会优先在自己的空间中寻找,找不到再去对应的类中寻找
3:如果自己没有就引用类的,如果类也没有就报错
4:对于类来说,类中的变量所有的对象都是可以读取的,并且读取的是同一份变量

类中的静态变量的用处
1:如果一个变量 是所有的对象共享的值,那么这个变量应该被定义成静态变量
2:所有和静态变量相关的增删改查都应该使用类名来处理,而不应该使用对象名直接修改静态变量
"""


class D:
    pass


# 属性的添加
D.compass = 123
print(D.compass)

# 实现一个类,能够自动统计这个类实例化了多少个对象


class E:
    count = 0

    def __init__(self):
        E.count += 1


e1 = E()
print(e1.count)
e2 = E()
print(e2.count)


class F:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age

    def func1(self):
        print(self)


a = F('alex', 83, '印度')
b = F('wusir', 74, '阿富汗')
print(a.Country)  # 中国
F.Country = '伊拉克'
a.Country = '日本'
print(a.Country)  # 日本
print(b.Country)  # 伊拉克  *不是阿富汗 因为b 调用的也是F类里面的
print(F.Country)  # 伊拉克


class G:
    Country = ['中国']     # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age

    def func1(self):
        print(self)


a = G('alex', 83, '印度')
b = G('wusir', 74, '泰国')
print(b.Country)  # 中国
a.Country[0] = '日本'
print(a.Country)  # ['日本']
print(b.Country)  # 日本
print(G.Country)  # 日本


class H:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
        self.Country = country

    def func1(self):
        print(self)


a = H('alex', 83, '印度')
b = H('wusir', 74, '泰国')
H.Country = '英国'
a.Country = '日本'
print(a.Country)  # 日本
print(b.Country)  # 泰国
print(H.Country)  # 英国


class I:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age

    def Country(self):
        return self.Country


a = I('alex', 83, '印度')
b = I('wusir', 74, '泰国')
print(a.Country)
print(a.Country())


class Foo(object):
    n1 = 'zzz'
    def __init__(self,name):
        self.n2 = name
obj = Foo('bbb')
print(obj.n1)   #zzz
print(obj.n2)   #bbb
print(Foo.n1)   #zzz
print(Foo.n2)   #报错