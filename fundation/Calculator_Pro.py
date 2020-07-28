'''
@Author: Ralph
@Type_file: Python
@Date: 2020-07-28 10:23:46
@LastEditTime: 2020-07-28 14:32:18
@FilePath: \workbeach\fundation\Calculator_Pro.py
@Effect: DO
'''
import re
exp = (1+3*4*5/6)-4
# 计算两个数的乘法或者除法


def mul_div(exp):
    # '3*-4','5/-6'
    if '*' in exp:
        a, b = exp.split('*')
        return float(a)*float(b)
    if '/' in exp:
        a, b = exp.split('/')
        return float(a) / float(b)


# 计算表达式中的所有的乘除法


def remove_muldiv(exp):
    while True:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', exp)
        if ret:
            son_exp = ret.group()   # 3*4  12*5
            res = mul_div(son_exp)
            print(res)  # 12  60
            exp = exp.replace(son_exp, str(res))
            print('-->', exp)  # exp = 1+12.0*5/6
        else:
            break
    return exp


ret = remove_muldiv('1+3*4*5/6-4-7')
print(ret)
