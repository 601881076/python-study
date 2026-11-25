"""
装饰器
● 概述：装饰器是一种在【不修改原函数代码】的前提下，对函数进行【增强】的工具。
    它是 Python 中非常强大的语法特性，常用于：日志、校验、计时、缓存、权限控制等。
● 核心语法： 装饰器是一种可调用对象（通常是函数），接收一个函数作为参数，并返回一个新函数。
"""

"""
函数装饰器 
需求：在不修改add函数的前提下，给add函数增加一些额外的功能，例如：计算前打印一句欢迎语。
"""

# 定义函数装饰器
# 定义装饰器核心规则：
# 1. 接收被装饰的函数、同时返回新函数（wrapper）
# 2. 装饰器“吐出来”的是 wrapper 函数，以后别人调用的也是 wrapper 函数。
# 3. 为了保证参数的兼容性，wrapper 函数要通过 *args 和 **kwargs 接收参数。
# 4. wrapper 函数中主要做的是：调用原函数（被装饰的函数）、执行其它逻辑，但要记得将原函数的返回值 return 出去。
# def say_hello(func):
#     def wrapper(*args, **kwargs):
#         print('你好，我要开始计算了')
#         return func(*args, **kwargs)
#
#     return wrapper


# 使用函数装饰器(手动装饰)
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# f_add = say_hello(add)
# result = f_add(10, 20, 30)
# print(result)

# 使用函数装饰器（语法糖@）
# 下述代码的执行流程：
# 1. @say_hello 会自动执行： add = say_hello(add)。
# 2. 以后调用 add()时，真正执行的是wrapper()。
# @say_hello
# def add(x, y, z):
#     res = x + y + z
#     print(f'相加的结果是: {res}')
#
#     return res
#
#
# result1 = add(1, 2, 3)
# print(result1)

"""
带参数的函数装饰器（三层嵌套）
需求：装饰不同的函数，打印不同的欢迎语。
核心：带参数的装饰器最终是三层嵌套结构：外层接收配置、中间层接收函数、内层接收具体参数。
"""

# def say_hello(msg):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             print(f'你好，我要开始 {msg} 计算了')
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return outer
#
#
# # 装饰加法函数
# @say_hello('加法')
# def add(x, y, z):
#     res = x + y + z
#     print(f'相加的结果是： {res}')
#     return res
#
#
# # 装饰减法函数
# @say_hello('减法')
# def sub(x, y):
#     res = x - y
#     print(f'相减的结果是：{res}')
#     return res
#
#
# # 测试
# result1 = add(10, 20, 30)
# print(result1)
#
# result2 = sub(30, 20)
# print(result2)

"""
多个函数装饰器一起使用
核心：注意装饰顺序，距离函数最近的装饰器，会先工作。
例如下面代码：test2先装饰，test1再装饰。
"""


def test1(func):
    print(f'我是test1装饰器')

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'test1追加逻辑')
        return res

    return wrapper


def test2(func):
    print(f'我是test2装饰器')

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('test2追加逻辑')
        return res

    return wrapper


# @test1
# @test2
# def add(x,y):
#     result = x + y
#     print(f'相加的结果是{result}')
#     return result


# result = add(1, 2)
# print(result)

# 上述函数装饰器可等价与下列代码
def add(x, y):
    result = x + y
    print(f'相加的结果是{result}')
    return result


wrapper_test2 = test2(add)  # 打印：我是test2装饰器
add = test1(wrapper_test2)  # 打印：我是test1装饰器

# 调用包装后的函数
result = add(1, 2)
print(result)
