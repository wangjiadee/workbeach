'''
@Author: Ralph
@Date: 2020-07-23 13:36:48
@LastEditTime: 2020-07-30 21:09:39
@FilePath: \workbeach\module\pickle_module.py
@Effect: pickle 模块 和面向对象的补充
'''
import pickle


class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


tom = Person('tom', '20', '00001')
sali = Person('sali', '21', '00002')
ralph = Person('ralph', '22', '00003')

# with open('pickle_file', 'wb') as f:
#     pickle.dump(tom, f)
#     pickle.dump(sali, f)
#     pickle.dump(ralph, f)
with open('pickle_file', 'rb') as f:
    while True:
        try:
            ret = pickle.load(f)
            print(ret.__dict__)  # {'name': 'tom', 'age': '20', 'id': '00001'}
        except EOFError:
            break
