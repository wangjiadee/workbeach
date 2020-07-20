# 内置函数 匿名函数

"""
匿名函数: 没有名字的函数、也叫一句话函数
函数名 = lambda 参数：返回值

lambda相当于函数的def.

"""
def func(x,y):
    return x+y
print(func(10,20))

func = lambda a,b: a+b
print(func(3, 4))  # 7



"""

内置函数：
1.map 映射函数
map(function,iterable) 可以对可迭代对象中的每一个元素进映射,分别取执行function
"""

lst = [1,2,3,4,5]
def func(s):
    return  s*s
mp = map(func,lst)
print(mp)   #<map object at 0x050FC118>
print(list(mp))  #使用list 来拿出来


# 用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
l1=[{'name':'alex'},{'name':'y'}]
print(list(map(lambda a :{"name":a["name"]+"_sb"},l1)))


# map(str,[1,2,3,4,5,6,7,8,9])输出是什么? (面试题)
print(map(str,[1,2,3,4,5,6,7,8,9]))  #<map object at 0x0433D1A8>


"""
2.filter 筛选过滤
filter(function,iterable)
function: 用来筛选的函数,在filter中会自动的把iterable中的元素传递给function,
然后根据function返回的True或者False来判断是否保留此项数据
filter 本身输出的是内存空间地址
添加list可以变成想要的内容
"""

# 用filter来处理,得到股票价格大于20的股票名字
shares = {'IBM': 36.6, 'Lenovo': 23.2, 'oldboy': 11.2, 'ocean': 10.2}
print(list(filter(lambda i:shares[i]>20,shares)))


# 有下面字典，得到购买每只股票的总价格，并放在一个迭代器中。
portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}]

print(list(map(lambda x:x['shares']*x['price'] ,portfolio)))

# 用filter过滤出单价大于100的股票。
print(list(filter(lambda a:a['shares'] > 100,portfolio)))


# 有下列三种数据类型，
l1 = [1,2,3,4,5,6]
l2 = ['oldboy','alex','wusir','太白','日天']
tu = ('**','***','****','*******')
# 写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）
"""
zip 
函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,
然后返回由这些元祖组成的内容,如果各个迭代器的元素个数不一致,则按照长度最短的返回
"""

print(list(zip(l1,l2,tu)))
print(list(filter(lambda el:el[0] >2 and len(el[2]) >= 4,zip(l1,l2,tu))))

#将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
l1 = [ {'sales_volumn': 0},
      {'sales_volumn': 108},
      {'sales_volumn': 337},
      {'sales_volumn': 475},
      {'sales_volumn': 396},
      {'sales_volumn': 172},
      {'sales_volumn': 9},
      {'sales_volumn': 58}, 
      {'sales_volumn': 272}, 
      {'sales_volumn': 456}, 
      {'sales_volumn': 440},
      {'sales_volumn': 239}]
print(sorted(l1, key=lambda d : d['sales_volumn']))  #升序
print(sorted(l1, key=lambda d : d['sales_volumn'], reverse=True))  #降序 


# 通过过滤掉年龄大于16岁的字典
lst = [{'id':1,'name':'alex','age':18},
        {'id':1,'name':'wusir','age':17},
        {'id':1,'name':'taibai','age':16},]

print(list(filter(lambda a:a['age'] <= 16,lst)))



#有如下列表,按照元素的长度进行升序
lst = ['天龙八部','西游记','红楼梦','三国演义']
print(sorted(lst,key = lambda a: len(a)))



#有如下数据,按照元素的年龄进行升序
lst = [{'id':1,'name':'alex','age':18},
    {'id':2,'name':'wusir','age':17},
    {'id':3,'name':'taibai','age':16},]

print(sorted(lst, key= lambda a:a['age']))

# 看代码叙说,两种方式的区别

"""
reversed
将一个序列翻转, 返回翻转序列的迭代器 reversed 
"""

lst = [1,2,3,5,9,12,4]
lst.reverse()  #将代码元素先翻转,然后打印翻转
print(lst)   #[4, 12, 9, 5, 3, 2, 1]
print(list(reversed(lst)))  # 变成翻转的新列表x

#分析代码
# 列表推导式
v = [lambda :x for x in range(10)]
print(v)
#0到9的内存地址
print(v[0])
#0的地址
print(v[0]())
#9


# 生成器 ---不运行的---就是一个内存地址
v = (lambda :x for x in range(10))
print(v)                #<generator object <genexpr> at 0x04FC6728> 
print(v[0])             #报错   因为生成器只有在next list for循环当中运行
print(v[0]())  
print(next(v))          #<function <genexpr>.<lambda> at 0x04C7B4F0>
print(next(v)())        # 如果单独的执行print(next(v)()) 输出为0  如果是执行 (next(v)) 和(next(v)()) 为1






"""
闭包：
1.什么是闭包？
    闭包是嵌套在函数中的函数
    闭包必修是内层函数对外层函数的变量（非全局变量）的引用

2.判断闭包方法
    
# 函数名.__code__.co_freevars 查看函数的自由变量
print(avg.__code__.co_freevars) 
"""

#**********
def num():
    return [lambda x:i*x for i in range(4)]
print([m(2)for m in num()])


#输出[6666]
# 详细解释
# https://blog.csdn.net/ppppppushcar/article/details/107463354


                                                            