"""
文件的写入
"""

import time

"""
# 打开文件，不存在的文件
f = open('D:\Python protest\学习笔记\文件操作\写入操作测试.txt', 'w', encoding='UTF-8')
# write写入
f.write('Hello World!!!')   # 写入内存中(缓冲区）
# flush刷新
f.flush()       # 将内存中积攒的内容，写入到硬盘的文件中
# close关闭， close内置了flush功能
f.close()
"""

# 打开一个已经存在的文件
f = open('D:\Python protest\学习笔记\文件操作\写入操作测试.txt', 'w', encoding='UTF-8')
# write写入，flush刷新
f.write('黑马程序员')
# close关闭
f.close()

# w模式，文件不存在，会创建新文件
# w模式，文件存在，会清空原有内容





