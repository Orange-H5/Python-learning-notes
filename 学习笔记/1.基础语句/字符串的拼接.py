
# 字符串的拼接（加号）
print("我真的要好好学好"+"Python")
a = "Python"
print("我真的要好好学好"+a)

# 字符串的拼接只能是字符串之间的
'''hight = 180
print("我身高"+hight)   # 报错部分
'''
print("---------------")


# 字符串的格式化
# 字符串的占位（%s转换为字符串，%d转换为整数 %f转为浮点型）
num_1 = 180.69
num_2 = 18
message = "我今年%s岁，身高%s" % (num_2, num_1)
print(message)

print("---------")

message_2 = "我今年%d岁，身高%f" % (num_2, num_1)
print(message_2)

