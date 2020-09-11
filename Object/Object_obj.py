# __call__
# callable 判断能不能运行
# 对象加括号 调用对应__call__下面的逻辑 对象() 调用这个类中的call方法
class A:
    def __call__(self,*args,**kwargs):
        print('9999')
obj = A()
print(callable(obj))
obj()




# __len__  len(obj) 需要实现这个类中__len__的方法

class Cls:
    def __init__(self,name):
        self.name = name
        self.Student = []
    def __len__(self):
        return len(self.Student)
        
Ralph = Cls('Ralph')
Ralph.Student.append('123')
Ralph.Student.append('321')
print(len(Ralph))



class Pow:
    def __init__(self,n):
        self.n = n
    
    def __pow2__(self):
        return self.n **2

def pow2(obj):
    return obj.__pow2__()

obj =Pow(10)  #实例化对象
print(pow2(obj))