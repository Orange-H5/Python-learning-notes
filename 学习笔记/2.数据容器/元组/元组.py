"""
元组的元素是不可修改（增加或删除元素）！！！
"""


# 定义元组tuple
t1 = (1, 'hello', True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t2的类型是：{type(t2)},内容是：{t2}")
print(f"t3的类型是：{type(t3)},内容是：{t3}")

# 定义单个元素的元组(必须加上，)
t4 = ('hello',)
print(f"t4的类型是：{type(t4)},内容是：{t4}")

# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是：{type(t5)},内容是：{t5}")

# 下标索引取出内容
num = t5[1][2]
print(f"从嵌套元组t5中取出的数据是:{num}")

# 元组的操作：index查找方法
t6 = ('a', 'b', 'c')
index = t6.index('a')
print(f"在元组t6中查找a的下标是：{index}")

# 元组的操作：count统计方法
t7 = (1, 4, 4, 4)
num = t7.count(4)
print(f"元组t7中4的数量有：{num}个")

# 元组的操作：len函数统计元组元素数量
num2 = len(t7)
print(f"元组t7中的元素数量为：{num2}个")

# 元组的遍历while
index = 0
while index < len(t7):
    print(f"元组的元素有:{t7[index]}")
    index += 1

# 元组的遍历for
for element in t7:
    print(f"元组的元素有：{element}")

# 元组内的字典元素是可修改的（list不变，list的内容可变）
t9 = (1, 2, ['itheima', 'itcast'])
print(f"t9的内容是：{t9}")
t9[2][0] = '黑马程序员'
print(f"t9的内容是：{t9}")


