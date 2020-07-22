name = 'RALPH'


__all__ = ['name']

def read1():
    print('RALPH123>>>>', name)

def read2():
    print('>>>>>>>>>>>>>>>>R')
    read1()



def change():
    global name
    name = 'barry'
    print(name)


print(__name__)