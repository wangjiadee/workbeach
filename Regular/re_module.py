'''
@Author: Ralph
@Type_file: Python
@Date: 2020-07-25 11:50:37
@LastEditTime: 2020-07-25 13:36:37
@FilePath: \workbeach\Regular\re_module.py
@Effect: RE模块
'''
"""
re 模块
#findall
    会优先显示分组内的内容
    取消优先显示（？：正则）
findall(正则,待匹配字符串,flag) :  返回所有匹配项的列表

#search
返回一个变量,通过group取到的是第一个匹配的项
    只能返回第一个符合条件的项
    得到的结构需要.group取值
    默认获取完整的匹配结果
    通过group(n)来获取n个分组中的内容
"""
"""
# 功能
# 性能
    # 时间 :
        # 你要完成一个代码所需要执行的代码行数
        # 你在执行代码的过程中,底层程序是如何工作的
    # 空间
        # 是占用了宝贵的内存条资源
        # 影响程序的执行效率
# 用户体验
"""

# split 通过正则表达式匹配的内容进行分割
import re
ret = re.split('\d+', 'wjd520xj')
print(ret)  # ['wjd', 'xj']
ret1 = re.split('\d(\d)\d', 'wangjiadee321ralph')
print(ret1)  # ['wangjiadee', '2', 'ralph']


# sub  替换方法
ret2 = re.sub('\d+', 'mdzz', 'wangjaide2wddd')
print(ret2)

# subn  返还替换的次数
# subn 替换,在sub的基础上,返回一个元组,第一个内容是替换结果,第二个是替换次数
ret3 = re.subn('\d+', "sb", "world2world2oppo")
print(ret3)

# match   用户输入匹配内容
# 只匹配指定开头  match 是用来规定这个字符串必须是怎么样的
# search 是用来寻找某一个字符串
ret4 = re.match('\d+', '123wva343mas')
print(ret4.group())

# compile -- 节省代码时间的工具（多次重复使用一个正则表达式，就可以使用）
# 假如同一个正则表达式要被使用多次
# 节省了多次解析同一个正则表达式的时间
ret5 = re.compile('\d+')
ret6 = ret5.search('ralph1234')
ret7 = ret5.findall('ralph1234')
print(ret7)
print(ret6)


# finditer -- 节省空间
# finditer :返回一个迭代器,通过迭代取到的是一个变量,通过group取值
ret8 = re.finditer('\d+', 'ralph18898')
for i in ret8:
    print(i.group())


# 列表不能用insert
# 列表不能用pop(n)


# 先节省时间在节省空间
rett = re.compile('\d+')
res = rett.finditer('alsjdks9218e8')
for r in res:
    print(r.group())


# 分组命名
# ?P<name1>
# (?P<名字>正则表达式)
# ret.group('名字')
# 分组命名 取消分组优先
# (?P<组名>正则)  (?P=组名)  (?:正则)

res = re.search('\d\d\d(?P<name1>\w+?)\d(\w)\d\d\d(?P<name2>\w+?)\d(\w)',
                '123abc45678agsf_123abc45678agsf123abc45678agsf')
print(res.group('name1'))
print(res.group('name2'))


# 分组命名的引用
exp = '<abc>akd7008&(&*)hgdwuih</abc>008&(&*)hgdwuih</abd>'
res2 = re.search('<(?P<tag>\w+)>.*?</(?P=tag)>', exp)
print(res2)


# 直接使用分组的索引
res3 = re.search(r'<(\w+)>.*?</\1>', exp)
print(res3)

# r 表示默认转义

# 分组命名(?P<组名>正则) (?P=组名)
# 有的时候我们要匹配的内容是包含在不想要的内容之中的,
# 只能先把不想要的内容匹配出来,然后再想办法从结果中去掉


# 加括弧 表示优先显示
rett2 = re.findall(r"\d+\.\d+|(\d+)", "1-2*(60+(-40.35/5)-(-4*3))")
print(rett2)
rett3 = ['1', '2', '60', '', '5', '4', '3', '', '']
rett3.remove('')
print(rett3)


# ********
rett4 = filter(lambda n: n, rett3)
print(list(rett4))
