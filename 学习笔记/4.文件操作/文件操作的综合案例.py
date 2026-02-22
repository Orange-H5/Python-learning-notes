"""
需求分析：
·读取文件
·将文件写出到'bill.txt.bak'文件作为备份
·同时，将文件内标记测试的数据丢弃

实现思路：
·open和r模式打开一个文件对象，并读取文件
·open和w模式打开另一个文件对象，并用于文件写出
·for循环内容，判断是否是测试，不是测试就write写出，是测试就continue跳过
·将2个文件对象均close()
"""

# 打开bill.txt文件读入信息，创建bill.txt.bak备份文件准备写入
f1 = open(r"D:\Python protest\学习笔记\文件操作\bill.txt", 'r', encoding='UTF-8')
f2 = open(r'D:\Python protest\学习笔记\文件操作\bill.txt.bak', 'w', encoding='UTF-8')


# 循环按行读入f1文件
for lines in f1:
    # 判断是否为‘测试’
    if lines[-3:-1] == '测试':
        continue
    # 不为‘测试’，则写入到f2文件中
    else:
        f2.write(lines)

# 关闭文件
f1.close()
f2.close()










