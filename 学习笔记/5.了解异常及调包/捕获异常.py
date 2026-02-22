"""
捕获异常
"""

"""
捕获异常
语法:
    try:
        可能出现异常的代码
    except:
        如果出现异常执行的代码
"""

# 基本捕获语法演示
try:
    f = open(r'D:\Python protest\学习笔记\了解异常\abc.txt', 'r', encoding='UTF-8')
except:
    # 提示异常
    print('出现异常了，因为文件不存在，我将open模式，改为w模式打开')
    # 异常操作
    f = open(r'D:\Python protest\学习笔记\了解异常\abc.txt', 'w', encoding='UTF-8')
print('----------')
"""
捕获指定异常
基本语法：
    try：
        print(name)
    except NameError  as e:
        print('name变量名称未定义错误')
"""

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print('出现了变量未定义的异常')
    print(e)
print('------------')

"""
捕获多个异常
语法：
    try：
        print(10)
    except (NameError, ZeroDivisionError):
        print('ZeroDivision错误')

"""

# 捕获多个异常

try:
    1 / 0
    print(name)
except(NameError, ZeroDivisionError) as e:
    print("出现了变量未定义或者除数为0的异常")
    print(e)
print('---------')
"""
捕获所有异常
法1：
    try:
        代码1
    except Exception as e:
        代码2

法2：
    try:
        代码1
    except:
        代码2
        
"""


"""
异常完整语法：
    
    try:
        代码1
    except:
        代码2
    else:
        代码1没有异常时执行的代码
"""

"""
异常的finally
---表示无论是否异常都要执行的代码
语法：
    try:
        代码1
    except:
        代码2
    else:
        代码3
    finally：
        代码4
"""

# finally异常演示
try:
    f = open(r'D:\Python protest\学习笔记\了解异常\abc.txt', 'r', encoding='UTF-8')
except:
    print('出现异常了')
else:
    print('开森捏，没有出现异常')
finally:
    print('我是finally，有没有异常我都要执行')
    f.close()


