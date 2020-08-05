'''
@Author: ralph
@Date: 2020-07-24 10:54:34
@LastEditTime: 2020-07-24 11:08:01
@LastEditors: Please set LastEditors
@Description: Python 异常处理
@FilePath: \python\workbeach\module\sys_module.py
'''


"""
python 检查异常处理和状态
"""

try:
    sys.exit(1)
except SystemExit as e:
    print(e)