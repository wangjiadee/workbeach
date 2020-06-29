z = ' xiE Jier '

# 移除空格
z1 = z.strip()
print(z1)


# 判断是不是由 xi开头,是不是 ier 结尾
z2 = z.startswith(' xi')
print(z2)
z3 = z.endswith('ier ')
print(z3)

# 将J 换成X
z4 = z.replace('J','X')
print(z4)

# 把第1个i换成j
z5 = z.replace('i','j',1)
print(z5)

# 通过i 做分割
z6 = z.split('i',1)
print(z6)

# 全部大写和小写
z7 = z.upper()
print(z7)
z8 = z.lower()
print(z8)

# 统计i出现的次数
z9 = z.count("i")
print(z9)


# 输出z 的 前2个字符、第3个字符、后2个字符
a1 = z[:2]
a2 = z[3]
a3 = z[-2:]
print(a1)
print(a2)
print(a3)



s = "890x7c6s"
#切片出890
print(s[0:3])
# 组成x7c
print(s[3:6])
# 组成8076
print(s[::2])
# 组成9xc
print(s[1:-2:2])
# 截取c
print(s[-3])
# 截取cx9
print(s[-3::-2])


# 使用while和for循环分别打印字符串s="asdfer"中每个元素
# for:

for i in s:
    print(i)
# while

i = 0
o = len(s)
while True:
    if i < o:
        print(s[i])
        i += 1
    else:
        break

# 使用for循环对s行循环，但是每次打印的内容都是s
for i in s:
    print(s)
# for 循环单个字母，但是每一次后面都有“xj”
for i in s:
    print(i + "xj")


e = "4321"
for i in e:
    print("fucking time"+i+"s")

for i in e:
    print("fucking time %ss"%(i))
print("go go go!")


