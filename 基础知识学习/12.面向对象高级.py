# 封装:封装就是把属性和方法捆绑在一起形成一个独立单元(类),并隐藏内部实现细节,只对外暴露必要的功能
# 内部:私有属性,私有方法 (在前面加上两个_表示私有,表示不要从类的外部访问,这是Python的命名约定,并不是真正的私有)
# 外部:公共属性,公共方法
class Car:
    def __init__(self,owner):
        self.__owner=owner

car = Car('lhs')
# print(car.__owner 不能访问但是可以设置一个公共方法访问

# 继承:描述类与类之间的关系
# 继承类的方法,子类继承父类后,会把父类的属性和方法都继承下来,但是只能继承非私有的属性和方法
# 继承方法:class 子类名(父类名)
# 继承-重写:是指子类继承父类后如果父类的方法不满足需求,可以在子类种重新定义父类中已有的方法(方法名相同),从而实现子类替代父类的实现
# 如果子类在重写父类方法时,需要调用父类方法,可以通过父类名.方法名(self)/super().方法名()

# 在python当中一个子类可以继承多个父类(多继承)
# 语法:class 子类名(父类名1,父类名2)
# 如果多继承父类有多个init初始化方法或同名属性,那么会优先使用第一个父类的方法和属性
# 子类其实也是父类的实例

# 多态:是指同一种方法,具有不同的形式,行为,表现.
# 其实就是一种方法,传入父类汇总拍那个不同的子类有不同表现方法
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('吃')

    def drink(self):
        print('喝')
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def eat(self):
        print('吃骨头')
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def eat(self):
        print('吃鱼')
# 多态的体现：同一个方法，不同子类有不同表现
def animal_eat(animal: Animal):
    animal.eat()
dog = Dog('旺财', 2)
cat = Cat('咪咪', 3)
animal_eat(dog)  # 输出: 吃骨头
animal_eat(cat)  # 输出: 吃鱼

# mro多继承原则,当一个类继承多类时,会优先使用第一个类的同名属性或方法
# 调用父类方法
# 1.超类调用:super.方法名
# 2.直接:父类名.方法名

# 普通多态:此时要求定义函数的参数是父类类型(其实没啥用)
# 多态:鸭子类型:不看对象是什么类型（继不继承、继承几个都无所谓），只看它有没有对应的方法。

# 抽象类:是指不能被实例化的类,通常用于定义接口,让子类去实现,只能被继承,不能被直接实例化,强制子类必须遵守
# Python中的抽象类,需要继承abc中的ABC类
# 要设置抽象类只需要让他继承ABC
# @abstractmethod装饰器,用于定义抽象方法
# 父类是抽象类,子类必须实现父类的抽象方法,否则子类也是抽象类
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
class Dog(Animal):
    def eat(self):
        print('吃骨头')
class Cat(Animal):
    def eat(self):
        print('吃鱼')
dog = Dog()
dog.eat()
cat = Cat()
cat.eat()
# 抽象类的实例化





































