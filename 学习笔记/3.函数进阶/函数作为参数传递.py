
# 定义一个函数，接收另一个函数作为传入参数
def test_func(computer):
    result = computer(1, 2)
    print(f"computer参数的类型是：{type(computer)}")
    print(f"计算结果是：{result}")

# 定义一个函数，准备作为参数传入另一个函数
def computer(x, y):
    return x+y

# 调用并传入函数
test_func(computer)
