'''
Author: Ralph
Type_file[python//GO//json//Yaml//Other]: [python//GO//json//Yaml//Other]
Date: 2020-09-12 04:15:21
LastEditTime: 2020-09-12 04:48:38
FilePath: /pyenv/code/workbeach/Object/Object_stu_system/bin/system_run.py
Effect: 学生系统
'''
import sys
import os
Base_Path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(Base_Path)
from code import src

# start 
if __name__ == '__main__':
    src.main()
    