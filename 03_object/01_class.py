"""
类的使用

# 定义一个类（类名通常用大驼峰写法）
class 类名:
    # 当一个函数被定义在类中时，它就被称为“方法”。
    # __init__方法又叫：初始化方法，它主要用来给当前实例对象添加属性。
    # __init__方法收到的参数是：当前正在创建的实例对象、其他自定义参数。
    # 当我们后期编写代码，对类进行实例化的时候，Python就会自动调用__init__方法，去完成对实例的初始化。
    def __init__(self, 参数1, 参数2, 参数3):
        # 通过self给当前实例添加属性，语法格式为：self.属性名 = 属性值
        self.属性名 = 参数1
        self.属性名 = 参数2
        self.属性名 = 参数3

1. 类名通常采用大驼峰命名法（如:Person、UserInfo）。
2. 类中所定义的函数，通常又称为方法。
3. __init__方法叫初始化方法，当我们对类进行实例化时，Python会自动调用__init__方法。
4. __init__方法的名字不能更改，否则 Python 无法自动调用。
5. __init__收到的第一个参数是当前正在创建的实例对象，形参通常用self。
6. __init__方法收到的除self以外的参数，通常用来设置实例的属性值，通过“点”语法实现：self.属性名 = 属性值
"""
from datetime import datetime

"""定义类"""
# 定义一个Person类（类名通常使用：大驼峰写法）
# class Person:
#     # 说明：当一个函数被定义在了类中时，那这个函数就被称为：方法。
#     # __init__方法：初始化方法，主要作用：给当前正在创建的实例对象添加属性
#     # __init__方法收到的参数：当前正在创建的实例对象（self）、其它的自定义参数
#     # 当我们以后编写代码去创建Person类实例的时候，Python会自动调用__init__方法
#     def __init__(self, name, age, gender):
#         # 给实例添加属性（语法为：self.属性名 = 值）
#         self.name = name
#         self.age = age
#         self.gender = gender

"""
创建实例
实例名 = 类名(参数1, 参数2, ...)
"""
# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# # 创建Person的实例对象
# p1 = Person('张三', 18, '男')
# p2 = Person('李四', 22, '女')
#
# # 如果直接打印一个实例的话，我们是看不到实例身上的属性的
# print(p1)
# print(p2)
#
# # 通过点语法可以访问或修改实例身上的属性
# print(p1.name)
# print(p1.age)
# print(p1.gender)
# print('-' * 20)
# print(p2.name)
# print(p2.age)
# print(p2.gender)
# p1.name = '阿三'
# print(p1.name)
#
# # 通过 实例.__dict__ 可以查看实例身上的所有属性
# print(p1.__dict__)
# print(p2.__dict__)
#
# # 实例创建完毕后，依然可以通过 实例.属性名 = 值 去给实例追加属性
# p1.address = '北京昌平宏福科技园'
# print(p1.__dict__)
# print(p2.__dict__)
#
# # 通过type函数，可以查看某个实例对象，是由哪个类创建出来的
# print(type(p1))
# print(type(p2))


"""
自定义方法
『自定义方法』的第一个参数也是self，是调用该方法的实例对象。
"""
# 定义一个Person类
# class Person:
#     # 初始化方法（给实例添加属性）
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     # 自定义方法（给实例添加行为）
#     # speak方法收到的参数是：调用speak方法的实例对象（self）、其它参数
#     # speak方法只有一份，保存在Person类身上的，所有Person类的实例对象，都可以调用到speak方法
#     def speak(self, msg):
#         print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')
#
# # 验证一下：speak方法是存在Person类身上的
# # print(Person.__dict__)
#
# # 创建Person类的实例对象
# p1 = Person('张三', 18, '男')
# p2 = Person('李四', 22, '女')
#
# # 验证一下：Person的实例对象身上是没有speak方法的
# # print(p1.__dict__)
# # print(p2.__dict__)
#
# # 所有Person类的实例对象，都可以调用到speak方法
# # 当执行p1.speak()的时候，查找speak方法的过程：1.实例对象自身(p1)  =>  2.实例的“缔造者”的身上(Person)
# # p1.speak('好好学习')
# # p2.speak('天天向上')
#
# # 验证一下上述的查找过程
# def speak():
#     print('巴拉巴拉巴拉巴拉巴拉')
# p1.speak = speak
# print(Person.__dict__)
# print(p1.__dict__)
# print(p2.__dict__)
# p1.speak()

