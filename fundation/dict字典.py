# 1.请将列表中的每个元素通过 "_" 链接起来。
users = ['fx','xj',666,'渣渣辉']
users[2] = "666"
s= "_".join(users)
print(s)

# method2
users = ['fx','xj',666,'渣渣辉']
ls = []
for  i  in  users:
    ls.append(str(i))
res = "_".join(ls)
print(res)


# 2.请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。

v1 = (11,22,33)
v2 = [44,55,66]
v2.extend(v1)
print(v2)


# 3.请将元组 v1 = (11,22,33,44,55,66,77,88,99)中的所有偶数索引位置的元素追加到新列表中。
# 元祖不能扩展
v1 = (11,22,33,44,55,66,77,88,99)
ls = v1[1::2]
ls1 = []
ls1.extend(ls)
print(ls1)



# 4.将字典的键和值分别追加到key_list 和 value_list 两个列表中，如：
key_list = []
value_list = []
info = {'k1':'v1','k2':'v2','k3':'v3'}
for i in info:
    key_list.append(i)
    value_list.append(info.get(i))
print(key_list)
print(value_list)

# method
key_list = []
value_list = []
info = {'k1':'v1','k2':'v2','k3':'v3'}
key_list.extend(info.keys())
value_list.extend(info.values())
print(key_list,value_list)


# 5.字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# a. 请循环输出所有的key
for i in dic:
    print(i)
# b. 请循环输出所有的value
for i in dic:
    print(dic.get(i))
# c. 请循环输出所有的key和value
for i in dic:
    print(dic.keys())
    print(dic.values())
# d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic['k4']="v4"
print(dic)
# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic['k1']="alex"
print(dic)
# f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
dic["k3"]="[11,22,33,44]"
print(dic)
# method2
dic['k3'].append("44")
print(dic)
# g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic['k3'].insert(0,18)
print(dic)


# 6.有如下字典,实现以下需求的内容
av_catalog = {
"欧美": {
"www.宝元.com": ["很多免费的,世界最大的", "质量一般"],
"www.alex.com": ["很多免费的,也很大", "质量挺好"],
"oldboy.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
"hao222.com": ["质量很高,真的很高", "全部收费,屌丝请绕过"]
},
"日韩": {
"tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]
},
"大陆": {
"1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
}
}

# 1)给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个 元素：'奶很多'。
av_catalog['欧美']['www.宝元.com'].insert(2,"奶很多")
print(av_catalog)

# 2)将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
del av_catalog['欧美']['hao222.com'][-1]
print(av_catalog)

# 3)将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
av_catalog['日韩']['tokyo-hot'][1] = av_catalog['日韩']['tokyo-hot'][1].upper()
print(av_catalog)

# 4)给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
av_catalog['大陆']["1028"]='一天就封了'
print(av_catalog)

# 5)删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]
del av_catalog['欧美']['oldboy.com']
print(av_catalog)

# 6)给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
av_catalog['大陆']['1024'].insert(0,'可以爬下来')
print(av_catalog)

# 7.请循环打印k2对应的值中的每个元素。
info = {
    'k1': 'v1',
    'k2': [('alex'), ('wupeiqi'), ('oldboy')],
}
# method1:
for i in range(0,3):
    print(info['k2'][i])
# method2:
for i in info.get('k2'):
    print(i)

# 8.有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}

info = {}
s1 = "k: 1|k1:2|k2:3 |k3 :4"
l1 = s1.split("|")
# print(l1)
for i in l1:
    x, y = i.split(":")  # 抓分元组
    info[x] = int(y)
print(info)


# 9.有如下值 li= [11,22,33,44,55,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
result = {'key1':[],'key2':[]}
li= [11,22,33,44,55,77,88,99,90]
for i in li:
    if  i > 66:
        result["key1"].append(i)
    elif i < 66:
        result["key2"].append(i)
print(result)


# 10.输出商品列表，用户输入序号，显示用户选中的商品
#
# 商品列表：
print("二手车拍卖市场！！！")
goods = [
{"name": "BYD", "price": '16W'},
{"name": "bens", "price": '80W'},
{"name": "Q3", "price": '40W'},
{"name": "特斯拉", "price": '25W'}
]
# 要求:
# 1：页面显示 序号 + 商品名称 + 商品价格，如：
for i in range(0,len(goods)):
    print(i,goods[i]['name'],goods[i]['price'])

# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
user_input = input("Pelase input fucking number: Quit(Q or q)").strip()
li = goods[int(user_input) - 1]
print(user_input,li["name"],li["price"])

# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
if user_input.isdecimal():
    user_input = int(user_input)
    if 0 < int(user_input) <= len(goods):
        pass
    else:
        print("what the fucking number? again!")
else:
    print("number? ok? mdzz!")

# 4：用户输入Q或者q，退出程序。
if user_input.upper() == 'Q':
    print("Bye!")
    break

# all_code:
print("二手车拍卖市场！！！")
goods = [
{"name": "BYD", "price": '16W'},
{"name": "bens", "price": '80W'},
{"name": "Q3", "price": '40W'},
{"name": "特斯拉", "price": '25W'}
]
for i in range(0,len(goods)):
    print(i+1,goods[i]['name'],goods[i]['price'])
while True:
    user_input = input("Pelase input fucking number: Quit(Q or q)").strip()
    if user_input.upper() == 'Q':
        print("Bye!")
        break
    if user_input.isdecimal():
        user_input = int(user_input)
        if 0 < int(user_input) <= len(goods):
            li = goods[int(user_input) - 1]
            print(user_input,li["name"],li["price"])
        else:
            print("what the fucking number? again!")
    else:
        print("number? ok? mdzz!")




# 覆盖式循环  最后结果是users 9
v = {}
for index in range(10):
    v['users'] = index
print(v)