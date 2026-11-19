"""
@description: 函数进阶
"""

"""函数可以像对象一样，动态添加属性。"""
# def welcome():
#     print("你好")
#
# # 动态添加属性
# welcome.desc = "这是一个用于打招呼的函数"
# welcome.version = 1.0
# print(welcome.__dict__)
#
# # 调用函数
# welcome()

"""函数可以赋值给变量。"""
# def welcome():
#     print('你好啊！')
#
# # 把函数对象赋值给变量
# say_hello = welcome
#
# # 通过变量调用函数
# say_hello()
#
# # 通过函数名调用函数
# welcome()

"""可变参数与不可变参数"""
# 不可变参数
# def welcome(data):
#     print(f'函数收到的data是：{data}，地址是：{id(data)}')
#     data = 888
#     print(f'被修改后的data是：{data}，地址是：{id(data)}')
#
# a = 666
# print(f'函数外侧a的值是：{a}，地址是：{id(a)}')
# welcome(a)
# print(f'函数调用后a的值是：{a}，地址是：{id(a)}')

# 可变参数
# def welcome(data):
#     print(f'函数收到的data是：{data}，地址是：{id(data)}')
#     data[2] = 99
#     print(f'被修改后的data是：{data}，地址是：{id(data)}')
#
# a = [10, 20, 30]
# print(f'函数外侧a的值是：{a}，地址是：{id(a)}')
# welcome(a)
# print(f'函数调用后a的值是：{a}，地址是：{id(a)}')

"""函数也可以作为参数"""
# def welcome():
#     print('你好啊！')
#
# def caller(f):
#     print('caller函数开始调用')
#     f()
#
# caller(welcome)

"""函数也可以作为返回值"""
# def welcome():
#     print('你好啊')
#     def show_msg(msg):
#         print(msg)
#     return show_msg
#
# # result = welcome()
# # result('尚硅谷')
# welcome()('尚硅谷')

"""在return关键字后面写多个值，并且多个值之间用逗号隔开，Python 会自动把多个值打包成元组。"""
# def calculate(x, y):
#     res1 = x + y
#     res2 = x - y
#     return res1, res2 # 实际返回的是：(res1, res2)
#
# result = calculate(10, 20)
# r1, r2 = calculate(10, 20)
#
# print(result)  # (30, -10)
# print(r1)      # 30
# print(r2)      # -10

"""
参数的打包与解包
定义函数时，打包接收参数：
● *形参名：打包所有的位置参数（会形成一个元组）。
● **形参名 ：打包所有的关键字参数（会形成一个字典）。
调用函数时，解包传递参数：
● *变量名：将元组拆解成一个一个独立的位置参数。
● **变量名：将字典拆解一个一个key=value形式的关键字参数。
"""
# # 打包接收参数：
# # *args    ：打包所有的位置参数（会形成一个元组）
# # **kwargs ：打包所有的关键字参数（会形成一个字典）
# def show_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# nums = (10, 20, 30)
# person = {'name': '张三', 'age': 18}
#
# # 解包传递参数：
# # *nums    ：将元组拆解成一个一个独立的位置参数
# # **person ：将字典拆解一个一个 key=value 形式的关键字参数
# show_info(*nums, **person)

"""
高阶函数
当一个函数的『参数是函数』或者『返回值是函数』那该函数就是『高阶函数』。

高阶函数的意义：
1. 代码复用性高：可以把行为“独立出去”，传入不同函数实现不同逻辑。
2. 能让函数更灵活，更通用。
3. 高阶函数是：装饰器、闭包的基础。（后面会讲）
"""
# def welcome():
#     print('你好啊！')
# # caller函数的参数是函数，所以caller是高阶函数
# def caller(f):
#     print('call函数开始调用')
#     f()
# caller(welcome)
# # outer函数的返回值是函数，所以outer函数是高阶函数
# def outer():
#     print('我是outer')
#     def inner():
#         print('我是inner')
#     return inner

# def info(msg):
#     return '[提示]' + msg
# def warn(msg):
#     return '[警告]' + msg
# def error(msg):
#     return '[错误]' + msg
#
# def log(fun, text):
#     print(fun(text))
#
# log(info, '文件保存成功！')
# log(warn, '磁盘空间不足！')
# log(error, '该用户不存在！')

"""
条件表达式
表达式：执行后最终能得到一个值的代码，就是表达式，例如这些都是表达式：

语法格式为：
结果1 if 条件 else 结果2
"""
# 3 + 5
# 'abc' * 3
# 5 > 3
# 'y' in 'Python'
# len('hello')

# age = 20
#
# # 传统if-else写法
# if age >= 18:
#     text = '成年'
# else:
#     text = '未成年'
#
# # 条件表达式写法
# text = '成年' if age >= 18 else '未成年·'
# print(text)
#
# rain = True
# food = '外卖' if rain else '出去吃'
#
# is_vip = True
# disscount = 0.8 if is_vip else 1.0
#
# is_login = True
# msg = '欢迎回来！' if is_login else '请先登录！'













