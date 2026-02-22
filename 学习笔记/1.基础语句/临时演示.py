
# 定义一个函数，函数名任意，要求调用后函数可以输出如下欢迎语：
# ‘加油，你一定要摆脱泥潭，走向更好的未来。’

# def workhard():
#     print('加油，你一定要摆脱泥潭，走向更好的未来。')
#
# workhard()


# 定义一个函数，判断体温值是否异常，（给定一个传入参数）
# 若体温小于等于37.5，则正常
# 若体温大于37.5，则异常，

# def tem_depend(tem):
#     if tem <= 37.5:
#         print(f'您的体温是{tem}°，体温正常请进。')
#     else:
#         print(f'您的提问是{tem}°，需要隔离')
# tem_depend(39)


# 定义函数返回值的语法格式(ps:函数体内遇到return，后续函数体内部代码均不执行)
# 定义一个函数，完成两个数字相加的功能，通过返回值，将相加结果返回给调用者

# def add(x, y):
#     result = x+y
#     return result
#
# a = add(3, 2)
# print(a)


# 函数综合案例，ATM取款
# def menu(name):
#     print('---主菜单---')
#     print(f'{name},您好，欢迎来到工商银行，请选择操作：')
#     print('查询余额\t[输入1]')        # 通过\t制表符，对齐输出
#     print('存款\t\t[输入2]')
#     print('取款\t\t[输入3]')
#     print('推出\t\t[输入4]')
#     global x
#     x = int(input('请输入您的选择：'))
#     print()
#
# def account(name):
#     print('---查询余额---')
#     global money
#     print(f'{name}，您好，您的余额剩余：{money}元')
#     print()
#
# def put_money(name):
#     print('---存款---')
#     money_in = int(input('请输入存款金额'))
#     print()
#
#     print('---存款---')
#     print(f'{name},您好，您存款{money_in}元成功')
#     global money
#     money += money_in
#     print(f'{name}，您好，您的余额剩余：{money}元')
#     print()
#
# def out_money(name):
#     global money
#     print('---取款---')
#     money_out = int(input('请输入取款金额'))
#     print()
#
#     if money_out <= money:
#         print('---取款---')
#         print(f'{name},您好，您取款{money_out}元成功')
#         money -= money_out
#         print(f'{name}，您好，您的余额剩余：{money}元')
#         print()
#     else:
#         print('取款金额超过所剩余额，请重新取款！')
#         print()
#
#
# money = 5000000
# name = input('请输入姓名：')
# x = 0
# while True:
#     menu(name)
#     if x == 1:
#         account(name)
#     elif x == 2:
#         put_money(name)
#     elif x == 3:
#         out_money(name)
#     else:
#         break

"""
2.数据容器：list列表
"""
"""
# 定义一个列表list
list1 = ['hcj', 666, True]
print(list1)
print(type(list1))
# 定义一个空列表
list2 = []
list3 = list()
print(list2)
print(list3)

# 定义一个嵌套列表
list4 = [['hcj', 666, True], [1, 2, 3]]

# 通过下标索引取出对应位置的数据
# 列表正序：[0 1 2 3 .....]
# 列表倒序：[.... -3 -2 -1]

a = list1[0]    # 取出list1中第一个元素：’hcj‘
b = list1[1]    # 取出list1中第二个元素：666
c = list1[-1]   # 取出list1中倒数一个元素：True
print('%s,%d,%d' % (a, b, c))

d = list4[0][2]     # 取出list4中第1个元素中的第3个元素:True
print(d)
"""
"""
list的常用操作
"""

"""
def B():
    for i in range(1, 1+10**17):
        A = i%2==1 and i%3==2 and i%4==1 and i%5==4
        B = i%6==5 and i%7==4 and i%8==1 and i%9==2
        C = i%10==9 and i%11==0 and i%12==5 and i%13==10
        D = i%14==11 and i%15==14 and i%16==9 and i%17==0
        E = i%18==11 and i%19==18 and i%20==9 and i%21==11
        F = i%22==11 and i%23==15 and i%24==17 and i%25==9
        G = i%26==23 and i%27==20 and i%28==25 and i%29==16
        H = i%30==29 and i%31==27 and i%32==25 and i%33==11
        I = i%34==17 and i%35==4 and i%36==29 and i%37==22
        J = i%38==37 and i%39==23 and i%40==9 and i%41==1
        K = i%42==11 and i%43==11 and i%44==33 and i%45==29
        L = i%46==15 and i%47==5 and i%48==41 and i%49==46

        if A and B and C and D and E and F and G and H and I and J and K and L:
            break
    print(i)

B()

"""

