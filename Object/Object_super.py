'''
Author: Ralph
Date: 2020-08-07 16:07:22
LastEditTime: 2020-08-07 17:14:11
LastEditors: Please set LastEditors
Description: Python super eg
FilePath: \workbeach\Object\Object_super.py
'''
# super 是按照mro顺序来寻找当前类的下一个类
# super 是可以传递参数的 python3 不需要传参数 python2 中的新式类是需要传递传递参数 (子类的名字.子类的对象).函数名
# 在python2 的经典类不支持super
# super(D,self).func() 在python2当中必须这样 但是在python3当中可以不用填写
 
class RA(object):
    def func(self):
        print("fucking!")

class RB(RA):
    def func(self):
        super(RB,self).func()
        print("Oppo Compare")
class RC(RA):
    def func(self):
        super(RC,self).func()
        print("MTK Compare")
class RD(RB,RC):
    def func(self):
        super(RD,self).func()
        print("ViVO Compare")
    
RD().func()
print('^' * int(40))



class User():
    def __init__(self,username):
        self.username = username
        
class VIP1_user(User):
    def __init__(self,username,userId):
        super().__init__(username)
        self.userId = userId
tom = VIP1_user('TOM','00001')
print(tom.__dict__)
        