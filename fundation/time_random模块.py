
# 写函数：用户输入某年某月，判断这是这一年的第几天（需要用Python的结构化时间）。
import time
data = input("请输入日期:(2020.02.02)")
ret = time.strptime(data,"%Y.%m.%d")
print(f"这是{ret.tm_year}的第{ret.tm_yday}天！")



#用户输入一个"2019-7-26 20:30:30"和当前时间相比,一共过去了多少年多少月多少天到少小时多少分钟
import time
date = input("请输入时间：")
ret = time.mktime(time.strptime(date,"%Y-%m-%d %H:%M:%S")) - time.time()   # 时间戳差
# print(ret)
s_time = time.gmtime(ret)
print(f"过去了{s_time.tm_year-1970}年，{s_time.tm_mon-1}月，{s_time.tm_mday-1}日，"
      f"{s_time.tm_hour}小时，{s_time.tm_min}分")


import random
def captcha():
    """
    随机码生成
    :return: 四位随机码（包含数字字母大小写）
    """
    cap = ""
    for i in range(4):
        num = random.randint(0, 9)
        num = str(num)
        cop_let = chr(random.randint(65, 90))
        sma_let = chr(random.randint(97, 122))
        lst = [num, cop_let,sma_let]
        ret = random.choice(lst)
        cap = "".join([cap,ret])
    return cap
print(captcha())



import random
def captcha():
    """
    随机码生成
    :return: 四位随机码（包含数字字母大小写）
    """
    ls = []
    for i in range(2):
        num = random.randint(0, 9)
        num = str(num)
        let_lower = chr(random.randint(65, 90))
        let_upper = chr(random.randint(97, 122))
        lst = [num, let_lower, let_upper]
        ret,ret1 = random.choices(lst,k=2)
        ls.append(ret)
        ls.append(ret1)
    cap = "".join(ls)
    return cap
print(captcha())