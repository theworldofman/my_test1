# Lambda表达式
#只有一行代码的函数可以写成Lambda表达式
# lambda 输入值:函数体
# 当然输入更多参数也可以\
# 返回值是函数体的计算结果
# map(function, iterable, ...)
# function：要应用的函数，可以是内置函数、自定义函数、lambda 等。
# iterable：一个或多个可迭代对象，如列表、元组、字符串等。
# 返回值：Python 3 中返回 map 迭代器，不是列表。
# 当传入多个可迭代对象时，map() 会并行取每个对象的元素，传给函数。
# a = [1, 2, 3]
# b = [10, 20, 30]
# result = map(lambda x, y: x + y, a, b)
# print(list(result))  # [11, 22, 33]
# 当然这里强制转换