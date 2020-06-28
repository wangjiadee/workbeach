"""
1.下标 索引 从0开始
2.对字符串进行任何的操作
3.步长 可以理解为间隔
"""

ss1 = 'xiejier宝宝520'

# 切片
ss2 = ss1[0]

#切片反取
ss3 = ss1[-1]
print(ss3)


# 指定切片部分内容
ss4 = ss1[0:3]
print(ss4)


# 指定步长来取值
ss5 = ss1[:7:2]
print(ss5)

# 反向指定步长
ss6 = ss1[::-2]
print(ss6)



"""
str commone methods
任何方法不会对原字符串进行操作 都是产生新的字符串
"""

#1. upper lower  大小写 遇到中文忽略
s = 'ralph'
s1 = s.upper()
print(s1,type(s1))

# application-验证码：
username = input("please input fucking name:")
password = input("please input fucking password:")
code = "X7j1"
u_code =input('please input fucking code:')

if u_code.upper() == code.upper():
    if username == 'mdzz' and password == 'sb':
        print("success loading!")
    else:
        print("Error!")
else:
    print("Error!!")


#2. startswith  判断以什么开头

print(s.startswith('r'))
print(s.startswith('ra'))

# 3.replace 替换

s2 = s.replace('ralph','xiejier')
print(s2)

s3 = 'xiejier love ralph，ralph love xiejier too'
s4 = s3.replace('ralph','xiejier',2)
print(s4)


#  4. strip 取消空格 \t \n
a = '  xie唉jier  '
print(a)
a1 = a.strip()
print(a1)

#  了解：指定去除字符
a2 = a.strip('ie')
print(a2)


# 5. split 切割   too important！！！！
#  split ---- return list

b = '123|qwe|asd|zxc'
b1 = b.split("|")
print(b1)

b2 = b.split("|",1)
print(b2)


#6. join
c = 'oppofindx2pro'
c1 = '+'.join(c)
print(c1,type(c1))


l1 = ['reno','a92','oneplus']
# list element must be str
c2 = '+'.join(l1)
print(c2)

# 7. count
d = 'jkfashfisdafjkdsalfhuwiaefjksavbgfiydasfgsdauifhewjfgsady'
print(d.count('f'))

# format 格式化输出
msg = '{}宝宝'.format('xiejier')
print(msg)


msg1 = '{name}宝宝'.format(name='xiejier')
print(msg1)


# is系列
v = 'preversion123'
print(v.isalnum()) # 字符是否有字母和数字组成
print(v.isalpha()) # 只能有字母
print(v.isdecimal()) #只能由于10进制的数字组成