"""
# 1.对list进行切片，从1开始，4结束，步长为1
list1 = [0, 1, 2, 3, 4, 5, 6]
list1_1 = list1[1:4]    # 步长默认是1，省略不写
print(f'结果是：{list1_1}')

# 2.对tuple进行切片，从头开始，到最后结束，步长为1
tuple1 = (0, 1, 2, 3, 4, 5, 6)
tuple1_1 = tuple1[:]     # 起始和结束不写表示从头到尾，步长为1可以省略
print(f'结果是：{tuple1_1}')

# 3.对str进行切片，从头开始，到最后结束，步长为2
str1 = '01234567'
str1_1 = str1[::2]  # 从头到尾省略不写，步长为2
print(f'结果是：{str1_1}')

# 4.对str进行切片，从头开始，到最后结束，步长为-1
str2 = '01234567'
str2_2 = str2[::-1]     # 从头到尾，逆序取出——反转序列
print(f'结果是：{str2_2}')

# 5.对列表进行切片，从3开始，到1结束，步长-1
list2 = [0, 1, 2, 3, 4, 5, 6]
list2_2 = list2[3:1:-1] # 从3—1逆序取出
print(f'结果是：{list2_2}')

# 6.对元组进行切片，从头开始，到尾结束，步长-2
tuple2 = (0, 1, 2, 3, 4, 5, 6)
tuple2_2 = tuple2[::-2]
print(f'结果是：{tuple2_2}')

"""

"""

N = int(input())
# 先遍历2——N-1,并找出所有素数
list_primes = []
for num in range(2,(N//2)+1):
    isprimes = True
    # 先判断端点的特殊情况
    if num == 2:
        isprimes = True
    else:
        for i in range(2,num):
            if num%i == 0:
                isprimes = False
                break
        # 若遍历的num为素数，则进一步判断N-num是否为素数
    if isprimes:
        num2 = N-num
        if num2 == 1:
            isprimes = False
        else:
            if num2 == 2:
                isprimes = True
            else:
                for i in range(2,num2):
                    if num2%i==0:
                        isprimes = False
                        break
                # 若num2也为素数，则即为所求
            if isprimes:
                print(f'{N} = {min(num,num2)} + {max(num,num2)}')
                break

"""
"""

# 46
N = int(input())
# 另一种接收方式
# grade = input().split(' ')——元素为字符串的列表
list_grade = list(map(int,input().split()))
# 处理平均成绩和判断及格人数
# 特别注意！！！！
# 不要忘记处理N==0的情况，要不然grade_avg会出现非0返回
if N ==0:
    grade_avg = 0
    grade_passed =0
else:
    grade_avg = sum(list_grade[0:len])/N
    # 判断及格人数
    grade_passed = 0
    for grade in list_grade[0:N]:
        if grade >= 60:
            grade_passed += 1
print(f'average = {grade_avg:.1f}')
print(f'count = {grade_passed}')

"""
"""
N = int(input())
list_grade = input().split(' ')
if N == 0 or list_grade==[]:
    grade_avg = 0
    count = 0
else:
    list_grade_int = list()
    for grade in list_grade[0:N]:
        list_grade_int.append(int(grade))
    grade_avg = sum(list_grade_int)/N
    count = 0
    for i in list_grade_int:
        if i >=60:
            count +=1
print(f'average = {grade_avg:.1f}')
print(f'count = {count}')

"""
# 用num（集合形式）记录输入的数据
num = set(map(int,input().split(',')))
set2 = {6,7,8,9,10}
# 取set2中有，但num中没有的元素——取差集
# 即第二小队中没有的票的队员
# 另一种写法 set2_no_vote = set2-num
set2_no_vote = set2.difference(num)
result = ' '.join(map(str, sorted(set2_no_vote)))
print(result)