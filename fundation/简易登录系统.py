
First_msg = """

>>>按1.请注册（第一次登陆 请先注册！）
>>>按2.请登录
>>>按3.进入文章页面
>>>按4.进入评论页面
>>>按5.进入日记页面
>>>按6.进入收藏页面
>>>按7.注销账号
>>>按8.退出整个程序
"""
Login_msg = """

>>>按3.进入文章页面
>>>按4.进入评论页面
>>>按5.进入日记页面
>>>按6.进入收藏页面
>>>按7.注销账号
>>>按8.退出整个程序
"""

print(First_msg)
flag = False
def login():
    """
    登录功能
    :return:如果是登录三次未成功,返回3,如果在三次之内成功,则返回登录的用户名
    """
    count = 0
    while count < 3:
        with open("userinfo_blogs.txt", "r", encoding="UTF-8") as f3:
            flage = False
            login_username = input("请输入登录用户名:").replace(" ", "")
            login_password = input("请输入登录密码:").replace(" ", "")
            for i in f3:
                if login_username.strip() == i.strip().split(":")[0] and login_password.strip() == i.strip().split(":")[1]:
                    # print(a,b)
                    flage = True
                    break
                # print(login_username,login_password)
                # print(i.split(":")[0],i.split(":")[1])
            if flage == False:
                # print(login_username)
                # print(login_password)
                print("登录失败!")
                count += 1
            else:
                print("登陆成功!")
                print(Login_msg)
                global flag
                flag = True
                return login_username
    return count

def register():
    """
    :return register username and password
    """

    while 1:
        error_F = True
        register_username  = input(">>>>请输入注册用户(仅支持数字和大小写字母)：")
        for i in register_username:
            if not (48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122):
                print("仅支持数字和大小写字母,请重新输入！")
                error_F = False
                break
        if error_F:
            register_password = input(">>>>请输入注册的密码(仅支持6-14字符！)：")
            if not (6 <= len(register_password) <= 14):
                print("不是TM说了6-14个字符吗？")
            else:
                break
    return register_username,register_password

def into_article(ret_login):
    print(f"Welcome to Fucking article center!{ret_login}")
    print("你可以偷看别人的日志文章")
    print("*******************************************************************")
    print(Login_msg)

def into_commit(ret_login):
    print(f"Welcome to Fucking commit center!{ret_login}")
    print("你可以做网络喷子")
    print("*******************************************************************")
    print(Login_msg)

def into_diary(ret_login):
    print(f"Welcome to Fucking diary center!{ret_login}")
    print("你可以写你的小秘密")
    print("*******************************************************************")
    print(Login_msg)

def into_collection(ret_login):
    print(f"Welcome to Fucking collection center!{ret_login}")
    print("你可以收藏别人的日志文章")
    print("*******************************************************************")
    print(Login_msg)

def logout():
    print("ByeBye!")
    global flag
    flag = False

def exit():
    print("退出成功！再见了您嘞")
    return "break"


########################################################################################################################
########################################################################################################################

while 1:
    User_Num = input(">>>>>请输入选择的类型")
    if User_Num.isdecimal() and 1 <= int(User_Num) <= 7:
        User_Num = int(User_Num)
        if User_Num == 1:
            reg_username,reg_password = register()
            with open("userinfo_blogs.txt", "r", encoding="UTF-8") as f:
                reg_flag =True
                for i in f:
                    i = i.split(":")
                    if reg_username == i[0]:
                        print("用户名已经存在！")
                        reg_flag = False
                if reg_flag == True:
                    with open("userinfo_blogs.txt", "a", encoding="UTF-8") as f1:
                        f1.write(f"{reg_username}:{reg_password}")
                        print("注册成功!")
        elif User_Num == 2:
            ret_login = login()
            if str(ret_login) == "3":
                print("M的，登录3次还错吗？")
                print("再见!")
                break
        elif User_Num == 3:
            if not flag:
                print("先登陆再说")
                ret_login = login()
                if str(ret_login) == '3':
                    print("M的，登录3次还错吗？")
                    print("再见!")
                    break
                into_article(ret_login)
            else:
                into_article(ret_login)

        elif User_Num == 4:
            if not flag:
                print("先登陆再说")
                ret_login = login()
                if str(ret_login) == '3':
                    print("M的，登录3次还错吗？")
                    print("再见!")
                    break
                into_commit(ret_login)
            else:
                into_commit(ret_login)
        elif User_Num == 5:
            if not flag:
                print("先登陆再说")
                ret_login = login()
                if str(ret_login) == '3':
                    print("M的，登录3次还错吗？")
                    print("再见!")
                    break
                into_diary(ret_login)
            else:
                into_diary(ret_login)
        elif User_Num == 6:
            if not flag:
                print("先登陆再说")
                ret_login = login()
                if str(ret_login) == '3':
                    print("M的，登录3次还错吗？")
                    print("再见!")
                    break
                into_collection(ret_login)
            else:
                into_collection(ret_login)
        elif User_Num == 7:
            if not flag:
                print("先登陆再说")
                ret_login = login()
                if str(ret_login) == '3':
                    print("M的，登录3次还错吗？")
                    print("再见!")
                    break
                logout()
            else:
                logout()
    elif User_Num == '8':
        break_login = exit()
        try:
            # eval ：把一个字符串的以函数的方式进行返回
            eval(break_login)
        except SyntaxError:
            break

    else:
            print("请输入正确的序号!")
