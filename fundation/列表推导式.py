# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
print([i.upper() for i in ["mdzz","nimazhale","dsb","cnm","diao"] if len(i) > 3])

# 求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
print([(x,y) for x in range(6) if x%2 == 0 for y in range(6) if y %2 ==1])

# 将列表M = [[1,2,3],[4,5,6],[7,8,9]] 的 369 提取出来
print([i[2] for i in [[1,2,3],[4,5,6],[7,8,9]] ])

# 求出50以内能被3整除的数的平方，并放入到一个列表中。
print([ i**3 for i in range(0,50,3) ])

# 构建一个列表：['fucking1times', 'fucking2times', 'fucking3times', 'fucking4times', 'fucking6times', 'fucking7times', 'fucking8times', 'fucking9times', 'fucking10times']
print([f"fucking{i}times" for i in range(1,11) if i !=5])

# 构建一个列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
print([(x,x+1) for x in range(6)])

# 构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print([i for i in range(0,20,2)])

# 有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']
l1 = ['alex', 'WuSir', '老男孩', '太白']
print([l1[i] + str(i) for i in range(len(l1))])


# 构建一个列表,列表里面的元素是扑克牌除去大小王以后，所有的牌类（列表里面的元素为元组类型）。
# l1 = [('A','spades'),('A','diamonds'), ('A','clubs'), ('A','hearts')......('K','spades'),('K','diamonds'), ('K','clubs'), ('K','hearts') ]
print([(x,y) for x in [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] for y in ['SPADES','DIAMONDS','CLUBS','HEARTS']])


# 有以下数据类型：
# 数据通过列表推导式转换成下面的类型：[[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
x = {
'name':'alex',
'Values':[{'timestamp':1517991992.94,
'values':100,},
{'timestamp': 1517992000.94,
'values': 200,},
{'timestamp': 1517992014.94,
'values': 300,},
{'timestamp': 1517992744.94,
'values': 350},
{'timestamp': 1517992800.94,
'values': 280}
],}
print([list((v['timestamp'],v['values'])) for v in x['Values']])



# 构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色（列表里面的元素为元组类型）。
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
print([(x,y) for x in colors for y in sizes])


# 简述一下yield 与yield from的区别。
"""
yield 主要用来生成一个生成器
yield from 用来取元素的值 返回另外一个生成器

"""

#分析代码
print([i % 2 for i in range(10)])
# [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
v = (i % 2 for i in range(10))
print(v)  #<generator object <genexpr> at 0x0581D7D0>
#打印出来的是生成器地址


for i in range(5):
     print(i)
print(i)