'''
@Author: Ralph
@Type_file: Python
@Date: 2020-07-30 19:45:19
@LastEditTime: 2020-08-03 20:24:10
@FilePath: \workbeach\fundation\简易计算器.py
@Effect: DO
'''
# 多位数相加计算器
import re
cal = input("please input fucking num ,must have '+' between each number:")
s1 = cal.split("+")
sum = 0
for i in s1:
    sum += int(i.strip())
print(sum)

###############################################


def calculator(s):
    def two_num_cal(s):  # 给定str格式的两个数字（可能是整数或小数）组成的四则运算表达式（可能包含多余的+或-，如'3.5346*-23.2354'、'-3.5346-23.2354'），返回float型的计算结果
        if re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(2) == '*':
            return float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(1))*float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(3))
        elif re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(2) == '/':
            return float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(1))/float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(3))
        elif re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(2) == '+':
            return float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(1))+float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(3))
        elif re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(2) == '-':
            return float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(1))-float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(3))
    while not re.search(r'^[-+]?\d+(\.\d+)?$', s):  # 当s不能转化为float型时，执行此while循环
        while re.search('[+-]{2,}', s):
            s = s.replace('++', '+').replace('--', '+').replace('+-',
                                                                '-').replace('-+', '-')  # 循环替换表达式中多余的+-号
        if re.search(r'[(][^()]+[)]', s):
            s = s[:re.search(r'[(][^()]+[)]', s).span()[0]] + str(calculator(re.search(r'[(][^()]+[)]', s).group()[1:len(
                re.search(r'[(][^()]+[)]', s).group())-1])) + s[re.search(r'[(][^()]+[)]', s).span()[1]:]  # 匹配首个最内层小括号，递归计算其值，将结果替换至原字符串
        if re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?', s):
            s = s[:re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?', s).span()[0]] + str(two_num_cal(re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?',
                                                                                                           s).group())) + s[re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?', s).span()[1]:]  # 匹配首个乘法或除法，将结果替换至原字符串
        if re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?', s) == None and re.search(r'[+-]?(\d+(\.\d+)?[+-]\d+(\.\d+)?)', s):
            s = s[:re.search(r'[+-]?(\d+(\.\d+)?[+-]\d+(\.\d+)?)', s).span()[0]] + str(two_num_cal(re.search(r'[+-]?(\d+(\.\d+)?[+-]\d+(\.\d+)?)',
                                                                                                             s).group())) + s[re.search(r'[+-]?(\d+(\.\d+)?[+-]\d+(\.\d+)?)', s).span()[1]:]  # 匹配首个加法或减法，将结果替换至原字符串
    return float(s)


#######################################
def calculator1(s):
    def two_num_cal(s):  # 给定str格式的两个数字（可能是整数或小数）组成的四则运算表达式（可能包含多余的+或-，如'3.5346*-23.2354'、'-3.5346-23.2354'），返回float型的计算结果
        ret = re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s)
        if ret.group(2) == '*':
            return float(ret.group(1))*float(ret.group(3))
        elif ret.group(2) == '/':
            return float(ret.group(1))/float(ret.group(3))
        elif ret.group(2) == '+':
            return float(ret.group(1))+float(ret.group(3))
        elif ret.group(2) == '-':
            return float(ret.group(1))-float(ret.group(3))
    while not re.search(r'^[+-]?\d+(\.\d+)?$', s):  # 当s不能转化为float型时，执行此while循环
        while re.search('[+-]{2,}', s):
            s = s.replace('++', '+').replace('--', '+').replace('+-',
                                                                '-').replace('-+', '-')  # 循环替换表达式中多余的+-号
        ret1 = re.search(r'[(][^()]+[)]', s)  # 匹配首个最内层小括号，递归计算其值，将结果替换至原字符串
        if ret1:
            s = s[:ret1.span()[0]] + str(calculator(ret1.group()
                                                    [1:len(ret1.group())-1])) + s[ret1.span()[1]:]
        # 匹配首个乘法或除法，将结果替换至原字符串
        ret2 = re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?', s)
        if ret2:
            s = s[:ret2.span()[0]] + str(two_num_cal(ret2.group())) + \
                s[ret2.span()[1]:]
        # 匹配首个加法或减法，将结果替换至原字符串
        ret3 = re.search(r'[+-]?(\d+(\.\d+)?[+-]\d+(\.\d+)?)', s)
        if ret2 == None and ret3:
            s = s[:ret3.span()[0]] + str(two_num_cal(ret3.group())) + \
                s[ret3.span()[1]:]
    return float(s)
