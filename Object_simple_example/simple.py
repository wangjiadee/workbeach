'''
Author: Ralph
Type_file[python//GO//json//Yaml//Other]: [python//GO//json//Yaml//Other]
Date: 2020-09-12 01:58:06
LastEditTime: 2020-09-12 02:21:01
FilePath: /pyenv/simple.py
Effect: DO
'''
class Baby(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

ba = Baby("1", "3")



class Demo2:
        __instance = None
        def __new__(cls,*args,**kwargs):
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
            return cls.__instance
        def __init__(self,a,b):
            self.a = a 
            self.b = b


b1 = Demo2('1','2')
print(b1.a)
b2 = Demo2('3','4')   # <__main__.Demo2 object at 0x0471D400>  <__main__.Demo2 object at 0x0471D400>
print(b1,b2)
print(b1.a, b2.a)



