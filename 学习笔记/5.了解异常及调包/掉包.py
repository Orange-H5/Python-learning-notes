"""
演示python的包
"""

# 导入自定义包中的模块,并使用
import my_package.my_module1
import my_package.my_module2


my_package.my_module1.info_print1()
my_package.my_module2.info_print2()

# 此引用无需写包名
from my_package import my_module1
from my_package import my_module2

my_module1.info_print1()
my_module2.info_print2()

# 引用包中模块的具体功能
from my_package.my_module1 import info_print1
info_print1()




