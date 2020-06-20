message1 = """--------------start at this--------------
name : reno
color: Y 
version: v1.0
---------------------------start at this--------------"""

message2 = """--------------start at this--------------
name : find
color: X
version: v2.0
---------------------------start at this--------------"""


message3 = """--------------start at this--------------
name : xp
color: W 
version: v3.0
---------------------------start at this--------------"""

name = input("input name：")
color = input("input color：")
version = input("input version：")

#格式化输出 ： 模板
message = """--------------start at this--------------
name : %s
color: %s
version: %s
---------------------------start at this--------------""" % (name,color,version)
print(message)
