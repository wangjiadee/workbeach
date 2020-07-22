"""
模块是什么？
模块就是文件

Python的模块分为3类

1.内置模块
2.第三方模块，第三方库
3. 自定义模块


import 模块 
第一次导入模块 会加载到内存当中，只要程序不消失， 之后的从程序中寻找，
接下来你在引用多少次,它会先从内存中寻找有没有此模块,如果已经加载到内存,就不在重复加载.

第一次导入模块发生类三件事情
1.在内存中创建一个ralph命名空间
2.执行这个名称空间的可执行代码
3.通过ralph.的方式引用模块里面的代码

"""


# 引入模块  同时会执行代码 
import ralph
print(ralph.name)
ralph.read1()



name = 'yaya'
# 被导入模块有独立的名称空间
ralph.change()   #barry
print(name)      #yaya
print(ralph.name)


"""
模块起名的规范：
1. 简单 便捷  不使用长名字
"""

import ralph as sm
print(sm.name)


# 为模块起名
result = input(">>>>input>")
if result == 'mysql':
    import mysql1 as sm
elif result == 'oracle':
    import oracle1 as sm
sm.db()



"""
import 导入规范

import time, os, sys  # 这样写不对
# 应该向以下这种写法:
import time
import os
import sys

"""