'''
Author: Ralph
Type_file[python//GO//json//Yaml//Other]: [python]
Date: 2020-09-12 04:58:13
LastEditTime: 2020-09-12 06:45:52
FilePath: /pyenv/code/workbeach/Object/Object_stu_system/code/src.py
Effect: 学生系统主程序
'''
from lib import common
import os
import sys
import time
import pickle
#Define dir path
sys_path = os.path.dirname(os.path.dirname(__file__))
# Define userinfo Storage path
data_path = os.path.join(sys_path, 'db', 'userinfo')
# Define Courseinfo Storage path
Course_path = os.path.join(sys_path, 'db', 'Course')
# Define studentinfo Storage path
Student_path = os.path.join(sys_path, 'db', 'Student')





status_dict = {
    'username' : None,
    'status' : None,
}
# 对应表
dic_userinfo = {}
Student_Object_list = ['Show_Course','Selected_Course','View_Selected_Course','exit']
Manager_Object_list = ['Create_Course','Create_Student','Show_Courses','Show_Students','Show_Students_Courses','exit']

class Course(object):
    def __init__(self, course_name, course_price, course_time,course_teacher):
        self.course_name = course_name
        self.course_price = course_price
        self.course_time = course_time
        self.course_Teacher = course_teacher


class Student(object):
    def __init__(self, student_name):
        self.student_name = student_name
        self.choose_course = []

    def Show_Course(self):
        """
        Students can view optional courses 
        """
        pass

    def Selected_Course(self):
        """
        Students can choose courses
        """
        pass

    def View_Selected_Course(self):
        """
        Students can view selected courses
        """
        pass

    def exit(self):
        """
        Exit
        """
        pass


class Manager(object):
    def __init__(self.Manager_name):
        self.Manager_name = Manager_name

    def Create_Course(self):
        '''
        Administrators can create course
        '''
        pass

    def Create_Student(self):
        '''
        Administrators can create student users
        '''
        pass

    def Show_Courses(self):
        '''
        Administrator can view selected courses
        '''
        pass

    def Show_Students(self):
        '''
        Administrators can view all student information
        '''
        pass

    def Show_Students_Courses(self):
        '''
        The administrator can view the course selection status of 
        all students
        '''
        pass

    def exit(self):
        '''
        exit
        '''
        pass


# Define Login Function
def Login():
    """
    AllUser login
    """
    n = 0
    while n < 3:
        if not status_dict['status']:
            username = input('>>>>Pls input u username :') 
            password = input('>>>>Pls input u password :')
            sec_pass = input('Pls input u password aging:')
            if sec_pass == password:
                password = common.encrypt(password)
                with open(data_path, mode='r', encoding='utf-8') as f1:
                    for i in f1:
                        a, b, c = i.strip().split('|')
                        dic_userinfo[a] = [b, c]
                    if username in dic_userinfo and password == dic_userinfo[username][0] and dic_userinfo[username][1] == 'Manager':
                        print('Welcome! %s'%(username))
                        return 'Manager',username
                    elif username in dic_userinfo and password == dic_userinfo[username][0] and dic_userinfo[username][1] == 'Student':
                        print('Hello！ %s student'%(username))
                        return 'Student',username
                    else:
                        n+=1
                        print(f'Login ERROR:u have {3-n}times!')
            else:
                exit('ERROR: The password entered is not the same')
    if n == 3:
        exit('System Error: Too many login failures, account locked!')

Student_UI = '''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||//\\
                / _||||| -:- |||||-\\
               |   | \\\  - /// |   ||
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|   1. 查看所有课程         2.选择课程          |
|   3. 查看所选课程         4.退出程序          |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
Manager_UI = '''
　　┏┓　　　┏┓+ +
　┏┛┻━━━┛┻┓ + +
　┃　　　　　　　┃ 　
　┃　　　━　　　┃ ++ + + +
 ████━████ ┃+
　┃　　　　　　　┃ +
　┃　　　┻　　　┃
　┃　　　　　　　┃ + +
　┗━┓　　　┏━┛
　　　┃　　　┃　　　　　　　　　　　
　　　┃　　　┃ + + + +
　　　┃　　　┃
　　　┃　　　┃ +  
　　　┃　　　┃    　　
　　　┃　　　┃　　+　　　　　　　　　
　　　┃　 　　┗━━━┓ + +
　　　┃ 　　　　　　　┣┓
　　　┃ 　　　　　　　┏┛
　　　┗┓┓┏━┳┓┏┛ + + + +
　　　　┃┫┫　┃┫┫
　　　　┗┻┛　┗┻┛+ + + +
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|   1. 创建课程               |
|   2. 创建学生帐号           |
|   3. 查看全部课程           |
|   4. 查看所有学生           |
|   5. 查看所有学生的选课情况 |
|   6. 退出                   |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''



# 
def main():
    USER_CLASS = Login()
    if USER_CLASS[0] == 'Student':
        while True:
            print(Student_UI)
            Student_Input = input('>>>>Pls chooes u want function:').strip()
            with open(Student_path, "rb") as f1:
                while 1:
                    try:
                        obj_student = pickle.load(f1)
                        if obj_student.name == USER_CLASS[1]:
                            break
                    except Exception:
                        break
            if hasattr(obj_student, Student_Object_list[int(Student_Input) - 1]):
                getattr(obj_student,Student_Object_list[int(Student_Input) - 1])(obj_student)
    if USER_CLASS[0] == 'Manager':
        while True:
            print(Manager_UI)
            Manager_Input = input('>>>>Pls chooes u want function:').strip()
            obj_student = Manager(USER_CLASS[1])
            if hasattr(obj_student, Manager_Object_list[int(Manager_Input) - 1]):
                getattr(obj_student,Manager_Object_list[int(Manager_Input) - 1])() 