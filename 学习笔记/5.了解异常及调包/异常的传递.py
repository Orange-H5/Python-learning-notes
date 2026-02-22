"""
演示异常的传递性质
"""

def func1():
    print('func1开始执行')
    num = 1/0
    print('func1执行结束')

def func2():
    print('func2开始执行')
    func1()
    print('func2执行结束')

def func3():
    try:
        func2()
    except Exception as e:
        print(f'出现异常了，异常的信息是:{e}')

func3()









