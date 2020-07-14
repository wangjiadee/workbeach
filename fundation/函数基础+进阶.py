# Analysis code
# 内部变量如果没有 就回去外层寻找
# 不会报错
a = 2
def wrapper():
    print(a)
wrapper()


# 局部变量的引用没有定义,内部变量不会影响外部变量
# 会报错
a = 2
def wrapper():
    a += 1
    print(a)
wrapper()


# 内部变量如果没有 就回去外层寻找
def wrapper():
    a = 1
    def inner():
        print(a)
    inner()
wrapper()


# 报错 因为没有声明nonlocal
def wrapper():
    a = 1
    def inner():
        a += 1
        print(a)
    inner()
wrapper()


#比较2个列表的长度大小 输出小的
l1,l2 = [1, 2, 3] ,[2, 3, 4, 5]
def func(*args):
    c = l1 if len(l1) < len(l2) else l2
    print(c)
func(l1,l2)


# 用'_'来切割列表,调用函数还执行
def func(*args):
    s = ""
    for i in args:
        s = s + str(i)+"_"
    print(s[:-1])
lst = [520,1314,'xijier']
func(*lst)




# 一下是错误代码 添加一行让代码能够运行
a = 10
def func():
    a = 1
    a += 1
    print(a)
func()
# 添加全局模式
"""
局部作用域对全局作用域的变量（此变量只能是不可变的数据类型）只能进行引用，而不能进行改变，只要改变就会报错，但是有些时候，
我们程序中会遇到局部作用域去改变全局作用域的一些变量的需求，这怎么做呢？这就得用到关键字global：
global第一个功能：在局部作用域中可以更改全局作用域的变量。
"""
a = 10
def func():
    global a
    a = 1
    a += 1
    print(a)
func()

#函数分析
def func1():
	print('in func1')

def func2():
	print('in func2')
ret = func1
ret()  #in func1
ret1 = func2
ret1() #in func2
ret2 = ret
ret3 = ret2
ret2()  #in func1
ret3()  #in func1

#函数分析
def func1():
    print('in func1')
def func2():
    print('in func2')
def func3(x, y):
    x()
    print('in func3')
    y()
print(111)
func3(func2, func1)
print(222)

# 111
# in func2
# in func3
# in func1
# 222



def func1():
    print('in func1')
def func2(x):
    print('in func2')
    return x
def func3(y):
    print('in func3')
    return y
ret = func2(func1)
ret()
#in func2
#in func1
ret2 = func3(func2)
ret3 = ret2(func1)
ret3()
# func3
# func2
# func1



#函数替换
def func(arg):
    return arg.replace('苍老师', '***')
def run():
    msg = "Alex的女朋友苍老师和大家都是好朋友"
    result = func(msg)
    print(result)
run()
data = run()
print(data)


#函数分析
data_list = []
def func(arg):
    return data_list.insert(0, arg)
data = func('绕不死你')
print(data)   # None 因为函数没有返回值
print(data_list)  # 执行完函数添加了一个参数


#函数分析
def func():
    print('你好呀')    #函数只显示print输出信息
    return '好你妹呀'   #但是函数有返回值
func_list = [func, func, func]   #列表里面存储是函数的内存地址
for item in func_list:
    val = item()   #将函数赋予给个变量 调用返回值
    print(val)
#和上面一样
def func():
    print('你好呀')
    return '好你妹呀'
func_list = [func, func, func]
for i in range(len(func_list)):
    val = func_list[i]()
    print(val)



def func():
    return '你麻痹'
def bar():
    return '尼玛炸了'
def base(a1, a2):
    return a1() + a2()
result = base(func, bar)
print(result)



#基础模式
for item in range(10):
    print(item)
print(item)

#添加函数
def func():
    for item in range(10):
        pass
    print(item)
func()


item = '老男孩'   # 外部变量
def func():
    item = 'alex'  #内部变量
    def inner():
        print(item)   # 往上寻找变量 发现内部变量alex
    for item in range(10):
        pass      #变量开始改变 变成9
    inner()  #最后在变量为9
func()


#代码分析
l1 = []
def func(args):
    l1.append(args)
    return l1
print(func(1))    #[1]
print(func(2))    #[1, 2]
print(func(3))    #[1, 2, 3]



name = '炸死'
def func():
    global name   #表示局部作用域可以对全局作用域进行修改了
    name = '死爹'

print(name)#没有调用函数 炸死
func()
print(name) # 调用函数了 全局作用域改变成了 死爹


name = '宝元'
def func():
    print(name)
func()


# 报错 局部变量不能对全局变量的修改
name = '宝元'
def func():
    print(name)
    name = 'alex'
func()


"""
不能更改全局变量。
在局部作用域中，对父级作用域（或者更外层作用域非全局作用域）的变量进行引用和修改，并且引用的哪层，从那层及以下此变量全部发生改变。
"""
count = 2
def func():
    count = 1
    def inner():
        nonlocal count
        count += 1
        print(count)  #第一次count 还是与原来的
    print(count)      # count+1 之后 变成2
    inner()
    print(count)      #内嵌函数走完了 还是2
func()
print(count)          #全局函数



"""
每次extendList被调用时，列表参数的默认值都将被设置为[].
但实际上的情况是，新的默认列表只在函数被定义的那一刻创建一次
"""
def extendList(val,list=[]):     #存储在默认参数
    list.append(val)
    return list
list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')
print('list1=%s'%list1) #[10, 'a']
print('list2=%s'%list2) #['123']
print('list3=%s'%list3) #[10, 'a']

#添加完成后 立即输出
def extendList(val,list=[]):
    list.append(val)
    return list
print('list1=%s'% extendList(10))
print('list2=%s'% extendList(123,[]))
print('list3=%s'% extendList('a'))



"""
用你的理解解释一下什么是可迭代对象，什么是迭代器。
        循环 重复的过程 含有__iter__方法的对象，都是可迭代对象。
        迭代器是一个可以迭代取值的工具
"""
# 使用while循环实现for循环的本质(面试题)
li=[1,2,3,4,5,6]
l1= li.__iter__()
while 1:
	try:
		print(l1.__next__())
	except:
		StopIteration
		break