import random
# n=int(input("请输入数字"))
#
# print(f"{n}在10到20之间",n>=10 and n<=20)

# and是与的意思表示二者同时对才对
# or是或的意思二对一就行
# not是非取反的意思

# if语法先判断,执行下面缩进的语句
# if n>=20:
#     print(n)
# else:
#     print(n+2)
# if    :
#
# elif   :可重复
#
# else:


# n=int(input("请输入考试成绩:"))
# if n>=85:
#     print("成绩优异")
# elif n>=60:
#     print("成绩及格")
# else:
#     print("成绩不及格")

# match...case匹配模式
# day=int(input())
# match day:
#     case 1:
#         print(day)
#     case 2:
#         print(day)
#     case _:#适用于没匹配的其他情况
#         print(day)

# while循环也是执行下面缩进的部分
# 可加else执行循环结束后的语句

# for循环结构
# msg=input("enter your message")
# for i in msg(数据集):
#     print(i)
# 与c语言不一样遍历的是msg里,关注每一个元素,while循环次数未知

# for循环常用range语句,生成指定数字序列
# range(end)生成从0到end,不包含end
#range(start,end)从start开始到end结束不包含end
#range(start,end,step)从start开始间隔step生成到end不包含end

# a=0
# for i in range(101):
#     a=a+i
# print(a)#自带换行效果
#
# print("o",end="")
# print("o",end="")
# end表示以什么结束默认是\n

# 打印九九乘法表
# for i in range(10):
#     for j in range(1,i+1 ):
#         print(f"{j}*{i}=",i*j,end=" ")
#     print()

# break结束循环,continue直接进入下一次循环

# random_num = random.randint(1, 100)
# while True:
#     num =int(input("请猜测一个数字:"))
#     if num==random_num:
#         print(f"恭喜你猜对了,数字就是{num}")
#         break
#     elif num>random_num:
#         print("数字大了")
#         continue
#     elif num<random_num:
#         print("数字小了")
#         continue

# msg =input("")
# m =0
# n =0
# for i in msg:
#     if i == "a":
#         n +=1
#         continue
#     if i == "k":
#         m +=1
#         continue
# print(m)
# print(n)

























