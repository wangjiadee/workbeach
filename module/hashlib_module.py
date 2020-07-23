'''
@Author: Ralph
@Type_file: Python
@Date: 2020-07-23 16:20:08
@LastEditTime: 2020-07-23 20:15:03
@FilePath: \workbeach\module\hashlib_module.py
'''

"""
hashlib 包含各种加密算法 md5 sha系列

用途：
1.密码加密
2.文件的校验

用法：
1：将bytes类型的字节转换成 固定长度的16进制数字组成的字符串
2：不同的bytes利用相同的算法（md5）转化成的结果不同
3：相同的bytes利用相同的算法（md5）转化成的结果相同
4：hashlib算法不可以逆转


"""
# 普通的加密：
import hashlib
hashlib.md5()
s1 = 'xiejierbb520'
ret = hashlib.md5()  # 开启加密
ret.update(s1.encode('utf-8'))  # 确定加密的内容
print(ret.hexdigest())  # 得出结果


def Md5(pwd):
    ret = hashlib.md5()
    ret.update(pwd.encode('utf-8'))
    return ret.hexdigest()


def register():
    username = input(">>>请输入用户名：").strip()
    password = input(">>>请输入密码：").strip()
    password_md5 = Md5(password)
    with open('register', mode='a', encoding='utf-8') as f1:
        f1.write(f'\n{username}|{password_md5}')


register()


# 加盐： 让加密的过程更加复杂


s1 = '123456'
ret = hashlib.md5("ralph".encode('utf-8'))  # 加盐操作
ret.update(s1.encode('utf-8'))
print(ret.hexdigest())


"""
sha 系列

随着sha系列的数字越高，加密越复杂，但是耗时长
"""


s1 = '123456'
ret = hashlib.sha512("ralph".encode('utf-8'))  # 加盐操作
ret.update(s1.encode('utf-8'))
print(ret.hexdigest())


"""
文件的校验
1：python 一切是对象  linux 一切是文件
"""

s1 = '123456安达市多撒大所多阿斯顿撒大所多'
ret = hashlib.sha512()
ret.update(s1.encode('utf-8'))
print(ret.hexdigest())


# 文件校验(low)


def File_md5(path):
    ret = hashlib.sha256()
    with open(path, mode='rb') as f1:
        b1 = f1.read()
        # print(b1)
        ret.update(b1)
    return ret.hexdigest()


result = File_md5('register')
print(result)  # f18ac36401b849f7b99177d26a6fc1d9854d1539051992789aebf40ebbb9c68f
