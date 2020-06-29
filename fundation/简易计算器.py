# 多位数相加计算器
cal = input("please input fucking num ,must have '+' between each number:")
s1 = cal.split("+")
sum = 0
for i in s1:
    sum += int(i.strip())
print(sum)

