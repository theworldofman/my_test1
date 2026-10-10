# dict字典用来存储键值对类型的,每个键存储一个值,可以通过键(key)来快速查找对应的值(value)
# 特点:键值对存储,键(不可以重复),可以修改

# 定义 字典名称 = {key:value,key:value,key:value}
# 定义空字典 名称={}\dict()
# dict1={"王玲":777,"咯i就":999}
# 注意字典中的value可以是任何类型的数据也可以是字典,而key不能为可变类型(可变类型例如list,set,dict不可以)int,元组,字符串可以
# key不能重复如果重复后面的会覆盖前面的值
# dict2 = {1:22,1.2:11,'李恒鑫':(1,11),"A":1.2,(1,2):24}
# 字典名字[key]可以获得key的value值,字典无下表
# print(dict2["李恒鑫"])
# dict2["李恒鑫"]="大帅哥"
# print(dict2)

# 添加 字典名称[key] = value,key不存在直接添加,存在则进行修改操作

# 删除pop 字典名称.pop(key)删除key并且返回对应的value/del 字典名称[key]直接删除

# 查询1.a = 字典名称[key] 2.a = 字典名称.get(key) 3.直接获取所有key 字典名称.keys() 4.直接获取所有value 字典名称.values() 5.直接获取所有键值对 字典名称.items()
# print(dict2.keys())
# print(dict2.values())
# print(dict2.items())

# 遍历时字典的元素键值对(字典名称.items()形式)可以用单个元组接受

# 购物车菜单系统
# print("#########################")
# print('     1.添加购物车         ')
# print('     2.修改购物车         ')
# print('     3.删除购物车         ')
# print('     4.查询购物车         ')
# print('     5.退出购物车         ')
# print("#########################")
# shop={}
# a=int(input('请输入想要的操作'))
# while a!=5:
#     if a==1:
#         key=input('请输入想要的物品')
#         if key in shop:
#             print('该商品已经存在请重新选择')
#         else:
#             good_price = float(input('商品价格'))
#             good_num = int(input('商品数量'))
#             shop[key]={"good_price":good_price,"good_num":good_num}
#             print('添加完毕')
#     elif a==2:
#         key = input('请输入想要的物品')
#         if key not in shop:
#             print('该商品不经存在请重新选择')
#         else:
#             good_price = float(input('商品价格'))
#             good_num = int(input('商品数量'))
#             shop[key] = {"good_price": good_price, "good_num": good_num}
#             print('修改完毕')
#
#     elif a==3:
#         key = input('请输入想要的物品')
#         if key not in shop:
#             print('该商品不存在请重新选择')
#         else:
#             del shop[key]
#             print('删除完毕')
#
#     elif a==4:
#         for key in shop:
#             print(f'商品名称{key},商品价格{shop[key]['good_price']},商品数量{shop[key]['good_num']}')
#     else:
#         print("不合理")
#
#
#     a = int(input('请输入想要的操作'))
# print('感谢使用')
#
#
#












