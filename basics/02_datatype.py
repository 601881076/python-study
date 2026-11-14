"""
Python 数据类型学习：通过学生类演示字符串和整数类型。

文件说明放在文件开头；类和方法说明放在各自定义内部的第一条语句处。
文档字符串使用三重双引号，下面采用常见的 Google 风格。
"""


class Student:
    """保存学生的姓名和年龄。

    Attributes:
        name (str): 学生姓名。
        age (int): 学生年龄，单位为岁。

    Example:
        >>> student = Student("小明", 18)
        >>> student.name
        '小明'
        >>> student.age
        18
    """

    def __init__(self, name: str, age: int) -> None:
        """根据姓名和年龄创建学生对象。

        Args:
            name: 学生姓名。
            age: 学生年龄，单位为岁。
        """
        self.name: str = name
        self.age: int = age

# 使用变量接收 type() 返回的类型
result1 = type('张三')
result2 = type(18)
result3 = type(72.5)

print(result1) # <class 'str'> 注意此处返回的不是string，是 string 的简写：str
print(result2) # <class 'int'>
print(result3) # <class 'float'>

name = '张三'
age = 18
weight = 72.5

# 使用变量接收type()返回的类型
result1 = type(name)
result2 = type(age)
result3 = type(weight)

# 打印这三个数据类型
print(result1)  # <class 'str'>
print(result2)  # <class 'str'>
print(result3)  # <class 'float'>

############ 整形 ############
num1 = 10_000_000
print(num1)

a = 3 ** 2
b = 2 ** 3
print(a)
print(b)

import sys
sys.set_int_max_str_digits(0)
a = 9 ** 9999  # 9的9999次方
print(a)  # 打印x

############ 浮点型 ############

