# 文件操作 读的权限 并打印
# 以只读方式打开文件，文件的指针将会放在文件的开头。是文件操作最常用的模式，也是默认模式
with open('a1.txt','r',encoding='utf-8') as f:
    print(f.read())

#  行尾追加
with open('a1.txt','a',encoding='utf-8') as f:
    print(f.write('你全家非主流，你妈黒袜子，你爸锡纸头'))
# 
# 读写权限 行尾追加
with open('a1.txt','r+',encoding='utf-8') as f:
    print(f.read())
    print(f.write('信不信由你，反正我信了'))

# 替换
with open('a1.txt','w',encoding='utf-8') as f:
    print(f.write('''每天坚持一点，
每天努力一点，
每天多思考一点，
慢慢你会发现，
你的进步越来越大。'''))
# 

"""
1. 文件window下的路径配置:  r'C:\\Users\尼玛炸了\Desktop\\111.txt' 在路径的整体前面加一个r。（推荐）
2. read() read()将文件中的内容全部读取出来;弊端 如果文件很大就会非常的占用内存,容易导致内存奔溃.
3. readline()读取每次只读取一行,注意点:readline()读取出来的数据在后面都有一个\n
4. readlines() 返回一个列表，列表里面每个元素是原文件的每一行，如果文件很大，占内存，容易崩盘。
5. rb模式：以二进制格式打开一个文件用于只读
6. w :如果文件不存在，利用w模式操作文件，那么它会先创建文件，然后写入内容
7. wb模式：以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，
   并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如：图片，音频，视频等
8. a 如果文件不存在，利用a模式操作文件，那么它会先创建文件，然后写入内容
"""

# 以r的模式打开原文件，利用for循环遍历文件句柄。
f = open('a1.txt',mode='r',encoding='utf-8')
print(f.read())
for i in f:
    print(i)

# readlines() 返回一个列表
f = open('a1.txt',mode='r',encoding='utf-8')
f1 = f.readlines()
print(f1)
# 会有空格
for i in f1:
    print(i)


# 以r模式读取指定字符。
f = open('a1.txt',mode='r',encoding='utf-8')
print(f.read(4))


# 以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
# readline()读取出来的数据在后面都有一个\n
f = open('a1.txt',mode='r',encoding='utf-8')
print(f.readline().strip())


# f.seek 表示可以移动光标到指定位置
with open("a1.txt",'a+',encoding="utf-8") as f, \
    open("a1.txt",'r',encoding="utf-8") as f1:
    f.seek(0)
    f.write("\n尼玛炸了")
    print(f.read())
    

# 通过代码，将其构建成这种数据类型：
# [{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
with open("a1.txt","r",encoding="utf-8") as f:
    lst,sum = [],0
    for i in f.readlines():
        k,v,j = i.split(" ")
        lst.append({"name":k,"price": int(v),"amount":int(j)})
        sum += int(v)
    f.close()
    print(lst,sum)


# 多文件的改的操作
with open("a1.txt","r",encoding="utf-8") as f1,open("a.txt","w",encoding="utf-8") as f2:
    for line in f1:
        new = line.replace("alex","mdzz")
        f2.write(new)


# name:apple price:10 amount:3 year:2012
# name:tesla price:100000 amount:1 year:2013
# .......

# 通过代码，将其构建成这种数据类型：
# [{'name':'apple','price':10,'amount':3,year:2012},
# {'name':'tesla','price':1000000,'amount':1}......]
f = open("a1.txt",'r+',encoding="utf-8")
li,sum=[],0
for line in f:
    dic={}
    lst = line.strip().split(" ")
    for i in lst:
        lst1=i.split(":")
        print(lst1)
        if lst1[0]== "name":
            dic[lst1[0]]=lst1[1]
        elif lst1[0]== "year":
            pass
        else:
            dic[lst1[0]]=int(lst1[1])
    sum+=dic["price"]*dic["amount"]
    li.append(dic)
print(li,sum)
f.close()




#  序号 部门 人数 平均年龄 备注
#  1 python 30 26 单身狗
#  2 Linux 26 30 没对象
#  3 运营部 20 24 女生多
#  .......
# 
# 通过代码，将其构建成这种数据类型：
# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},
# ......]

f = open("a1.txt",'r+',encoding="utf-8")
result,dic = [],{}
for i in f.readlines(1):
    i = i.strip().split()
    for line in f:
        li =line.strip().split()
        dic={i[0]:li[0],i[1]:li[1],i[2]:int(li[2]),i[3]:int(li[3]),i[4]:li[4]}
        result.append(dic)
    print(result)