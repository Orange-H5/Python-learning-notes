
# 使用while循环来遍历列表
def list_while_func():
    """
    使用while循环来遍历list列表
    通过循环控制下标索引
    每次循环下标索引变量+1
    循环条件：下标索引变量 < 列表元素数量
    :return: None
    """
    list1 = ['爱', '一', '个', '人']
    i = 0
    while i < len(list1):
        element = list1[i]
        print(f"列表的元素值：{element}")
        i += 1
    return

# 使用for循环遍历
def list_for_func():
    """
    使用for循环遍历列表
    直接利用临时变量取出各个元素
    :return: None
    """
    list2 = [1, 2, 3, 4, 5]
    for element in list2:
        print(f"列表中的元素有：{element}")
    return


