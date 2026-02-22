
# 定义集合(无序，不重复）
my_set = {"教育", "黑马程序员", "itheima", "教育", "黑马程序员", "itheima", "教育", "黑马程序员", "itheima"}
my_set_empty = set()
print(f"my_set的内容是:{my_set}")
print(f"my_set_empty的内容是:{my_set_empty}")

# 添加新元素
my_set.add('Python')
my_set.add('教育')
print(f"my_set添加元素后的结果是：{my_set}")

# 移除元素.remove()
my_set.remove('黑马程序员')
print(f"my_set删除元素后的结果是：{my_set}")

# 随机取出一个元素.pop()
my_set = {'教育', 'itheima', '黑马程序员'}
element = my_set.pop()
print(f"集合被取出的元素是：{element}，取出元素后：{my_set}")

# 清空集合.clear()
my_set.clear()

# 取两个集合的差集.difference()
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)    #取set1中有的而set2中没有的
print(f"取差集后结果是：{set3}")    #set1和set2保持不变

# 消除两个集合的差集.difference_update()
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)    #消除set1中与set2共有的元素，set1变，set2不变
print(f"消除差集后，set1的结果是：{set1}")

# 2个集合合并成1个集合.union()
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"合并后的结果是：{set3}")    #集合1和集合2不变

# 统计集合元素的数量len()
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
num1 = len(set1)
num2 = len(set2)
print(f"set1内的元素个数有：{num1}个")
print(f"set2内的元素个数有：{num2}个")

# 集合的遍历for (集合不支持while循环遍历)
set1 = {1, 2, 3, 4, 5}
for element in set1:
    print(element)

