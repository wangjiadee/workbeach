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



# python2 解决编码的问题
"""
python在安装时，默认的编码是ascii，当程序中出现非ascii编码时，python的处理常常会报错
UnicodeDecodeError: 'ascii' codec can't decode byte 0x?? in position 1: ordinal not in range(128)，
python没办法处理非ascii编码的，此时需要自己设置python的默认编码，一般设置为utf8的编码格式。

以下是python2的写法，但是在python3中这个需要已经不存在了，这么做也不会什么实际意义。
在Python2.x中由于str和byte之间没有明显区别，经常要依赖于defaultencoding来做转换。
在python3中有了明确的str和byte类型区别，从一种类型转换成另一种类型要显式指定encoding。
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')

