"""
Python 数据类型学习：字符串

文件说明放在文件开头；类和方法说明放在各自定义内部的第一条语句处。
文档字符串使用三重双引号，下面采用常见的 Google 风格。
"""

name = '张三'
gender = '男'
weight = 65.2
age = 12

info1 = '我叫' + name + '，我是' + gender + '生'

name = '张三'
gender = '男'
weight = 65.2
age = 12

info2 = '我叫%s，我是%s生，我体重是%f，年龄是%d' % (name, gender, weight, age)
print(info2)

name = '张三'
gender = '男'
weight = 65.2
age = 12

info3 = f'我叫{name}，我是{gender}生，我体重是{weight}，年龄是{age}'
print(info3)