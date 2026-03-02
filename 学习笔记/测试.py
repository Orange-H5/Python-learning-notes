"""
用于临时调试代码
"""
# 用eval方法将输入的字符串格式的字典转为真实的字典
dict1 = eval(input())
dict2 = eval(input())
# 遍历其中的一个字典
for k, v in dict1.items():
    # 若dict1和dict2中存在相同key，则累加v,并删去dict2中的该key
    if k in dict2:
        dict1[k] += dict2[k]
        dict2.pop(k)
# 上述循环做完后，dict1中与dict2中key相同的值已经进行累加
# 将dict2中独有的键值对存入dict1
for k, v in dict2.items():
    dict1[k] = v
# 此时对dict1的键进行排序（ascii表值正序）就可得出答案
# 创建空字典存入所有键值对（ascii转换后）
dict1_result = {}
# 创建空字典来建立转换ascii后的key1与原始key的对应关系
dict1_key_counterpart = {}
for key, value in dict1.items():
    # 若key是字符串形式
    if isinstance(key, str):
        # 将该单个字符转为ascii码值，并存入dict1_result
        # key——>key1
        key1 = ord(key)
        dict1_result[key1] = value
        # 建立此时key1与key的对应关系，便于后续还原键
        dict1_key_counterpart[key1] = key
    else:
        # 同上
        dict1_result[key] = value
        dict1_key_counterpart[key] = key
# 对存入所有键值对（转换后）的dict1_result进行键的排序
# 得到key_sort——键（转换后，正序）的列表
key_sort = sorted(dict1_result)
# 创建空字典，存入最终结果
dict_result = {}
# 遍历排好序的转换后的键列表
for key2 in key_sort:
    # 将转换的key2对应到原始的key3值——通过之前的对应字典联系
    # 还原字典的键（正序）——ascii码值——>字符串
    key3 = dict1_key_counterpart[key2]
    # 将此时的key3对应的原始value存入结果列表
    dict_result[key3] = dict1_result[key2]
# 输出结果
print(dict_result)







































