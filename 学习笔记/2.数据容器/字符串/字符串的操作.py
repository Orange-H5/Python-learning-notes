
# 字符串下标索引取值
my_str = "itheima and itcast"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，值是{value},取下标为-16的元素，值是：{value2}")

# index方法.index
value = my_str.index('and')
print(f"在字符串{my_str}中查找and，其起始下标是：{value}")

# replace方法——字符串的替换.replace()
"""replace(字符串1，字符串2)
将字符串的全部：字符串1，替换为字符串2
ps：不是修改字符串本身，而是得到了一个新的字符串
"""
new_my_str = my_str.replace('it', '程序')
print(f"将字符串{my_str},进行替换后得到：{new_my_str}")

# split方法——字符串的分割.split()
# 按指定的分隔符，将字符串划分为多个字符串，并存入列表对象中
# ps：字符串本身不变，而是得到了一个新的列表对象
my_str = "hello itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split分割后得到：{my_str_list},类型是{type(my_str_list)}")

# 字符串的规整操作——去前后空格.strip()
my_str = "  hello itheima itcast  "
new_my_str = my_str.strip()
print(f"字符串{my_str}被strip后，结果：{new_my_str}")

my_str = "12hello itheima itcast21"
new_my_str =my_str.strip('12')
print(f"字符串{my_str}被strip('12')后，结果：{new_my_str}")

# 统计字符串中某字符串出现的次数.count()
my_str = "hello itheima itcast"
count = my_str.count('it')
print(f"字符串{my_str}中it出现的次数是{count}")

# 统计字符串的长度.len()
num = len(my_str)
print(f"字符串{my_str}的长度为{num}")