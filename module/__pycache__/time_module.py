'''
@Author: your name
@Date: 2020-07-24 11:32:18
@LastEditTime: 2020-07-24 14:17:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\workbeach\module\__pycache__\time_module.py
'''
import time

"""
时间模块：
1：时间戳(timestamp) ：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。 
2：格式化的时间字符串(Format String)： ‘1999-12-06’

%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身


"""

#常用方法
time.sleep(1)
# (线程)推迟指定的时间运行。单位为秒。

# 获取当前时间戳
a = time.time()   #1595561932.0168152
print(a)


#时间字符串
a2=time.strftime("%Y-%m-%d %X")
print(a2)
a3 =time.strftime("%Y-%m-%d %H-%M-%S")
print(a3)

#时间元组:localtime将一个时间戳转换为当前时区的struct_time
a3 = time.localtime()
print(a3)
# time.struct_time(tm_year=2020, tm_mon=7, tm_mday=24, tm_hour=11, tm_min=46, tm_sec=3, tm_wday=4, tm_yday=206, tm_isdst=0)



"""
时间戳是计算机能够识别的时间；时间字符串是人能够看懂的时间；元组则是用来操作时间的
"""
# 格式化时间 ---->  结构化时间
ft = time.strftime('%Y/%m/%d %H:%M:%S')
st = time.strptime(ft,'%Y/%m/%d %H:%M:%S')
print("YY：",st)


# 结构化时间 ---> 时间戳
t = time.mktime(st)
print(t)

# 时间戳 ----> 结构化时间
t = time.time()
st = time.localtime(t)
print(st)

# 结构化时间 ---> 格式化时间
ft = time.strftime('%Y/%m/%d %H:%M:%S',st)
print(ft)

#结构化时间 --> %a %b %d %H:%M:%S %Y串
#time.asctime(结构化时间) 如果不传参数，直接返回当前时间的格式化串
time.asctime(time.localtime(1500000000))
'Fri Jul 14 10:40:00 2017'
time.asctime()
'Mon Jul 24 15:18:33 2017'

#时间戳 --> %a %d %d %H:%M:%S %Y串
#time.ctime(时间戳)  如果不传参数，直接返回当前时间的格式化串
time.ctime()
'Mon Jul 24 15:19:07 2017'
time.ctime(1500000000)
'Fri Jul 14 10:40:00 2017' 

t = time.time()
ft = time.ctime(t)
print(ft)

st = time.localtime()
ft = time.asctime(st)
print(ft)





# 计算时间差：
true_time=time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))
time_now=time.mktime(time.strptime('2017-09-12 11:00:00','%Y-%m-%d %H:%M:%S'))
dif_time=time_now-true_time
struct_time=time.gmtime(dif_time)
print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,
                                       struct_time.tm_mday-1,struct_time.tm_hour,
                                       struct_time.tm_min,struct_time.tm_sec))