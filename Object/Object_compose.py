'''
@Author: Ralph
@Type_file: Python
@Date: 2020-07-28 14:34:03
@LastEditTime: 2020-07-30 11:06:02
@FilePath: \workbeach\Object\Object_compose.py
@Effect: 面向对象的组成
'''


"""
组合
一个类的对象同时也是另一个类的对象

# 学生类
    # 姓名 性别 年龄 学号 班级 手机号
# 班级信息
    # 班级名字
    # 开班时间
    # 当前讲师
"""


class Student:
    def __init__(self, name, sex, age, number, cla, phone):
        self.name = name
        self.sex = sex
        self.age = age
        self.number = number
        self.cla = cla
        self.phone = phone


class Clas:
    def __init__(self, cname, begintime, teacher):
        self.cname = cname
        self.begintime = begintime
        self.teacher = teacher


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price


test = Clas('v1', '2020-01-01', 'vv1')
test2 = Clas('v2', '2020-02-01', 'vv2')
name1 = Student('name1', 'male', 18, 27, test, 13812012012)
name2 = Student('name2', 'male', 18, 17, test2, 13812012013)
test3 = Clas('v3', '2020-03-01', 'vv3')
test4 = Clas('v4', '2020-04-01', 'vv4')
go = Course('go01', '3M', 58888)
python = Course('python01', '6M', 29999)
test3.course = python
test4.course = go
print(test3.course.period)
print(test4.course.price)
print(name1.cla, test)
print(test.begintime)
print(name2.cla.begintime)




from math import pi
class Circle:
    def __init__(self,r):
        self.r = r
    
    def area(self):
        return pi * self.r**2
    
    def perimeter(self):
        return pi *2*self.r
    


class Ring:
    def __init__(self,o_r,i_r):
        #对参数大小进行排序
        o_r,i_r = (o_r,i_r) if o_r > i_r else (i_r,o_r)
        #内部实例化
        self.o_r = Circle(o_r)     
        self.i_r = Circle(i_r)
    def area(self):
        return self.o_r.area() - self.i_r.area()
    def perimeter(self):
        return self.o_r.perimeter() + self.i_r.perimeter()

r= Ring(10,8)
# print(r)