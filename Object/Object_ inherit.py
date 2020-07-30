'''
@Author: Ralph
@Date: 2020-07-30 11:08:27
@LastEditTime: 2020-07-30 20:00:35
@LastEditors: Please set LastEditors
@Description: python面向对象的继承
@FilePath: \workbeach\Object\Object_ inherit.py
'''


class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s is eating" % self.name)

    def drink(self):
        print('%s is drinking' % self.name)

    def sleep(self):
        print('%s is sleeping' % self.name)

    def climb_tree(self):
        print('%s is climbing' % self.name)


class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('%s is eating' % self.name)

    def drink(self):
        print('%s is drinking' % self.name)

    def sleep(self):
        print('%s is sleeping' % self.name)

    def house_keep(self):
        print('%s house keeping' % self.name)


small_cat = Cat('small_cat')
small_cat.eat()
small_cat.drink()

big_dog = Dog('big_dog')
big_dog.eat()
print('*' * int(20))


"""
继承 -- 可以解决代码重复的问题

 class A:
     pass
 class B(A):
     pass
 B继承A,A是父类,B是子类
 A是父类 基类 超类
 B是子类 派生类
子类可以使用父类中的 : 方法 静态变量
"""


class Person:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def eat(self):
        print('%s is eating' % self.name)

    def drink(self):
        print('%s is drinking %s' % (self.name, self.food))

    def sleep(self):
        print('%s is sleeping' % self.name)
# 父类的继承


class Student(Person):
    def study(self):
        print('%s studing somethings!' % self.name)
    # 当子类和父类的方法重名的时候,我们只使用子类的方法,而不会去调用父类的方法了

    def eat(self):
        print("%s eating sth and studing" % self.name)
# 父类的继承


class Teacher(Person):
    def __init__(self, name, food, salary):
        Person.__init__(self, name, food)  # 调用了父类的初始化,去完成一些通用属性的初始化
        self.salary = salary             # 派生属性

    def teach(self):
        print('%s teaching somethings!' % self.name)

    def drink(self):
        # 子类想要调用父类的方法的同时还想执行自己的同名方法
        # 在子类的方法中调用父类的方法 :父类名.方法名(self)
        Person.drink(self)


# 先开辟空间,空间里有一个类指针-->指向Student
# 调用init,对象在自己的空间中找init没找到,到Student类中找init也没找到,
# 找父类Person中的init
tom = Student('tom', 'tea')
tom.study()
tom.eat()   # 当子类和父类的方法重名的时候,我们只使用子类的方法,而不会去调用父类的方法了

sila = Teacher('sila', 'coco', '88888')
sila.drink()
sila.teach()
print(sila.__dict__)
print('*' * int(20))


class Foo:
    def __init__(self):
        self.func()   # 在每一个self调用func的时候,我们不看这句话是在哪里执行,只看self是谁

    def func(self):
        print('in foo')


class Son(Foo):
    def func(self):
        print('in son')


Son()
print('*' * int(20))


"""
单继承与多继承

单继承
调子类的 : 子类自己有的时候
调父类的 : 子类自己没有的时候
调子类和父类的 :子类父类都有,在子类中调用父类的

多继承
一个类有多个父类,在调用父类方法的时候,按照继承顺序,先继承的就先寻找
"""

# 单继承


class D:
    def func(self):
        print('in D')


class C(D):
    pass


class A(C):
    def func(self):
        print('in A')


class B(A):
    pass


B().func()  # in A
print('*' * int(20))


# 多继承 有好几个爹
# 有一些语言不支持多继承 java
# python语言的特点 : 可以在面向对象中支持多继承
class B:
    def func(self):
        print('in B')


class A:
    def func(self):
        print('in A')


class C(B, A):
    pass


# B的父类在前面 就先输出B 如果A在前面就输出A
C().func()
