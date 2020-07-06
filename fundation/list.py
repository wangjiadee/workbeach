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
