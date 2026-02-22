
# 新增元素, 字典[key] = value
my_dict ={'周杰伦': 99, '林俊杰': 88, '张学友': 77}
my_dict['张信哲'] = 66
print(f"字典经过新增元素后，结果：{my_dict}")

# 更新元素
my_dict['周杰伦'] = 33
print(f"字典经过更新后，结果：{my_dict}")

# 删除元素.pop(key)  字典中同时取出并删除
score = my_dict.pop('周杰伦')
print(f"字典中被移除了一个元素，结果：{my_dict}，周杰伦的考试分数是:{score}")

# 清空元素.clear
my_dict.clear()

# 获取全部的keys（用于遍历）
my_dict ={'周杰伦': 99, '林俊杰': 88, '张学友': 77}
keys = my_dict.keys()
print(f"字典的全部keys是：{keys}")

# 遍历字典(只能用for)
# 法1：通过获取全部的keys来遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")
# 法2 直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

# 统计字典内的元素数量len()
num = len(my_dict)
print(f"字典中的元素数量有：{num}个")

