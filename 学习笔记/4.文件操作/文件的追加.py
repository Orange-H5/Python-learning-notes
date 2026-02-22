"""
文件的追加写入
"""

"""
# 打开文件，不存在的文件
f = open("D:\Python protest\学习笔记\文件操作\追加操作测试.txt", "a", encoding='UTF-8')
# write写入
f.write('黑马程序员')
# flush刷新
f.flush()
# close关闭
f.close()
"""

# 打开一个已存在的文件
f = open("D:\Python protest\学习笔记\文件操作\追加操作测试.txt", "a", encoding='UTF-8')
# write写入，flush刷新
f.write('\n我要学好python')
# close关闭
f.close()


