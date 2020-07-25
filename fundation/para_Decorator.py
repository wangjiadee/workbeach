'''
@Author: Ralph
@Type_file: Python
@Date: 2020-07-25 13:14:19
@LastEditTime: 2020-07-25 13:21:53
@FilePath: \workbeach\fundation\para_Decorator.py
@Effect: 带参数的装饰器
'''


"""

开放封闭原则
我们提前写好一个功能,让别人使用的时候能够直接使用就能完成相应的功能

"""




import time
def logger(path):
    def log(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            with open(path, mode='a', encoding='utf-8') as f:
                msg = '%s 执行了%s' % (time.strftime(
                    '%Y-%m-%d %H:%M:%S'), func.__name__)
                f.write(msg)
            return ret
        return inner
    return log


@logger('auth.log')
def login():
    print('登录的逻辑')


@logger('auth.log')
def register():
    print('注册的逻辑')


@logger('auth.log')     # ret = log('auth.log')   show_goods = ret(show_goods)
def show_goods():
    print('查看所有商品信息')


@logger('buy.log')
def add_goods():
    print('商品加入购物车')


login()
add_goods()
show_goods()
