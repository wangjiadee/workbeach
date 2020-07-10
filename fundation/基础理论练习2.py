v1 = [1,2,3,4,5]
v2 = [v1,v1,v1]
v1.append(6)
print(v1)
print(v2)



# [222, 2, 3, 4, 5]
# [[222, 2, 3, 4, 5], [222, 2, 3, 4, 5], [222, 2, 3, 4, 5]]
v1 = [1,2,3,4,5]
v2 = [v1,v1,v1]
v2[1][0] = 111
v2[2][0] = 222
print(v1)
print(v2)


# {'k1': [6, 7, 8, 9]}
v1 = [1,2,3,4,5,6,7,8,9]
v2 = {}
for item in v1:
    if item < 6:
        continue
    if 'k1' in v2:
        v2['k1'].append(item)
    else:
        v2['k1'] = [item ]    #v2 ={'k1':[6]}
print(v2)


# 深浅拷贝案例
# 字符串使用的是同一个缓存机制
import copy
v1 = "alex"
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(v1 is v2)
print(v1 is v3)

import copy
v1 = {"2":"4"}
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(v1 is v2)  #false
print(v1 is v3)  #false

import copy
v1 = [1,2,3,4,5]
v2 = copy.copy(v1) #外壳是新的  里面的元素是沿用原来的
v3 = copy.deepcopy(v1) #外壳是新的 里面的不可变得元素沿用原来得 可以变得重新组成
print(v1 is v2)  #false
print(v1 is v3)


import copy
v1 = [1,2,3,4,5]
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(v1[0] is v2[0])
print(v1[0] is v3[0])
print(v2[0] is v3[0])


import copy
v1 = [1,2,3,4,[11,22]]
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(v1[-1] is v2[-1])  #浅拷贝 外壳拷贝 里面的所有元素内存地址相同
print(v1[-1] is v3[-1])
print(v2[-1] is v3[-1])



import copy
v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
v2 = copy.copy(v1)
print(v1 is v2)  #外壳是新的所以 就是新的
print(v1[0] is v2[0])
print(v1[3] is v2[3])
print(v1[3]['name'] is v2[3]['name'])
print(v1[3]['numbers'] is v2[3]['numbers'])
print(v1[3]['numbers'][1] is v2[3]['numbers'][1])


# 可变数据类型重组
import copy
v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
v2 = copy.deepcopy(v1)
print(v1 is v2)
print(v1[0] is v2[0])
print(v1[3] is v2[3])
print(v1[3]['name'] is v2[3]['name'])
print(v1[3]['numbers'] is v2[3]['numbers'])
print(v1[3]['numbers'][1] is v2[3]['numbers'][1])


# 11.请说出下面a,b,c三个变量的数据类型。
a = ('mdzz')
b = (1,)
c = ({'name': 'barry'})   #()里面是什么就是什么类型 如果是纯数字就是元祖
print(type(a),type(b),type(c))


l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
# 从大到小排序
l1.sort(reverse = True)
print(l1)
# 从小到大排序
l1.sort()
print(l1)
# 反转l1列表
l1.reverse()
print(l1)


# 13.利用python代码构建一个这样的列表(升级题)：
# [['_','_','_'],['_','_','_'],['_','_','_']]
l1 = []
for i in range(3):
    l1.append(['_']*3)
print(l1)
print([["_"*3]*3])

l1 = [1,2,3,4,5]
l1 += [3,4]
print(l1)


# fromkeys: 快速组成dict的key 和values
dic = dict.fromkeys('zxy',[])
print(dic)
dic['y'].append(666)
dic['z'].append(111)
print(dic)

# fromkeys方法并不适用来创建多个对象，因为我如果改变了某一个对象中的某个属性，那么其余对象都会被改变
dic = {'k1':[],'k2':[],'k3':[]}
dic['k1'].append(123)
dic['k2'].append(321)
print(dic)


# 请把索引为奇数对应的元素删除（不能一个一个删除）
l1 = [11, 22, 33, 44, 55]
l2 = []

for i in range(len(l1)):
    if i % 2 ==0 :
        l2.append(l1[i])
l1 = l2
print(l1)

# dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18} 请将字典中所有键带k元素的键值对删除.
dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18}
li = []
for i in dic:
    if 'k' in i:
        li.append(i)
for b in li:
    dic.pop(b)
print(dic)


"""
bytes数据类型是python的基础数据类型，bytes类型存在的意义是什么？
bytes主要用与网络传输数据和在硬盘里保存数据。可以节省空间。是python数据类型中唯一采用非unicode编码的数据类型。

列举bytes类型与str类型的三个不同点？
编码方式不同；
组成单位不同：字符，字节；
中文的表现形式不同。
"""

# 18.完成下列需求：
s1 = '尼玛炸了'
# 将s1转换成utf-8的bytes类型。
b1 = s1.encode('utf-8')
print(b1)
# 将s1转化成gbk的bytes类型。
b2 = s1.encode('gbk')
print(b2)
# b为utf-8的bytes类型，请转换成gbk的bytes类型。
b = b'\xe5\xb0\xbc\xe7\x8e\x9b\xe7\x82\xb8\xe4\xba\x86'
s2 = b.decode('utf-8')
s3 = s2.encode('gbk')
print(s2,s3)


# 用户输入一个数字，判断一个数是否是水仙花数。
# 水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数. 那这个数就是一个水仙花数,
# 例如: 153 = 1**3 + 5**3 + 3**3
while 1:
    user_input = input(">>> num is:")
    if user_input.isdecimal():
        if len(user_input) == 3:
            user_input = int(user_input)
            if user_input == ((user_input // 100) ** 3 +((user_input % 100) // 10 ) ** 3 + (user_input % 10) ** 3):
                print('{}是水仙花数'.format(user_input))
            else:
                print('您输入的不是水仙花数，请重新输入')
        else:
            print('您输入的不是三位数字，请重新输入')
    else:
        print('输入内容包含非数字元素，请重新输入')

# 把列表中所有姓周的⼈的信息删掉(此题有坑, 请慎重):
# lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
# 结果: lst = ['麻花藤']
l1 = []
lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
for i in lst:
    if '周' not in i:
        l1.append(i)
lst = l1
print(lst)


# 21.车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (选做题)
cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪B25041']
locals = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '京':'北京', '湘':'湖南'}
# 结果: {'⿊⻰江':2, '⼭东': 2, '上海': 1}
dic = {}
dic1 = {}
for i in cars:
    s = i[0]
    if s in locals.keys():
        dic[i] = locals[i[0]]
        # print(dic) {'车牌': '省份名'}
for j in list(dic.values()): #所有省份作为一个列表，统计每个省的个数。
    dic1[j] = list(dic.values()).count(j) #省份全称作为键，统计的个数作为值。
print(dic1)#{'⼭东': 2, '北京': 1, '⿊⻰江': 2, '上海': 1}