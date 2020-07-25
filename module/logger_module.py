'''
@Author: ralph
@Date: 2020-07-24 14:34:21
@LastEditTime: 2020-07-25 13:51:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \workbeach\module\logger_module.py
'''

"""
logging配置
"""


from logging import handlers
import time
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/tmp/test.log',
                    filemode='w')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

# 输出内容是有等级的 : 默认处理warning级别以上的所有信息
# logging.debug('debug message')          # 调试
# logging.info('info message')            # 信息
# logging.warning('warning message')      # 警告
# logging.error('error message')          # 错误
# logging.critical('critical message')    # 批判性的


"""
默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志.
这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG），
默认的日志格式为日志级别：Logger名称：用户输出消息。




logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有：

filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：指定handler使用的日志显示格式。
datefmt：指定日期时间格式。
level：设置rootlogger（后边会讲解具体概念）的日志级别
stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件(f=open(‘test.log’,’w’))，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
"""


logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log', encoding='utf-8')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setLevel(logging.DEBUG)

fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)  # logger对象可以添加多个fh和ch对象
logger.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')


# 无论你希望日志里打印哪些内容,都得你自己写,没有自动生成日志这种事儿
# 输出到屏幕
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)
logging.warning('warning message test2')
logging.error('error message test2')
logging.critical('critical message test2')


# 输出到文件,并且设置信息的等级
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    filename='tmp.log',
    level=logging.DEBUG

)
logging.debug('debug 信息错误 test2')
logging.info('warning 信息错误 test2')
logging.warning('warning message test2')
logging.error('error message test2')
logging.critical('critical message test2')


# 同时向文件和屏幕上输出 和 乱码
fh = logging.FileHandler('tmp.log', encoding='utf-8')
# fh2 = logging.FileHandler('tmp2.log',encoding='utf-8')
sh = logging.StreamHandler()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.DEBUG,
    # handlers=[fh,sh,fh2]
    handlers=[fh, sh]
)
logging.debug('debug 信息错误 test2')
logging.info('warning 信息错误 test2')
logging.warning('warning message test2')
logging.error('error message test2')
logging.critical('critical message test2')


# 做日志的切分
sh = logging.StreamHandler()
rh = handlers.RotatingFileHandler(
    'myapp.log', maxBytes=1024, backupCount=5)   # 按照大小做切割
fh = handlers.TimedRotatingFileHandler(
    filename='x2.log', when='s', interval=5, encoding='utf-8')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.DEBUG,
    # handlers=[fh,sh,fh2]
    handlers=[fh, rh, sh]
)
for i in range(1, 100000):
    time.sleep(1)
    logging.error('KeyboardInterrupt error %s' % str(i))
