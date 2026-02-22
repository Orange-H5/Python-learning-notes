"""
演示自定义模块
"""
"""
# 导入自定义模块
import my_module1
my_module1.test(1,2)


# 导入不同模块的同名功能
# 最新导入的覆盖先前的
from my_module1 import test
from my_module2 import test

test(1,2)

"""

from my_module1 import test