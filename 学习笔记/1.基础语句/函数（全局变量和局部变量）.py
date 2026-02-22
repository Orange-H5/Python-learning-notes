
# 定义全局变量
num = 200

def check_a():
    print(f"check_a:{num}")

def check_b():
    print(f"check_b:{num}")

check_a()
check_b()
print(num)


# 全局变量不受局部影响
# 局部变量只作用于局部区域

num_1 = 200

def check_1():
    print(f"check_1:{num}")

def check_2():
    num = 100
    print(f"check_2:{num}")

check_1()
check_2()
print(num_1)


# global关键字，在函数内声明变量为全局变量

num_2 = 200

def check_3():
    print(f"check_3:{num_2}")

def check_4():
     global num_2   #设置内部定义的变量为全局变量
     num_2 = 500
     print(f"check_4:{num_2}")

check_3()
check_4()
print(num_2)