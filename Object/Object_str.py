'''
Author: Ralph
Type_file[python//GO//json//Yaml//Other]: [python]
Date: 2020-09-12 02:21:48
LastEditTime: 2020-09-12 02:59:17
FilePath: /pyenv/str.py
Effect: str repr 用法
'''
#__str__  (__repr__)用法一样
# 当我们打印一个对象 用%s进行字符串拼接 或者str(对象)总是调用这个对象的__str__方法
# 如果找不到__str__,就调用__repr__方法
# __repr__不仅是__str__的替代品,还有自己的功能
# 用%r进行字符串拼接 或者用repr(对象)的时候总是调用这个对象的__repr__方法
# 在打印一个对象的时候 调用__str__方法
# 在%s拼接一个对象的时候 调用__str__方法
# 在str一个对象的时候 调用__str__方法

class Course:
    def __init__(self, n, p, q):
        self.n = n
        self.p = p
        self.q = q


demo1  = Course("demo1",1,"d1")
demo2  = Course("demo2",2,"d2")
demo3 = Course("demo3",3,"d3")
demo4 = Course("demo4", 4, "d4")

lst = [demo1, demo2, demo3, demo4]
for index, c in enumerate(lst, 1):
    print(index, c.n, c.p, c.q)
# num = int(input(">>>"))
# course = lst[num - 1]
# print(course.n, course.p)



class Dourse:
    def __init__(self, n, p, q):
        self.n = n
        self.p = p
        self.q = q
    def __str__(self):
        return ','.join([self.n,str(self.p),self.q])


demo5 = Dourse("demo5",5,"d5")
demo6 = Dourse("demo6",6,"d6")

lst = [demo5, demo6]
for i in lst:
    print(i)



class cla(object):
    def __init__(self):
        self.pop = []
    def append(self,name):
        self.pop.append(name)
    def __str__(self):
        return str(self.pop)

pop1 = cla()
print(pop1)
pop1.append("Love")
print(pop1)