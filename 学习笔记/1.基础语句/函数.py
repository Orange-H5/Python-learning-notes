

# 无return语句的函数返回值
def say_hi():
    print("你好")

result = say_hi()
print(f"无返回值的函数，返回内容是：{result}")
print(f"无返回值的函数，返回类型是{type(result)}")

# 另一种写法
def say_hi():
    print("你好")
    return None


# 函数的说明文档写法
def add(x,y):
    """
    add函数可以接收2个参数，进行2数相加的功能
    :param x:表示相加的其中一个数字
    :param y:表示相加的另一数字
    :return:返回值是2数相加的结果
    """
    result = x + y
    print(f"2数相加的结果是：{result}")
    return result

b = add(5,6)
print(b)


# 函数的嵌套调用

