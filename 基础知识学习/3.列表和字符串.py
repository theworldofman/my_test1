# 数据容器
# 列表(list) 字符串(str)
# 元组(tuple) 集合(set) 字典(dict)

# 列表 定义列表名称 = [元素1,元素2]
# 特点:可以储存不同类型元素,元素有序,可以重复,可以修改
#下标从0开始,从左到有正向索引从0开始,从右往左反向索引从-1开始

# list1 =[1,2,'isa',3,1,2]
# print(type(list1))
# print(list1[0],list1[2])
# list1[1]='www'
# print(list1)
# 删除操作
# del list1[1]
# print(list1)
# list1[1]="a"
# print(list1)

# 切片操作
# 序列数据[开始索引:结束索引:步长]
# 包含开始不包含结束
# print(list1[:5:2])

# 列表常用方法
# append添加元素,在最后加上
# list1.append(4)
# print(list1)

# insert,在指定索引之前添加元素
# # list1.insert(1,5)
# print(list1)

# # remove删除匹配到的第一个值
# list1.remove(1)
# print(list1)

# # pop删除列表指定索引位置的元素,未指定就删除最后一个
# a=list1.pop()
# print(a)
# print(list1)

# # sort对列表的元素进行排序,元素性质一样才可以排序
# sort可以自定义排序方法sort函数( ,key=None,reverse=False),这里key是排序方法,reverse是反转意思,可以设置为True反转
# list1[2]=10
# list1.sort()
# print(list1)

# # reverse反转列表元素
# list1.reverse()
# print(list1)

# num_list = []
#
# for i in range(10):
#     n =int(input())
#     num_list.append(n)
# num_list.sort()
# print(num_list[0])
# print(num_list[-1])
# # py语句sum函数求和sum();len()获取列表元素个数(列表元素长度)
# print(sum(num_list)/len(num_list))

# for循环可以遍历列表
# in运算符判断元素是不是在列表中,存在返回true,不存在返回false,可以用not in

# 解包操作,*可以把列表分成一个一个元素
# list1=[1,2,3]
# list2=[4,5,6]
# list3=[*list1,*list2]
# list4=list1+list2
# print(list3)
# print(list3)

# 列表推导式按照一定规则快速生成列表
# 1:[要插入的值 for循环]
# list1 = [i**2 for i in range(1,20)]
# print(list1)
# 2:[]要插入的值 for循环 if条件]
# list1 = [i for i in range(11) if i % 2 == 0]
# print(list1)

# 字符串特点:不可变性,有序行,可迭代性
# 索引也有正向和逆向,切片和列表一致
# s ="sidahj"
# print(s[6::-1])
# for i in s:
#     print(i,end=" ")


# s = "*Hello_World_Hello*"

# #find查找子串返回第一次索引位置
# a=s.find("_")
# print(a)

# #count统计子串出现次数
# b=s.count("_")
# print(b)

# # upper转大写返回
# c=s.upper()
# print(c)

# # lower转小写返回
# d=s.lower()
# print(d)

# # split按字符串按指定切割成列表
# e=s.split("_")
# print(e)

# # strip去除字符串两边特定字符或者空符
# f=s.strip('*')
# print(f)

# # replace将指定子串替换为新的字串
# g=s.replace("_","-")
# print(g)

# # startswith检查字符串是否以指定字串开头,返回布尔值
# h=s.startswith("_")
# print(h)

# male = input("Enter your male name: ")
# if '.' in male and male.count("@")==1:
#     print(f"{male} is correct")

# join 是字符串的方法，作用是：把一个「字符串列表（或任何可迭代对象）」用指定的分隔符拼接成一个字符串。
#"分隔符".join(可迭代对象)
list1 = ["Hello", "World", "Hello"]
result = " ".join(list1)
print(result)




