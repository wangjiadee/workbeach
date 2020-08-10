'''
Author: Ralph
Date: 2020-08-10 16:54:54
LastEditTime: 2020-08-10 17:31:53
LastEditors: Please set LastEditors
Description: Property 案例
FilePath: \workbeach\Object\Object_property.py
'''

"""
@property 
将方法伪装成属性，在调用这个方法的时候 不在需要括弧
"""
import  time
from math import pi
class Yuan():
    def __init__(self,r):
        self.r = r
    @property
    def area(self):
        return pi * self.r **2
c1 = Yuan(5)
# print(c1.area())   # 没有加property
print(c1.area)



class Student():
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday
    @property
    def Student_age(self):  #装饰的方法是不能有参数的
        return time.localtime().tm_year - self.birthday
tom  =  Student('TOM',1998)
print(tom.Student_age)


# property 和私有的属性合作
class USER(object):
    def __init__(self,username,password):
        self.username = username
        self.__password = password
    @property
    def See_Password(self):
        return self.__password

userone = USER('userone','mdzz')
print(userone.See_Password)


class Root(object):
    exp_add_port = 0.88
    def __init__(self,Grade,exp):
        self.Grade = Grade
        self.__exp = exp
    @property 
    def Last_exp(self):
        return self.__exp * self.exp_add_port
    @Last_exp.setter  #名字必须是一样的
    def Last_exp(self,se_value):
        print("ERROR! It is security method!")
    

zhanshi = Root('player1',10)
print(zhanshi.Last_exp)  # 被property所装饰
zhanshi.Last_exp = 99    # 被setter装饰的