"""
实例属性
1️ 定义：通过实例.属性名 = 值定义在实例身上的属性，称为：实例属性。
2️ 特点：
1. 每个实例都有自己『独立的一份』实例属性，各个实例之间是互不影响的。  
2. 实例属性只能通过实例.xxxx访问和修改，不能通过『类名』访问或修改。
"""
# # 定义一个Person类
# class Person:
#     # 初始化方法
#     def __init__(self, name, age, gender):
#         # 通过【实例.属性名 = 值】给实例添加的属性，就叫实例属性
#         # 实例属性只能通过实例访问，不能通过类访问
#         # 每个实例都有自己【独一份的】实例属性，各个实例之间是互不干扰的
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# # 创建Person类的实例对象
# p1 = Person('张三', 18, '男')
# p2 = Person('李四', 22, '女')
#
# # 实例属性只能通过实例访问，不能通过类访问
# print(p1.name)
# print(Person.name)

"""
类属性
定义： 在类中直接写赋值语句（例如：a = 100），就会在类身上添加一个a属性，值为 100，此时的a就是『类属性』，它属于类本身，由类所拥有，并且该类创建出来的所有实例对象，都能去访问a属性。  
特点：
1. 所有实例访问的，都是同一个类属性，所以类属性通常用于：存放公共数据。
2. 类属性即可以通过『类』访问，也可以『实例』访问。
"""
# 定义一个Person类
# class Person:
#     # max_age、planet 他们都是类属性，类属性是保存在类身上的
#     # 类属性可以通过类访问，也可以通过实例访问
#     # 类属性通常用于保存：公共数据
#     max_age = 120
#     planet = '地球'
#
#     # 初始化方法
#     def __init__(self, name, age, gender):
#         # 给实例添加属性
#         self.name = name
#         self.gender = gender
#         # 限制age的最大值
#         if age <= Person.max_age:
#             self.age = age
#         else:
#             print(f'年龄超出范围了，已经将年龄设置为最大值：{Person.max_age}')
#             self.age = Person.max_age
#
# # 验证一下：类属性是保存在类身上的
# # print(Person.__dict__)
#
# # 创建Person类的实例对象
# p1 = Person('张三', 18, '男')
# p2 = Person('李四', 22, '女')
#
# # 验证一下：实例身上是没有类属性的
# # print(p1.__dict__)
# # print(p2.__dict__)
#
#
# # 验证一下：类属性可以通过类访问，也可以通过实例访问
# # print(Person.max_age)
# # print(p1.max_age)  # 查找max_age的过程：1.实例自身(p1)  => 2.实例的“缔造者”(Person)
# # print(p2.planet)
#
# # 测试一下年龄超出范围
# # p3 = Person('王五', 170, '女')
# # print(p3.__dict__)


"""
实例方法
定义：类中所定义的方法，最终会保存在类身上，并且主要是通过实例调用，所以叫：实例方法。
特点：
1. 实例方法虽然最终会保存在类身上，但它主要是供实例使用的，所以才叫实例方法。
2. 因为收到了self参数，所以其内部可以：访问实例属性，调用实例方法。
3. 实例方法的主要作用：定义实例对象的具体行为。
"""
# 定义一个Person类
# class Person:
#     # 初始化方法（给实例添加属性）
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     # 下面的speak方法、run方法，都保存在类身上，但他们主要是供实例调用，所以他们都叫：实例方法
#     # 自定义方法（给实例添加行为）
#     def speak(self, msg):
#         print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')
#
#     # 自定义方法（给实例添加行为）
#     def run(self, distance):
#         print(f'{self.name}疯狂的奔跑了{distance}米')
#
# # 创建Person类的实例对象
# p1 = Person('张三', 18, '男')
# p2 = Person('李四', 22, '女')
#
# print(Person.__dict__)
# print(p1.__dict__)
# print(p2.__dict__)
#
# # 通过实例调用实例方法
# p1.speak('你好')
# p1.run(300)
#
# # 通过类去调用实例方法(能调用，但不推荐)
# Person.run(p2, 100)

