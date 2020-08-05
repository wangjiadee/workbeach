#使用linux服务的python指引
#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
It provide the class which can operate databases,like insert,delete,update,select.
It need python package 'pymysql'.
And here is create table sentence:
然后可以输出一些已经在数据库中的表格 并且格式输出
CREATE TABLE `Old_boy` (
    Student_Id int(15) NOT NULL AUTO_INCREMENT,
    Student_Name varchar(255) DEFAULT NULL,
    Student_Score varchar(255) DEFAULT NULL,
)
可以写很多
"""

# 针对老的python2.x 的代码转化问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 导入py的mysql 数据库
import pymysql
import os
import time
# 导入基于进程的并行问题
from multiprocessing import Pool

# 定义一些规范类
class SqlTest(object):
    # 定义数据库的简单类
    def __init__(self, host, user, password, database, charset="utf8", port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.port = port
    # 定义连接数据库的类 和与数据库交互
    def Collect(self):
        self.con = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database, charset=self.charset)
        self.cursor = self.con.cursor()
    # 定义数据库交互后的关闭
    def Close(self):
        self.cursor.close()
        self.con.close()
    # 交互之后的清理
    def __enter__(self):
        self.Collect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Close():
        


class SQL(object):
    '''
    it provide that class which can operate databases
    '''

    def __init__(self, host, user, password, database, charset="utf8", port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.port = port

    def Insert(self,table_name):
        """
        指导相关信息
        """
        with SQLContext(self.host, self.user, self.password, self.database, self.charset, self.port) as c_sql:
            pass 
        
    def Select(self,table_name):
        """
        指导相关信息
        """
        with SQLContext(self.host, self.user, self.password, self.database, self.charset, self.port) as c_sql:
            pass 
        
    def Delete(self,table_name):
        """
        指导相关信息
        """
        with SQLContext(self.host, self.user, self.password, self.database, self.charset, self.port) as c_sql:
            pass 
    def Update(self,table_name):
        """
        指导相关信息
        """
        with SQLContext(self.host, self.user, self.password, self.database, self.charset, self.port) as c_sql:
            pass 

c_sql = SQL(host="123.123.123.123", user="root", password="123456", database="student", port=3306)

if __name__ == "__main__":
    print c_sql.Select(table_name="表名字")
