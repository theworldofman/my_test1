# 面向过程是按步骤一步一步来适用于简单的代码
# 面向对象是以对象为基本单元,把数据(属性)和功能(方法)打包,关注点在对象帮我做这件事

# 类是对象的模板,对象是类的实例.对象是由类创造出来的

#类名命名用大驼峰命名法,用大写分割不同单词

# 定义类(类似于结构体但是可以动态给属性,但是不推荐动态提供属性,不便于维护)
# class 类名:
#      pass
# 创建对象
# 对象名 = 类名()
# 对象名.属性名1 = 属性值1
# 对象名.属性名2 = 属性值2

# 第一种定义方法
# class Car:
#     pass
# c1 = Car()
# c1.name = 'BMW'
# c1.price = 100000
# print(c1.__dict__)
# __dict__是自定义特殊属性,是以字典类型存储所有属性

# 第二种定义方法
# class 类名:
#       def __init__(self,参数列表):   注意self参数必须放在第一个,表示当前创建的实例对象,__init__初始化方法,对象创建后自动调用,用于设置初始状态`
#            self.属性名 = 参数值
#            self.属性名 = 参数值
# 注意这里def实际上就是函数定义,def在类外面定义就是函数,在类里面定义就是方法

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         print('属性赋值完毕')
#
# c1 = Car('BMW','X1','2000')
# print(c1.__dict__)

# 实例方法
# class 类名:
#      def __init__(self,形参列表):
#         self.属性名 = 参数值(公式)
#         ...........
#
# (实例方法,实际上就是函数,但是有self本生,就是可以不用再次传参就可以使用类里面的值了)
#      def 方法名(self,形参列表):(没有self就没办法操作属性)
#           .....

# 下面使用方法时候类似于函数


class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def running(self):
        print(f'{self.brand}正在高速行驶')

    def __str__(self):
        return f"{self.brand}"

    def __eq__(self,other):
        return self.brand == other.brand

    def __lt__(self,other):
        return self.price < other.price

c1 = Car('BMW','X1',133333)
c1.running()


# 魔法方法是指以双下划线开头,结尾的特殊方法,用于雷达特殊行为
# 魔法方法不用手动调用,py会在合适时机自动调用

# 1.__init__ ----------初始化方法
# 2.__str__ -----------字符串表示方法
# 3.__eq__ ------------比较两个对象是否相等(equal缩写)
# 4.__lt__,__le__,__gt__,__ge__----------判断大小(less than 小于,le 小于等于,gt 大于,ge 大于等于)

# __init__使用主要是初始化

c2 = Car('BMW','X1',133333)
# print(c2)       结果是地址
# print(c1==c2)   结果是False
# print(c1 < c2)  比较不了
# 这时候就用到了魔法方法,我们不需要调用,用到相关的py会自动调用,相当于我们为"==","<","对象表现形式"赋予了特定内容

# print(c2)         结果是我们定义的brand
# print(c1==c2)     结果是TRUE
# print(c1 < c2)    结果是FALSE,大于小于定义一个就行


# 属性分为:1.实例属性:是属于具体的对象,每个对象是独立的,调用时  实例对象(self就行).属性, 定义在__init__方法里
#         2.类属性 :类属性是属于类本身的属性,所有实例共享  定义是不在  __init__ 里的,通过 类名.属性操作
# 说明,通过实例查找属性时,会先查找实例属性,实例属性不存在时,再查找类属性

