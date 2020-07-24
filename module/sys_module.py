'''
@Author: ralph
@Date: 2020-07-24 10:54:34
@LastEditTime: 2020-07-24 11:08:01
@LastEditors: Please set LastEditors
@Description: sys 
@FilePath: \python\workbeach\module\sys_module.py
'''

"""
sys模块是与python解释器交互的一个接口
"""

import sys  

sys.argv           #令行参数List，第一个元素是程序本身路径
sys.exit(n)        #退出程序，正常退出时exit(0),错误退出sys.exit(1)
sys.version        #获取Python解释程序的版本信息
sys.path           #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       #返回操作系统平台名称



"""
python 检查异常处理和状态
"""

try:
    sys.exit(1)
except SystemExit as e:
    print(e)