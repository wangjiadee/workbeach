'''
Author: your name
Date: 2020-08-12 11:57:00
LastEditTime: 2020-08-12 11:58:36
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \workbeach\Python_Silent_writing.py
'''
"""
PYhton 默写集合
"""


# super 的默写


class User:
    def __init__(self,name):
        self.name = name

class VIPUser(User):
    def __init__(self,name,VIP_Level,start_Date,end_Date):
        super().__init__(name)
        # User.__init__(self.name)
        # super(VIPUser,self).__init__(bane)
        self.VIP_Level = VIP_Level
        self.start_Date = start_Date
        self.end_Date = end_Date
        
Tom = VIPUser('tom','VIP18','2020-02-02','2022-02-02')
print(Tom.__dict__)
        