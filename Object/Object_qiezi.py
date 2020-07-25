'''
@Author: Ralph
@Type_file: Python
@Date: 2020-07-25 13:58:14
@LastEditTime: 2020-07-25 17:26:18
@FilePath: \workbeach\Object\Object_qiezi.py
@Effect: 面向对象的楔子
'''


alex = {
    'name': 'alex',
    'sex': '不详',
    'job': '搓澡工',
    'level': 0,
    'hp': 250,
    'weapon': '搓澡巾',
    'ad': 1
}


xb = {
    'name': '小白',
    'kind': '泰迪',
    'hp': 5000,
    'ad': 249
}

print(alex, xb)


def Person(name, sex, job, hp, weapon, ad, level=0):   # 人模子
    def 搓(dog):
        dog['hp'] -= dic['ad']
        print('%s 攻击了 %s,%s掉了%s点血' %
              (dic['name'], dog['name'], dog['name'], dic['ad']))
    dic = {
        'name': name,
        'sex': sex,
        'job': job,
        'level': level,
        'hp': hp,
        'weapon': weapon,
        'ad': ad,
        'action': 搓
    }
    return dic


def Dog(name, kind, hp, ad):
    def 舔(person):  # 函数不是一个公用的函数 是一个有归属感的函数
        person['hp'] -= dic['ad']
        print('%s 舔了 %s,%s掉了%s点血' %
              (dic['name'], person['name'], person['name'], dic['ad']))
    dic = {
        'name': name,
        'kind': kind,
        'hp': hp,
        'ad': ad,
        'action': 舔
    }
    return dic


alex = Person('alex', '不详', '搓澡工', 250, '搓澡巾', 1)
wusir = Person('wusir', 'male', '法师', 500, '打狗棍', 1000)
小白 = Dog('小白', '泰迪', 5000, 249)
小金 = Dog('小金', '柯基', 10000, 499)

小白['action'](alex)
alex['action'](小白)
