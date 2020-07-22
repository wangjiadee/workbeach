"""
from ralph import name
from ralph import read1
from ralph import read2

print(name)

print(globals())
"""

"""
1.from...import 容易和本文件的名字产生冲突,后者将前者覆盖

name = 'alex'
from ralph import name
print(name)   #输出的不是alex

"""


"""
2. 当前位置直接使用read1和read2,执行时，仍然以ralph.py文件全局名称空间 
"""

#引用ralph中的read1的内存地址
#不是在本文件完全构建一个新的参数  相当于构建了一个变量read1 但是这个read1 指向的函数 还是原来文件的内存地址
from ralph import read1  
name = 'yaya'
read1()
print(globals())




from ralph import change
name = 'YAYA'
print(name)                # 依旧使用本次定义变量
change()                   #调用了ralph.change  ralph 的name指向的内存地址发生了变化
print(name)                #还是使用了本文件的变量
from ralph import name     #将本文件指向了ralph 的内存地址
print(name) #Barry

# 当前位置直接使用read1和read2,执行时，仍然以ralph.py文件全局名称空间 
# 只要是导入原来的
from ralph import read1
name = 'YY'
read1()




# form ralph import *
# 一般不能这样写  必须要记录所有的变量
# 如果要使用的话 要配合__all__ = [] 使用


"""
py文件的两个功能:
1. 自己用 脚本
2. 被别人引用 模块使用
"""
print(__name__) #如果是自己使用 运行结果是__main__
# 当ralph.py做模块被别人引用时: __name__ == ralph  输出py文件的名字



"""
__name__ 根据文件的扮演的角色(脚本,模块)不同而得到不同的结果
1, 模块需要调试时,加上 if __name__ == '__main__':
2, 作为项目的启动文件需要用.
"""