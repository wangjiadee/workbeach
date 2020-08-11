'''
Author: Ralph
Date: 2020-08-11 15:07:57
LastEditTime: 2020-08-11 16:37:52
LastEditors: Please set LastEditors
Description: 使用面向对象的json和pickle
FilePath: \workbeach\Object\Object_pickle_json.py
'''


import pickle
import json
import sys



"""
sys.modules['__main__']找到当前运行的模块
"""
class M_Pickle:
    def __init__(self,path):
        self.path = path
        self.__count = 1

    def m_dump(self,obj):
        with open(self.path,mode = 'ab') as file_handler:
            pickle.dump(obj,file_handler)

    def m_load(self,obj):
        with open(self.path,mode = 'rb') as file_handler:
            for i in range(self.__count):
                ret = pickle.load(file_handler)
        self.__count +=1
        return ret

class M_Json:
    def __init__(self,path):
        self.path = path
    
    def m_dump(self,item):
        with open(self.path,encoding='utf-8',mode='a') as file_handler:
            json.dump(item,file_handler)
            
    def m_load(self):
        with open(self.path,encoding="utf-8",mode= 'a') as file_handler:
            ret = json.load(file_handler)
            return ret

Test = (1,2,3)
path = input('>>>>>Input u path:')
mode = input('>>>>>Json or Pickle:')
mode = 'M_' + mode

if hasattr(sys.modules['__main__'],mode):
    if callable(getattr(sys.modules['__main__'],mode)):
        obj = getattr(sys.modules['__main__'],mode)(path)
        obj.m_dump(Test)
    