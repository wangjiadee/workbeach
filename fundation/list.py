li = ["ajfidos","ckozxpcxkz","jgkfdo","nbvkn"]
print(len(li))

# 追加
li.append("seven")
print(li)

# 插入 inset
li.insert(1,"tony")
print(li)

# 替换
li[1] = 'xiejier'
print(li)

# 扩展列表
l2 = ["456","345","234","123"]
li.extend(l2)
print(li)

# 扩展字符串
li = ["ajfidos","ckozxpcxkz","jgkfdo","nbvkn"]
s = "xiejier"
li.extend(s)
print(li)

# 删除列表中的元素
li = ["ajfidos","ckozxpcxkz","jgkfdo","nbvkn"]
li.pop(2)
print(li)


li = ["ajfidos","ckozxpcxkz","jgkfdo","nbvkn"]
d = li.pop(1)
print(li)

# 删除多个元素
li = ["ajfidos","ckozxpcxkz","jgkfdo","nbvkn"]
del li[1:3]
print(li)


# list 的切片
li = [1, 3, 2, "a", 4, "b", 5,"c",["a","b","cc"]]
# 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
l1 = li[:3]
# 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
l2 = li[3:6]
# 通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
l3 = li[:7:2]
# 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
l4 = li[1:6:2]
# 通过对li列表的切片形成新的列表l5,l5 = ["c"]
l5 = li[7:8]
# 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
l6 = li[:7:-2]
# 通过对li列表的切片形成新的列表l7,l7 = ['cc', 'b', 'a']
l7 = li[8][-1:-4:-1]

# 将列表lis中的"tt"变成大写（用两种方式）。
lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][0]  = lis[3][2][1][0].upper()
print(lis)

lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][0]  = "TT"
print(lis)
# 将列表中的数字3变成字符串"100"（用两种方式）。
lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][1]  = "100"
print(lis)

lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][1]  = str(100)
print(lis)
# 将列表中的字符串"1"变成数字101（用两种方式）。
lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][2]  = "101"
print(lis)

lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][2]  = lis[3][2][1][2].replace("1","101")
print(lis)


# 将列表lis中的"tt"变成大写（用两种方式）。
lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][0]  = lis[3][2][1][0].upper()
print(lis)

lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][0]  = "TT"
print(lis)
# 将列表中的数字3变成字符串"100"（用两种方式）。
lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][1]  = "100"
print(lis)

lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][1]  = str(100)
print(lis)
# 将列表中的字符串"1"变成数字101（用两种方式）。
lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][2]  = "101"
print(lis)

lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][2]  = lis[3][2][1][2].replace("1","101")
print(lis)


li = ["find", "reno", "oppo"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_wusir_taibai"
# 列表list 转字符串
s = "_".join(li)
print(s)

# 5.for & range 循环列表
li = ["gz", "sz", "bj", "cd", "wz"]
for i in range(len(li)):
    print(li[i])
    
# 6.利用for循环和range将100以内所有的偶数添加到一个新列表中。

l1 = []
for i in range(1,101):
    if i % 2 == 0:
        l1.append(i)
print(l1)


# 7.利用for循环和range找出50以内能被3整除的数，并将这些数插入到一个新列表中。
l2 = []
for i in range(1,51):
    if i % 3 == 0:
        l2.append(i)
print(l2)

# 8.利用for循环和range从100 ~ -1，倒序打印。
for i in range(100,-2,-1):
    print(i)

# 9.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后在对列表的元素进行筛选，将能被4整除的数留下来。
lis = []
for i in range(100,10,-1):
    if i % 2 == 0:
        print(lis.append(i))
for i in lis:
    if i % 4 != 0:
        lis.remove(i)
print(lis)

#10.利用for循环和range，将1-30的数字中能被3整除的数改成* 依次添加到的列表当中
l3 = []
for i in range(1,31):
    if i % 3 ==0:
        l3.append("*")
        continue
    l3.append(i)
print(l3)


# 11.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
lis = []
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
for i in li:
    i = i.replace(" ","")
    if (i.startswith("A") or i.startswith("a")) and i.endswith("c"):
        lis.append(i)
    for q in lis:
        print(q)
print(lis)


# 12.开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# 则将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
l1 = []
li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
while True:
    x = 0
    user_input = input("please input fucking things: Q or q again logout ")
    if user_input.upper() == 'Q':
        break
    for x in li:
        if x in user_input:
            user_input = user_input.replace(x,"*" * len(x))
    l1.append(user_input)
print(l1)

# 13
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
for i in range(0,len(li)):
    if i != 4:
        print(li[i])
    elif i == 4:
        l2 = li[4]
        for x in l2:
            print(x)


# 14.用户输入一个数字,使用列表输出这个数字内的斐波那契数列,如下列表:(选做题)
# 用户输入100 输出[1,1,2,3,5,8,13,21,34,55,89]这个列表

a = 1
b = 1
sum_num = 0
lst = []
inp = int(input("pelase input fucking number："))
while sum_num <= inp:
    if a == 1:
        sum_num = b + a
        lst.append(a)
        lst.append(b)
        lst.append(sum_num)
    temp = sum_num
    if (sum_num + a) > inp:
        break
    sum_num += a
    a = temp
    lst.append(sum_num)
print(lst)