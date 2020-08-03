'''
@Author: Ralph
@Type_file: Python
@Date: 2020-08-03 14:13:41
@LastEditTime: 2020-08-03 16:35:48
@FilePath: \workbeach\Object\Object_inherit_order.py
@Effect: 继承的顺序
'''


"""
需要背诵:
在python3当作 所有的类都继承object类，只要继承object类就是新式类
因此python3中的类都是新式类

经典类：
在py3中不存在，但是在py2中有
所有 不继承object的类都是经典类，继承object的类都是新式类
"""

# 以下是请调用python2的环境:


class Python2_A:
    pass


class Python2_B(object):
    pass
# A 是经典类 B是新式类

# 以下请调用python3的环境：


class Python3_A:
    pass


class Python3_B(object):
    pass

# AB 都是新式类


"""
经典类和新式类的区别

1.在单继承方面中（无论是新式类还是经典类都是一样的一层一层的往上找）
object<---A<---B<---C<---D
如果实例化D的对象 先去找D 然后在一层一层的往上找(深度)

2.在多继承方面
D同时继承BC，BC都继承A

新式类的多继承：（广度优先）   经典类的多继承：（深度优先）
      A4                            A3
    /   \                          /   \
   /     \                        /     \
 B2      C3                      B2     C4 
   \     /                        \     /  
    \   /                          \   / 
      D1                             D1


# 经典类 都是深度优先，总是在一条路走不通时候在换一条路，不会走重复的路
"""

# 对于新式类 是默认认为广度有限


class A(object):
    def func(self):
        print('AAA')


class B(A):
    def func(self):
        print('BBB')


class C(A):
    def func(self):
        print('CCC')


class D(B, C):
    pass


# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())
# 以上方法只能在python3中使用
d = D()
d.func()


"""
新式类---广度优先 ---使用的是C3算法 --- 不是全部的先走广度的
     A6
B3       C5
D2       E4
    F1


C3算法：
先算出A类的
A(object) = [AO]
B(A) = [BAO]
C(A) = [CAO]
D(B) = [DBAO]
E(C) = [ECAO]
F(D,E)  = c3(D(B) + E(C))
        = [F] + [DBAO] + [ECAO]   #F本身自己出在最先 
F       = [DBAO] + [ECAO]         #D在第一个且没有在后面出现 可以提出D
FD      = [BAO] + [ECAO]          #B在第一个且没有在后面出现 可以提出B
FDB     = [AO] + [ECAO]           #A出现在第一个了 但是后面有A,不提取A
FDBE    = [AO] + [CAO]            #由于A的不提取 E出现在第一且后面没有 提出E
FDBEC   = [AO] + [AO]             #由于A的不提取 C出现在第一且后面没有 提出C
FDBECA  = [O] + [O]               #A出现在第一个 且后面也出现在了第一个 可以提出
FDBECAO 

C3算法的内容：
    如果是单继承：总是按照子类->父类的顺序来计算
    如果是多继承： 先按照自己的本类--父类1的顺序继承---父类2的顺序继承.....

"""
# C3 算法练习1
G(object) = [GO]
F(G) = [FGO]
D(G) = [DGO]
B(F) = [BFGO]
E() = [E]
C(E) = [CE]
A(B, C, D) = C3(B(F)+C(E)+D(G))
= [A] + [BFGO] + [CE] + [DGO]  # A本身自己出在最先

A = [BFGO] + [CE] + [DGO]  # B在第一个且没有在后面出现 可以提出B
AB = [FGO] + [CE] + [DGO]  # F在第一个且没有在后面出现 可以提出F
ABF = [GO] + [CE] + [DGO]
ABFC = [GO] + [E] + [DGO]
ABFCE = [GO] + [DGO]
ABFCED = [GO] + [GO]
ABFCEDG = [O] + [O]
ABFCEDGO
