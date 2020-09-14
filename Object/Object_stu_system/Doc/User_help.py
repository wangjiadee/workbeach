'''
Author: Ralph
Type_file[python//GO//json//Yaml//Other]: [python//GO//json//Yaml//Other]
Date: 2020-09-12 04:25:08
LastEditTime: 2020-09-12 05:54:44
FilePath: /pyenv/code/workbeach/Object/Object_stu_system/Doc/User_help.py
Effect: DO
'''
import os
import sys
import hashlib
# 输出文件父级目录
Base_Path1 = os.path.dirname(os.path.dirname(__file__))
# 输出文件的目录（绝对路径）
Base_Path2 = os.path.dirname(__file__)
print(Base_Path1)
#添加环境变量 能引入模块的地址
# sys.path.append(Base_Path)



#src文件：
"""
登录系统
1.登录三次
2.密码加密
3.数据文件读写
"""




#common.py文件

# ret = hashlib.md5()
# ret.update(n.encode("utf-8")) #n 表示要加密的字符
# ret.hexdigest() #返回16进制