"""
类方法
定义：使用@classmethod装饰器修饰，第一个参数是类本身，通常用形参cls接收。
特点：
1. 可通过『类名』或『实例名』调用，但强烈推荐通过类名调用以体现语义。
2. 因为收到了cls参数，所以内部可以访问类属性。
3.  一般用于：实现与类相关的逻辑，如：操作类级别的信息、工厂方法等。
"""
# from datetime import datetime
#
# # 定义一个Person类
# class Person:
#     # 类属性
#     max_age = 120
#     planet = '地球'
#
#     # 初始化方法（给实例添加属性）
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     # speak方法、run方法，他们都属于：实例方法
#     def speak(self, msg):
#         print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')
#
#     def run(self, distance):
#         print(f'{self.name}疯狂的奔跑了{distance}米')
#
#     # 使用 @classmethod 装饰过的方法，就叫：类方法，类方法保存在类身上的
#     # 类方法收到的参数：当前类本身（cls）、自定义的参数
#     # 因为收到了cls参数，所以类方法中是可以访问类属性的
#     # 类方法通常用于实现：与类相关的逻辑，例如：操作类级别的信息、一些工厂方法
#     @classmethod
#     def change_planet(cls, value):
#         cls.planet = value
#
#     @classmethod
#     def create(cls, info_str):
#         # 从info_str中获取到有效信息
#         name, year, gender = info_str.split('-')
#         # 获取当前年份
#         current_year = datetime.now().year
#         # 计算年龄
#         age = current_year - int(year)
#         # 创建并返回一个Person类的实例对象
#         return cls(name, age, gender)
#
#
# # 验证一下：类方法保存在类身上的
# # print(Person.__dict__)
#
# # 类方法需要通过类调用
# # Person.change_planet('月球')
# # print(Person.__dict__)
#
# # 创建Person实例
# p1 = Person('张三', 18, '男')
# p2 = Person('李四', 22, '女')
#
# # 验证一下：类属性planet已经修改了
# # print(p1.planet)
# # print(p2.planet)
#
# # 测试一下类方法 —— create
# # p3 = Person.create('李华-2003-女')
# # print(p3.__dict__)
#
# # 注意点：类方法，也能通过实例调用到，但是非常不推荐
# p4 = p1.create('李华-2003-女')
# print(p4.__dict__)


"""
静态方法
定义：使用@staticmethod装饰器修饰，方法没有self或cls参数，只是单纯的定义在类中。
特点：
1. 可通过『类名』或『实例名』调用，但强烈推荐通过类名调用以体现语义。  
2. 由于没有self或cls参数，所以静态方法中通常：不访问类属性，也不访问实例属性。
3. 一般用于：定义与类相关，但可以独立使用的工具方法。
"""


# 定义一个Person类
class Person:
    # *******************************
    # *******************************
    # *******************************
    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 静态方法
    # 使用 @staticmethod 装饰过的方法，就叫：静态方法，静态方法也是保存在类身上的
    # 静态方法只是单纯的定义在类中，它不会收到：self、cls参数，它收到的参数都是自定义参数
    # 由于静态方法没有收到：self、cls参数，所以其内部不会访问任何：类和实例相关的内容
    # 静态方法通常用于定义：与类相关的工具方法
    @staticmethod
    def is_adult(year):
        # 获取当前的年份
        current_year = datetime.now().year
        # 计算年龄
        age = current_year - year
        # 返回结果（成年True，未成年False）
        return age >= 18

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6] + '********' + idcard[-4:]


# 验证一下：静态方法也是保存在类身上的
# print(Person.__dict__)

# 静态方法需要通过类去调用
# result = Person.is_adult(2015)
# print(result)
# result2 = Person.mask_idcard('212101198802030028')
# print(result2)

# 注意点：通过实例也能调用到静态方法，但非常不推荐
# p1 = Person('张三', 18, '男')
# res = p1.mask_idcard('212101198802030028')
# print(res)
