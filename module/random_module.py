'''
@Author: your name
@Date: 2020-07-24 10:29:46
@LastEditTime: 2020-07-24 10:48:18
@LastEditors: Please set LastEditors
@Description: randome_module
@FilePath: \python\workbeach\module\random_module.py
'''
import random
random.random()      # 大于0且小于1之间的小数
random.uniform(1,3) #大于1小于3的小数
#随机整数
random.randint(1,5)  # 大于等于1且小于等于5之间的整数
random.randrange(1,10,2) # 大于等于1且小于10之间的奇数
#随机选择一个返回
random.choice([1,'23',[4,5]])  # #1或者23或者[4,5]
random.sample([1,'23',[4,5]],2) # #列表元素任意2个组合




# 生成验证码：
def v_code():
    code = ''
    for i in range(4):
        num = random.randint(0,9)
        alf = chr(random.randint(65,90))
        add=random.choice([num,alf])
        code="".join([code,str(add)])
    return code
print(v_code())