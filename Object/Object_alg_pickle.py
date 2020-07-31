'''
@Author: Ralph
@Date: 2020-07-31 17:38:49
@LastEditTime: 2020-07-31 17:42:09
@LastEditors: Please set LastEditors
@Description: 面向对象和队列堆栈.pickle 
@FilePath: \python\workbeach\Object\Object_alg_pickle.py
'''


"""
内置的数据结构：
     {} kv 通过key找到v
     [] 序列 通过index取值
     () 元祖 
     {1,} 集合
     'sss' 字符串

不是python内置的数据结构：
    Queue 队列 （先进先出） FIFO
    stack 栈 （先进后出）LIFO
"""


import pickle
class Que_Sta(object):
    def __init__(self):
        self.list = []
    def get(self,item):
        self.list.append(item)
    def put(self):
        if self.inedx  == -1:
            print(self.list.pop())
        else:
            print(self.list.pop(0))
class Queue(Que_Sta):
    def __init__(self):
        self.index = -1
        Que_Sta.__init__(self)
class Stack(Que_Sta):
    def __init__(self):
        self.index = 0
        Que_Sta.__init__(self)

class Pickle(object):
    def __init__(self,file_path):
        self.file_path = file_path
    def Dump(self,obj):
        with open(self.file_path,mode="wb") as f:
            pickle.dump(obj,f)
    def Load(self):
        with open(self.file_path,mode= "rb") as f1:
            while True:
                try:
                    yield pickle.load(f1)
                except EOFError:
                    break
        
        
ret = Stack()
ret.get(1)
ret.get(2)
ret.get(3)
file1 = Pickle('pickle_file')
file1.Dump(ret)
print(file1.Load())
for i in file1.Load():
    print(i,i.list)