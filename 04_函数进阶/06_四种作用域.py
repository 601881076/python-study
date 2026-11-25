"""
四种作用域

Python 中有四种作用域，分别是：
1. Local（局部作用域）
2. Enclosing（外层作用域）
3. Global（全局作用域）
4. Built-in（内建作用域）
当访问一个变量时，Python 会按以下顺序查找：  Local   =>  Enclosing   => Global   => Built-in
"""

"""
局部作用域（Local）
定义：函数的内部就是局部作用域，局部作用域中的变量，只在该函数内部可见。
特点：
● 每次调用函数都会创建一个新的局部作用域。
● 函数运行结束后，局部作用域会随之销毁。
● 局部作用域优先级最高，即：查找一个变量时，Python 会首先在局部作用域中查找。
"""
# def test():
#     x = 10  # x 在局部作用域
#     print(x)  # 可以访问
#
# print(x)  # ❌ 报错：x 在局部之外不可见

"""
外层作用域（Enclosing）
定义：如果函数中又定义了函数，那么外层函数的作用域，就是内层函数的 Enclosing 作用域。
特点：
● 只有当函数“嵌套定义”时才会出现。
● 内层函数可以读取外层函数变量。
● 想修改外层变量必须使用nonlocal。
"""
# def outer():
#     y = 20
#     def inner():
#         print(y)
#
#     inner()
# outer()

# 修改外层变量
# def outer():
#     y = 20
#     def inner():
#         # nonlocal y
#         y= 99
#         print(y) # 输出 99，此处输出的是 inner 函数的局部变量y
#     inner()
#     print(y) # 输出20
# outer()

"""
全局作用域
定义：.py文件就是全局作用域，全局作用域中的变量，在当前.py文件的任何位置都可以访问。
特点：
● 全局变量只在当前.py文件中可见。
● 函数内部可以使用global关键字修改全局变量。
"""
# a = 100  # 全局变量
#
# def test():
#     print(a)  # 可以读取
#
# test()
# print(a)  # 在本文件任何位置都可以访问

# 修改全局作用域
# a = 100
# def test():
#     global a
#     a = 200  # 修改全局变量
#     print(a)
#
# test()
# print(a)

"""
定义：Python 预先定义好的东西，会放在内建作用域中，所有.py文件都可以直接使用。
特点：
● 所有.py文件都能直接使用其中的名称。
● 例如：print、len、range、sum、max 等。
● 查找优先级最低，即：查找一个变量时，内建作用域是“最后一道防线”。
"""
# print('hello')
# len([1, 2, 3])