'''
Author: Ralph
Date: 2020-08-06 14:35:59
LastEditTime: 2020-08-06 17:08:17
LastEditors: Please set LastEditors
Description: 登录注册功能结合面向对象
FilePath: \workbeach\temp.py
'''


"""
NOTES: 

enumerate() ：循环列表 
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

"""

#注册之后，重启所有的用户丢失
#一次执行的注册行为，在之后所有的执行中都能正常登录

class User(object):
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
        

class Account(object):
    def __init__(self):
        self.user_list = []

    def login(self):
        """
        After Login,compared without self.user_list
        
        """
        for count in range(3):
            if not self.user_list:
                print('Pls register first')
                
            UserName = input('Please input username:')
            PassWord = input('Please input password:')
            for user in self.user_list:
                # 对象里面的属性去做比对
                if UserName == user.name and PassWord == user.pwd:
                    print('login success!')
                    break
                else:
                    print(">>>>ERROR: username or password mistake!")
            
            
    def register(self):
        """
        After successful registration, it will be placed in the list of user_list
        """
        # print('register')
        UserName = input('Please input username:')
        PassWord = input('Please input password:')
        Check_Pass = input('Please input u password again:')
        if PassWord == Check_Pass:
            user = User(UserName,PassWord)
            self.user_list.append(user)
            print('Register Success!')
        else:
            print('>>>>ERROR:Inconsistent input 2 times')
    def run(self):
        Frist_list = ['Log in','Register']
        while True:
            for index,item in enumerate(Frist_list,1):
                print(index,item)
            num = input('Please input operating number:').strip()
            if num == '1':
                self.login()
            elif num == '2':
                self.register()
            elif num.upper() == 'Q':
                break
############################################################
if __name__ == "__main__":
    obj = Account()
    obj.run()