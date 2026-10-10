#(#在python里是注释的意思)
# ctrl+/可以快速注释

print('hello world')
print('hello world')
# 在不同行不需要;换行符自动区分句子
print('hello world');print('你哈')
# 在同一行需要;隔开语句

print(True+1) #结果是2
print("True+1")#结果是True+1

# 变量定义不用定义变量类型,动态类型语言,及一个变量可以接受不同类型的值,例如
# num = 1
num = "OK"
jk,dk=10,2.3
# print(num)
# print输出变量时要分段,用逗号隔开,ctrl+d复制上一行
print("num的含义是",num)
# 标识符:为变量取得名字

# type函数可以查询数据类型
# print(type(num))
# print(type(1))

# isinstance()检查数据是不是给定类型,第一项是数据第二项是类型,是输出true
# print(isinstance(num,str))
# print(isinstance(num,int))
# print(isinstance(num,float))

# 字符串定义三种
s1 = 'Hello'
s2 = "Hello"
s3 = """hhhh
 hhh
h  h""" #三引号可以换行(多行字符串)
print(s1+s2)
print(s1,s2)
print(s2)
print(s3)
# 转义字符\+' "可以输出' ",\n换行.\t制表
msg = '\''