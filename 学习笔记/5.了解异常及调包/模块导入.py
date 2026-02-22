"""
演示python模块导入
"""

# 使用import导入time模块使用sleep功能（函数）(需要写time.xxx)
import time
print('你好')
time.sleep(5)
print('我好')


# 只导入time模块中的sleep功能（函数）
from time import sleep
print('你好')
sleep(5)
print('我好')

# 使用*导入time模块的全部功能(无需写time.xxx)
from time import *
print('你好')
sleep(5)
print('我好')

# 使用别名导入
# import 模块 as xx  (写xx.)
# from 模块 import 函数 as xx ( 写xx() )












