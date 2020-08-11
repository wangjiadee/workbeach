'''
Author: your name
Date: 2020-08-10 17:49:34
LastEditTime: 2020-08-11 15:02:06
LastEditors: Please set LastEditors
Description: 登录注册功能结合面向对象
FilePath: \workbeach\Object\Object_loading_server.py
'''

"""
NOTES: 

hasattr() 函数用于判断对象是否包含对应的属性。
    class Coordinate:
        x = 10
        y = -5
        z = 0
    
    point1 = Coordinate() 
    print(hasattr(point1, 'x'))
    print(hasattr(point1, 'y'))
    print(hasattr(point1, 'z'))
    print(hasattr(point1, 'no'))  # 没有该属性


callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。

getattr() 函数用于返回一个对象属性值。
    >>>class A(object):
    ...     bar = 1
    ... 
    >>> a = A()
    >>> getattr(a, 'bar')        # 获取属性 bar 值
    1
    >>> getattr(a, 'bar2')       # 属性 bar2 不存在，触发异常
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'A' object has no attribute 'bar2'
    >>> getattr(a, 'bar2', 3)    # 属性 bar2 不存在，但设置了默认值
    3
"""

class User:
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        """
        save user_info
        """
        self.user_list = []
    
    def Login(self):
        """
        login function
        """
        for c in range(3):
            if not self.user_list:
                print(">>>>>Pls Register Fisrt!")
                return
            username = input("Pls input u username：")
            password = input("Pls input u password：")
            for i in self.user_list:
                if username == i.name and password == i.pwd:
                    print("Loding success!")
                    return
                print("ERROR: Incorrect account or password")
                
    def Register(self):
        """
        Register method
        """
        while True:
            while True:
                Username = input("Pls input u username:")
                Password = input("Pls input u password:")
                Second_password = input("Pls input u password again:")
                if Password == Second_password:
                    break
                print("Error：Entered passwords differ！")
            # 判断在不在存储列表里面：
            if not self.user_list:
                new_userinfo = User(Username,Password)
                self.user_list.append(new_userinfo)
                return
            for i in self.user_list:
                if Username != i.name:
                    new_userinfo = User(Username,Password)
                    self.user_list.append(new_userinfo)
                    return
                print("This username has been registered")
                
    def Run(self):
        """
        main process
        """
        INFO_LIST = ['Login','Register']
        while True:
            while True:
                for i in enumerate(INFO_LIST):
                    print(i[0]+1,i[1])
                User_Choose = input("Pls Choose u action:(Q breark)")
                if User_Choose.upper() == 'Q':
                    return
                elif User_Choose.isdecimal():
                    if int(User_Choose) == 1 or int(User_Choose) == 2:
                        break
                print("ERROR: Illegal input")
            User_Choose = int(User_Choose)
            if hasattr(self,INFO_LIST[User_Choose - 1]):
                if callable(getattr(self, INFO_LIST[User_Choose - 1])):
                    getattr(self, INFO_LIST[User_Choose - 1])()
                

#######################main function start #############
if __name__ == '__main__':
    obj = Account()
    obj.Run() 