'''
@Author: Ralph
@Type_file: Python
@Date: 2020-08-03 19:30:37
@LastEditTime: 2020-08-03 19:30:53
@FilePath: \workbeach\Object\Object_chouxianglei.py
@Effect: python的抽象类 父类对子类的约束
'''
# 抽象类（规范类）
# 作用：启动规范和约束的作用，并没有实际的作用，作为父类


# 实现抽象类的另一种方式   依赖abc模块
from abc import ABCMeta, abstractmethod
# 报错内容: Can't instantiate abstract class Applpay with abstract methods pay


class Payment(metaclass=ABCMeta):
    @abstractmethod
    # pay的参数需要填写和其他对应的传入参数
    def pay(self, money):
        # 指定报错信息
        raise NotImplementedError('请在在子类中重写同名pay的方法')


class Alipay(Payment):
    def __init__(self, name):
        self.name = name

    def pay(self, money):
        dic = {'username': self.name, 'price': money}
        print('%s通过支付宝成功支付%s元' % (self.name, money))


class Wechat(Payment):
    def __init__(self, name):
        self.name = name

    def pay(self, money):
        dic = {'name': self.name, 'price': money}
        print('%s通过微信成功支付%s元' % (self.name, money))


class Applpay(Payment):
    def __init__(self, name):
        self.name = name

    def pay(self, money):
        # def zhifu(self, money):
        dic = {'name': self.name, 'price': money}
        print('%s通过苹果成功支付%s元' % (self.name, money))
# wechat_user = Wechat('tom')
# wechat_user.pay(500)
# Alipay_user = Alipay('wek')
# Alipay_user.pay(100)

# 归一化思想设计


def pay(name, price, kind):
    if kind == 'Wechat':
        obj = Wechat(name)
    elif kind == 'Alipay':
        obj = Alipay(name)
    elif kind == 'Applpay':
        obj = Applpay(name)
    obj.pay(price)


pay('tony', 500, 'Wechat')
pay('ralph', 4500, 'Alipay')
pay('ralph', 4500, 'Applpay')
