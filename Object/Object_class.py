'''
@Author: Ralph
@Type_file: Python
@Date: 2020-07-25 17:27:49
@LastEditTime: 2020-07-25 17:51:23
@FilePath: \workbeach\Object\Object_class.py
@Effect: 面向对象的类
'''
# 先来定义模子,用来描述一类事物
# 具有相同的属性和动作

# 必须叫__init__这个名字,不能改变的,
# 所有的在一个具体的人物出现之后拥有的属性


class Person:
    def __init__(self, name, sex, job, hp, weapon, ad):
        self.name = name
        self.sex = sex
        self.job = job
        self.level = 0
        self.hp = hp
        self.weapon = weapon
        self.ad = ad


class Dog():
    def __init__(self, name, blood, aggr, kind):
        self.dog_name = name
        self.hp = blood
        self.ad = aggr
        self.kind = kind


小白 = Dog('小白', 5000, 249, '柴犬')
print(小白.dog_name)
print(小白.__dict__)

# alex 就是对象
# alex = Person()的过程 是通过类获取一个对象的过程 - 实例化
alex = Person('alex', '不详', '搓澡工', 260, '搓澡巾', 1)
print(alex, alex.__dict__)

wusir = Person('wusir', 'male', '法师', 500, '打狗棍', 1000)
print(wusir, wusir.__dict__)


# 属性的查看：
print(alex.name)

# 属性的修改
alex.name = 'alexsb'
print(alex.name)

# 属性的增加
alex.money = 1000000
print(alex.money)
print(alex.__dict__)

# 属性的删除
del alex.money
print(alex.__dict__)


"""
类名() 会自动调用类中的__init__方法
类和对象之间的关系?
    类 是一个大范围 是一个模子 它约束了事物有哪些属性 但是不能约束具体的值
    对象 是一个具体的内容 是模子的产物 它遵循了类的约束 同时给属性赋上具体的值

Person是一个类 :alex wusir都是这个类的对象
类有一个空间,存储的是定义在class中的所有名字
每一个对象又拥有自己的空间,通过对象名.__dict__就可以查看这个对象的属性和值

实例化所经历的步骤
    1.类名() 之后的第一个事儿 :开辟一块儿内存空间
    2.调用 __init__ 把空间的内存地址作为self参数传递到函数内部
    3.所有的这一个对象需要使用的属性都需要和self关联起来
    4.执行完init中的逻辑之后,self变量会自动的被返回到调用处(发生实例化的地方)

"""

# 修改列表\字典中的某个值,或者是对象的某一个属性 都不会影响这个对象\字典\列表所在的内存空间
d = {'k': 'v'}
print(d, id(d))  # 1356845745928
d['k'] = 'vvvv'
print(d, id(d))  # 1356845745928


# =====================================================================
# 定义一个圆形类,半径是这个圆形的属性,实例化一个半径为5的圆形,一个半径为10的圆形
class Yuan():
    def __init__(self, R):
        self.mianji = R * R * 3.14
        self.zhouchang = 2*R*3.14


y1 = Yuan(5)
y2 = Yuan(10)
print(y1.mianji)
print(y2.mianji)
print(y1.__dict__)
print(y2.__dict__)

# 定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


ralph = User('ralph', 123123)
xj = User('xiejier', 321321)
print(ralph.__dict__)
print(xj.__dict__)
