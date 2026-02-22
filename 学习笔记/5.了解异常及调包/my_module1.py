
# 模块文件引用__all__列表对象，外部通过from xx import * 时，只能引用列表中的函数
__all__=['test2']


def test(a,b):
    print(a+b)

def test2(a,b):
    print(a-b)



# 模块内部测试函数，调用时将不输出
if __name__ == '__main__':
    test(1, 2)





