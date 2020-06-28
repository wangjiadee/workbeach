#次方：
a = 3
b = 4
print(a ** b)

# 取商
print(10 // 3)

# 求余
print(10 % 2)

#不等于
print( 3 != 5)



# 逻辑运算符
"""
and   or   not

x and y :  x为真，值是y,x为假，值是x
x or y :   x为真，值就是x，x为假，值是y


1.在没有（）的情况下 ， 优先级：not > and > or
2.同一优先级从左到右依次计算
"""

print(1 < 3 and 3 < 4 or 1>2)

#成员运算符

# in 和 not in
print('123' in '123333333333')
print('abc' not in '123333333333')


# 数字和字符串之间的转换
i1 = 100
print(str(i1)),type(str(i1))


# 数字和布尔值之间的转化：
# 非0即True 0 就是false
sb = 100
print(bool(sb))
#负数 小数 浮点类型的都是T
sd =  -1
print(bool(sd))

mdzz = 0
print(bool(mdzz))

print(1 > 2 and 3 or 4 and 4 < 5)
print(8 or 3 and 4 or 2 and 0 or 9 and 7)
print( 2 > 2 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

