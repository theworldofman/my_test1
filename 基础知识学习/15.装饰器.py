# 装饰器:装饰器是一种也输的函数,用来修改其他对象的行为,可以用来扩展和增强原有的功能,而不修改原始函数的代码
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()
#写法:@装饰器函数
# def 函数
# 在我们使用时,会执行装饰器函数,而在装饰器函数内会包含def定义的函数
# 装饰器函数怎么写
# def 装饰器函数名(参数一般是函数):
#     def x():
#          编写自己添加的函数,其中要包含func,可以扩展
#     return x

# 如果修饰的函数有参数,此时我们的修饰函数会报错,此时我们要添加*args, **kwargs不定参数
# 也就是改成x(*args, **kwargs),此时不管修饰的函数有多少参数,我们都可以实现装饰,注意func(*args, **kwargs)

# 如果有返回值,我们要在x函数内部也返回该值,因为我们本质上执行的就是x函数