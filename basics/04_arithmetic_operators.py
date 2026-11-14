"""
Python 数据类型学习：算术运算符
文件说明放在文件开头；类和方法说明放在各自定义内部的第一条语句处。
文档字符串使用三重双引号，下面采用常见的 Google 风格。
"""

# 加
print(9 + 7)
# 减
print(7 - 2)
# 乘
print(3 * 4)
# 除
print(9 / 3)
# 取整
print(9 // 6)
# 取余
print(9 % 6)
# 指数
print(2 ** 3)

################### 赋值运算符 ###################
print('################### 赋值运算符 ###################')
age = 18
print(age)

price = 52
print(price)

# 布尔类型是int类型的子类型，底层的本质是用1表示True，用0表示False
print('################### 布尔类型 ###################')
print(int(True))   # 1
print(int(False))  # 0

print(4 + True)   # 5
print(8 - False)  # 8

print(True + True)   # 2
print(True - False)  # 1

print(7 > True)    # True
print(False <= 0)  # True