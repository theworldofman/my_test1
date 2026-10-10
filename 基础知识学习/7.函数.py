# 函数是组织好的,可以重复使用,用来实现特定功能的代码片段
# 函数的定义与调用
# def 函数名(参数列表(多个参数时用','分隔开)):
#     函数体
#     return 返回值(若有多个返回值用','分隔,多个返回值分装到元组之中)

# 调用函数
# 函数名(参数)

# 函数先定义后调用,定义时候函数不执行,调用时才执行,先定义后调用.
# round(前面是四舍五入对象,逗号后面是目标精度)

# 函数说明文档写在函数开头用三引号包裹起来,用于解释函数的功能,参数和返回值的信息
def rectangle_aera(l,w):
    '''
    求长方形面积
    :param l: 长
    :param w: 宽
    :return: 面积
    '''
    return l*w
rectangle_aera(3,5)

#函数调用以栈形式进行
def triangle_area(a,b):
    """
    求出三角形面积
    :param a: 底
    :param b: 高
    :return:三角形面积
    """
    return round(a*b/2,2)

def count_aeiou(s):
    """
    求出字符串里元音字母数量
    :param s: 字符串
    :return: 元音字母数量
    """
    num=0
    for c in s:
        if c in "aeiou":
            num+=1
    return num

def calc_score(list1):
    """
    求出最大最小平均
    :param list1:
    :return:
    """
    max_score=max(list1)
    min_score=min(list1)
    avg_score=round(sum(list1)/len(list1),1)
    return max_score,min_score,avg_score

score=[12,32,11,423,2322,55,63]
print(calc_score(score))

# 全局便量在函数外定义的变量叫做全局变量,在整个文件内都可以访问(通常定义在文件顶部)
# 局部变量只能在函数内有效

num2=100

def num1():
#num2在函数中定义时就已经把他看成局部变量了,所以不能有类似于
#num2=num2+1操作
    print(num2)
num1()
print(num2)

# global可以在函数内部修改全局变量值

def num3():
    global num2
    num2+=1
    print(num2)
num3()
print(num2)

# 函数传参方式
# 1.位置传参.调用函数时根据定义函数的位置来传递参数 要求:调用函数时参数顺序于定义函数时参数顺序完全一致
# 2.关键字传参:调用函数时以定义时形参为关键字传参,以"键=值"的形式传递(不要求顺序)
# 上述二者可以一起使用(位置在前,关键字在后)

# 默认参数(缺省参数)用于定义函数时,为参数提供默认值,调用函数时可以不传递有默认值的参数,没指定用默认,指定了用指定的

def tongji(name,age,city='beijing'):
    print(name,age,city)
tongji('lhx',19)
tongji(age=20,name='wf',city='hangzhou')

# 不定长参数(可变参数)用于函数定义及调用时参数个数不确定的场景
# 基于位置参数的不定长
# def calc(*args):(注意这里args只是约定俗成的变量名,并不是关键字)
# calc(a,d,c)此时arge是元组封装a,d,c当然也可以传单个元组 函数名((元组))

def calcj(*args):
    print(args)
calcj(1,23,45,6)

# 不定长参数关键字传递(**kwargs)()kwarges约定俗成
# 最终会封装到字典类型

# def jjj(*args,**kwargs):
#     print(args)
#     for abc,abd in kwargs.items():
#         print(abc,abd,end='#')
# print(kwargs)

# jjj(1,2,3,4,roundw=1,wd=2)
# 后面俩是关键字不定长,此时后俩变到一个字典当中这里关键字可以随意写

# 函数的参数类型
# 1.普通参数:数字,布尔,字符串,列表,元组,集合,字典等
# 2.特殊类型:函数 可以调用别的函数,用于使用函数不定的情况

def hhh(x,y,oper):
    print(oper(x,y))

def add(x,y):
    return x+y

hhh(1,2,add)

# 匿名函数 lambda声明简单函数(单行表达式)
# lambda 参数列表 : 函数体(只可以在一行),它会自动return
# 因为没有名字没办法调用,所以调用要把他赋值给一个变量,此时这个变量就是个函数,相当于命名了(意义在哪?)

add1 = lambda x,y:x+y
print(add1(1,2))

# 匿名函数打印分割线
outline = lambda :print("---------------------")
outline()

# 匿名函数典型应用场景,作为高阶函数的参数
data_list = ['as','dsd','fasas','a','a##']
data_list.sort()
print(data_list)
data_list.sort(key= lambda item: len(item))
print(data_list)



def Factorial(x):
    if x==1:
        return 1
    else:
        return x*Factorial(x-1)
a = Factorial(3)
print(a)

