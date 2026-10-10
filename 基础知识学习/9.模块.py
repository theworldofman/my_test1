
#模块类似于c语言里的库
# 导入后可以使用对应功能
# 导入模块方法
# 这里的功能可以时函数,方法,类等
# (1)导入整个模块
#1. import 模块名  调用其中函数时方法: 模块名.功能名
#2. import 模块名 as 别名(以后调用方法就可以用简化后的别名)   调用方法: 别名.功能名
# (2)只导入一些功能
#1. from 模块名 import 功能名 调用时候直接功能: 功能名
#2. from 模块名 import 功能名 as 别名 调用: 别名
#3. from 模块名 import * (调用所有功能)  调用方式:  功能名

# import random
# for i in range(100):
#     print(random.randint(1,100))

# from random import randint as rnd
#
# for i in range(100):
#     print(rnd(1, 100))


# 自定义模块
# 定义常量时全大写(但是还是可以改变值)
# 重复输出 print (' '*重复数量)

#引用导入模块的值
# import 01.my_fun
#
# print(01.my_fun.PI)
# 01.my_fun.outline()

# __all__指定from ...import * 导入的是哪些功能
#__all__ = ['功能名','常量名'....]

# 软件包本质就是一个文件夹,该文件夹可以包含多个py模块,文件夹下还包含一个__init__.py
# 包->模块->功能,导入时层层递进,一层一层调

# 这里的功能可以时函数,方法,类等
# (1)导入整个模块
#1. import 包名.模块名  调用其中函数时方法: 包名.模块名.功能名
#2. from 包名 import 模块名 调用时模块名.功能名
#3. from 包名 import *  (导入包里所有模块)调用时直接模块.功能名(注意若要用导入所有模块要在__init__文件里面定义__all__=[])
# (2)只导入一些功能
#1. from 包名.模块名 import 功能名 调用时候直接功能: 功能名
#2. from 包名.模块名 import * (调用所有功能)  调用方式:  功能名


# import modul1.my_test1
# print(modul1.my_test1.func1(1,2))

# from modul1.my_test1 import *
# print(func1(1,4))



