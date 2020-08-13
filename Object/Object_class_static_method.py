'''
Author: Ralph
Date: 2020-08-13 14:30:24
LastEditTime: 2020-08-13 14:31:39
LastEditors: Please set LastEditors
Description: classmethod 和staticmethod
FilePath: \workbeach\Object\Object_class_static_method.py
'''
# classmethod 把一个对象绑定的方法 修改成一个类方法
# 在方法中仍然可以引用类中的静态变量
# 可以不用实例化对象，就直接用类名在外包调用方法

# 开发规范！
import time
class Good():
    __discount = 0.8
    def __init__(self):
        self.__price = 5
        self.price = self.__price * self.__discount
# 定义了一个方法，默认传了一个self，但是没有使用
    # def change_discount(self,new_dis):
        # Good.__discount = new_dis
# cls 默认指向了自己所在的类
    @classmethod
    def change_discount(cls,new_dis):
        print(cls,Good)
        cls.__discount = new_dis
# oppo_finx = Good()
# print(oppo_finx.price)
# 使用了classmethod 可以用类名调用：
Good.change_discount(0.6)
vivo = Good()
print(vivo.price)

# 同时还可以使用对象名调用
vivo.change_discount(0.5)
oppo2 = Good()
print(oppo2.price)

print('^' * int(60))


class Date:
    def __init__(self,year,mouth,day):
        self.year = year
        self.mouth = mouth 
        self.day = day
    @classmethod
    def today(cls):
        struct_t = time.localtime()
        date = cls(struct_t.tm_year,struct_t.tm_mon,struct_t.tm_mday)
        return date

dtime = Date.today()
print(dtime.year,dtime.mouth,dtime.day)



# @staticmethod 被装饰的方法成为静态方法
# 一个函数 在类的内部执行 就用到staticmenthod

class User():
    pass

    @staticmethod
    def Login():
        print('LOGIN')

User.Login()

#能定义在类里面的方法：
# 1  静态变量-----所有对象共享  
# 2  绑定方法-----自带self参数的函数           由对象调用
# 3  类方法------是自带cls的参数               由对象或者类调用
# 4  静态方法-----啥都不带的普通函数           由对象或者类调用
# 5  property属性---- 是一个伪装成属性的方法   由对象调用 但是不加括号


class EG:
    com = 'huawei'            #1
    def func(self):
        print(self.__dict__)  #2
    @classmethod
    def clas_func(cls):
        print(cls)            #3
    @staticmethod
    def static_func():
        print('#4')
        
    @property
    def name(self):
        return '#5'

