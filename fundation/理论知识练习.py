# 1.有如下
v1 = {'郭宝元','李杰','太白','梦鸽'}
v2 = {'李杰','景女神'}
# 请得到 v1 和 v2 的交集并输出
print(v1 & v2)
# 请得到 v1 和 v2 的并集并输出
print(v1 | v2)
# 请得到 v1 和 v2 的 差集并输出
print(v1 - v2)
# 请得到 v2 和 v1 的 差集并输出
print(v2 - v1)


# 2.循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）
li = []
while 1:
    user_input = input("Pelase input fucking notes:")
    li.append(user_input)
    print(li)
    if user_input.upper() == "N":
        break
        print(li)

# 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
v1  = {"拍照","爬山","小白船","机会"}
v2 = []
while 1:
    user_input = input("Pelase input fucking notes:")
    if user_input.upper() == "N":
        break
        print(v1,v2)
    for i in v1:
        if user_input == i:
            v2.append(user_input)
    v1.add(user_input)
    print(v1,v2)

"""
可变类型：dict、list、set
不可变类型：int、long、float、complex、string、bool、tupl
其中可变类型不能作为字典的key，因为它们没有__hash__()方法

id的使用方式 : id(变量)
id的作用：查看变量的内存地址

type 的使用方式 ：type(变量名)
type 的作用：  查看变量的数据类型


代码块 缓存机制 和 小数据池:
-----代码块-------
python 都由代码块组成

-----缓存机制-----
在同一代码快中,遇到初始化变量时候  先去一个类似字典的存储空间里面查找 如果有就直接用 没有在存储
满足缓存机制则他们在内存中只存在一个，即：id相同。
int float str bool 符合
-----小数据池-----
在不同的代码块里面.python 默认将-5~256整数共用一个数据缓存


-----深浅拷贝----
对于浅copy来说，只是在内存中重新创建了开辟了一个空间存放一个新列表，但是新列表中的元素与原列表中的元素是公用的。(不copy 原来的内存地址)
对于深copy来说，列表是在内存中重新创建的，列表中可变的数据类型是重新创建的，列表中的不可变的数据类型是公用的。(可变数据类型内存重组 )




"""

# is  是判断2边的内存地址是否相同
# ==  是判断2边的值是否相同
result1 = v1 == v2
result2 = v1 is v2


# 可变数据类型: dict list set
# 变量所指向的内存地址可变
v1 = {'k1':'v1','k2':[1,2,3]}
v2 = v1
v1['k1'] = 'wupeiqi'
print(v2)


# 按顺序执行
v1 = '人生苦短，我用Python'
v2 = [1,2,3,4,v1]
v1 = "人生苦短，用毛线Python"
print(v2)

# list 是可变数据类型 因此 userinfo指向info的内存地址 随着userinfo的改变而改变
info = [1,2,3]
userinfo = {'account':info, 'num':info, 'money':info}
info.append(9)
print(userinfo)
# 不可变数据类型 :str
info = "题怎么这么多"
print(userinfo)

# list 可变类型  info[0] 改变 其他的跟着改变
info = [1,2,3]
userinfo = [info,info,info,info,info]
info[0] = '不仅多，还特么难呢'
print(info,userinfo)

# list 可变类型 即使是 外部定义的list 修改list 依旧会改变
info = [1,2,3]
print(id(info))
userinfo = [info,info,info,info,info]
print(id(userinfo))
userinfo[2][0] = '闭嘴'
print(info,userinfo)


info = [1,2,3]
user_list = []
for item in range(10):
    user_list.append(info)
info[1] = "是谁说Python好学的？"
print(user_list)

# for 循环完成后 data['user'] = 9   得到 字典 data = {‘user’:9}
data = {}
for i in range(10):
    data['user'] = i
print(data)

#  输出的是9个09
#[{'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}]
data_list = []
data = {}
for i in range(10):
    data['user'] = i
    data_list.append(data)
print(data_list)


# duang 7游戏
user_input = int(input("Pelase input number:"))
lst = []
for i in range(user_input+1):
    if  i != 0 and i % 7 == 0:
        # print("duang")
        lst.append("duang")
    else:
        # print(i)
        lst.append(i)
lst.pop(0)
print(lst)