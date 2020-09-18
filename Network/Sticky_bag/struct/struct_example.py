'''
Author: Ralph
Type_file[python//GO//json//Yaml//Other]: [python//GO//json//Yaml//Other]
Date: 2020-09-18 10:16:51
LastEditTime: 2020-09-18 10:19:42
FilePath: /pyenv/Sticky_bag/struct/struct_example.py
Effect: DO
'''
import struct

n1 = 12332231
n2 = 233322
n3 = 444

r = struct.pack('i',n1)
r2 = struct.pack('i',n2)
r3 = struct.pack('i', n3)

print(len(r))
print(len(r2))
print(len(r3))