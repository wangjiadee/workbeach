'''
Author: Ralph
Type_file[python//GO//json//Yaml//Other]: [python]
Date: 2020-09-12 05:41:17
LastEditTime: 2020-09-12 05:46:41
FilePath: /pyenv/code/workbeach/Object/Object_stu_system/lib/common.py
Effect: DO
'''

import os
import logging.config
import hashlib
from code import src
def encrypt(n):
    ret = hashlib.md5()
    ret.update(n.encode("utf-8"))
    return ret.hexdigest()


