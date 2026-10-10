# 集合set不能储存重复元素,特点:无序(不可索引,不可以切片),不可重复,可修改
# 定义集合{}
# !!空集合定义 s2=set(),不能={}

s1 = {1,2,3,1,3,4}
s2 = {1,5,6,3}
# print(s1)

#add添加元素
s1.add(5)
print(s1)

# remove移除
s1.remove(5)
print(s1)

# pop随机移除元素并且返回
# a = s1.pop()
# print(a)

# clear清除集合
# s1.clear()
# print(s1)

# difference求差集,在第一个集合存在,在第二个集合不存在
# 也可以用运算符-求差集
# 集合推导式{往集合中添加的元素 for循环 if 条件}
print(s1.difference(s2))

# union求并集
# 并集运算符|
print(s1.union(s2))

# intersection求交集
# 也可以用运算符&实现交集
print(s1.intersection(s2))

# set,tuple,list,str集合也可以*解包成列表

# for循环遍历集合顺序不固定
