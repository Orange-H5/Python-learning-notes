
mylist = ['itcast', 'itheima', 'python']

# 查找某元素在列表内的索引值——.index
index = mylist.index("itheima")
print(f"列表中'itheima'的下标为{index}")

# 如果被查找的元素不存在，则会报错
# index2 = mylist.index("hello")
# print(f"列表中‘hello'的下标为{index2}")

# 修改特定下标索引的值
mylist[0] = 'hello'
print(f"列表被修改元素后的结果是：{mylist}")

# 在指定下标位置插入新元素（后续元素整体后移1位）.insert
mylist.insert(1,'best')
print(f"列表插入新元素后的结果是：{mylist}")

# 在列表尾部追加“单个”新元素.append
mylist.append('我爱你')
print(f"追加元素后的列表结果为：{mylist}")

# 在列表尾部追加一批元素.extend
mylist2 = [1, 2 ,3]
mylist.extend(mylist2)
print(f"列表在追加了新的一批元素后结果是：{mylist}")

# 删除指定下标索引的元素（2种方法）del .pop(取出返回）
del mylist[2]
print(f"列表删除元素后的结果是：{mylist}")

element = mylist.pop(0)
print(f"通过pop方法取出元素后列表内容为：{mylist}，取出的元素是{element}")

# 删除某元素在列表中的第一个匹配项.remove
mylist = ['itcast', 'itheima', 'itcast', 'itheima', 'python']
mylist.remove('itheima')
print(f"通过remove方法移除元素后，列表的结果是：{mylist}")

# 清空列表.clear
mylist.clear()
print(f"列表被清空了，结果是：{mylist}")

# 统计某元素在列表中的数量
mylist = ['itcast', 'itheima', 'itcast', 'itheima', 'python']
count = mylist.count('itheima')
print(f"列表中itheima的数量是{count}")

# 统计列表元素总个数
mylist = ['itcast', 'itheima', 'itcast', 'itheima', 'python']
count1 = len(mylist)
print(f"列表的元素数量共有{count1}个")
