"""
文件读取
"""

# 打开文件
# open(name, mode, edcoding) 文件名（包括路径，读取模式，编码方式）
# mode有3种模式，r-只读方式打开，指针放置开头，此为默认模式
# w-打开文件只用于写入，若该文件已存在则打开晚间，并从头开始编辑，原内容将被删除；若不存在，则创建新文件
# a-打开文件用于追加，若文件已存在，新内容将写入已有内容后，若此文件不存在，则创建新文件写入
f = open('D:\Python protest\学习笔记\文件操作\测试.txt', 'r', encoding='UTF-8')
print(type(f))
"""
# 读取文件
# .read(num), num表示读取字节长度，默认全读
print(f'读取10个字节的结果：{f.read(10)}')
# 第二次读取记录上次读取的位置，从该位置开始读取
print(f'读取全部内容的结果：{f.read()}')
print('--------------------------------')
"""

"""
# .readlines(),按行的方式一次性读取，且返回一个列表。其中每一行的数据为一个元素
lines = f.readlines()
print(f'lines对象的类型：{type(lines)}')
print(f'lines对象的内容是:{lines}')
"""

"""
# .readline(),按行读取内容
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f'第一行数据是:{line1}')
print(f'第二行数据是:{line2}')
print(f'第三行数据是:{line3}')
"""

"""
# for循环读取文件行
for line in f:
    print(f'每一行数据是:{line}')
"""

# 文件的关闭
# .close()
f.close()

# with open 语法操作文件,操作完成后自动关闭文件
with open('D:\Python protest\学习笔记\文件操作\测试.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(f'每一行数据是:{line}')





