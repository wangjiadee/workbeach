'''
@Author: Ralph
@Date: 2020-07-23 12:22:12
@LastEditTime: 2020-07-23 13:15:44
@FilePath: \python\module\序列化模块.py
@Effect: python 序列化模块
'''

"""
序列化模块： 将数据结构转化成特殊的序列
数据通过网络传输 转化成bytes执行，但是数据类型只有str类型 
由于str转化不回去 就产生了特殊的str ----序列化 json ----所有语言都是认可的

json 将数据结构转化成特殊的字符串 并且可以反转回去
json 类型：（2对四种）
dumps loads  只要用于网络传输，可以读写文件
dump load 只能读写文件 且读写一种数据
"""

# dumps
dic = {'username':'yaya','password':'123123','status': True}
import json
st = json.dumps(dic)
print(st,type(st))

# loads
dic1 = json.loads(st)
print(dic1,type(dic1))

l1 = [1,2,3,4,5,{"name":"ralph"}]
with open('json文件',encoding="utf-8",mode='w') as f:
    st = json.dumps(l1)
    f.write(st)


with open('json文件','r',encoding='utf-8') as f1:
    st = f1.read()
    l1 = json.loads(st)
    print(l1,type(l1))




# dump load 只能写入文件 并且只能写入一个数据结构
# dump load 不能一次写多个数据

l1 = [1,2,3,{"name":"ralph"}]
with open('json文件','w',encoding='utf-8') as f2:
    json.dump(l1,f2)   #一次dump一个数据  省略了write的步骤


# 数据读取
with open('json文件','r',encoding='utf-8') as f3:
    l1 = json.load(f3)
    print(l1,type(l1))



# ****************************************工作常用**************************************************
#一次写入多个数据 dump和load完成不了  要用dumps 和loads

l2 = [1,2,3,4,5]
l3 = [1,2,3,2,5]
l4 = [1,2,2,4,5]

# 写入
with open('json文件',encoding="utf-8",mode='w') as f4:
    f4.write(json.dumps(l2) + '\n')
    f4.write(json.dumps(l3) + '\n')
    f4.write(json.dumps(l4) + '\n')

#读取
with open('json文件',encoding="utf-8",mode='r') as f4:
    for i in f4:
        print(json.loads(i))
# ************************************************************************************************