

def user_info(name, age, gender):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")

# 位置参数 ——默认形式，按位排序传入
user_info('小明', 20, '男')

# 关键字参数
user_info(name='小王', age=11, gender='男')
user_info(age=11, name='小王', gender='男')
user_info('小王', gender='男', age=11)

# 缺省参数（默认参数）(默认参数必须放在最后）
def user_info(name, age, gender='男'):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")

user_info('小天', 13)
user_info('小天', 13, gender='女')

'''
# 错误写法(默认参数未放置最后)
def user_info(name, age=11, gender):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")
'''

# 不定长参数（可变参数）

# 不定长-位置不定长，*
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)},内容是：{args}")

user_info(1, 2, 3, '小明', '男孩')


# 不定长-关键字不定长，**
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)},内容是：{kwargs}")

user_info(name='小王', age=11, gender='男孩', addr='北京')
