"""
Python 数据类型学习：函数入门

文件说明放在文件开头；类和方法说明放在各自定义内部的第一条语句处。
文档字符串使用三重双引号，下面采用常见的 Google 风格。
"""

# 定义函数
def welcome():
    print('欢迎来到尚硅谷课堂！')
    print('尚硅谷，让天下没有难学的技术！')

print(f'当前 __name__ 的值：{__name__}')



# if __name__ == '__main__':
    # 调用函数（让函数中的代码运行起来）
    # welcome()
    # welcome()
    # welcome()

# 定义函数（定义的同时：声明需要两个参数，分别是：菜品数量 num，和菜品名称 dish）
def order(num, dish):
    print(f'您点的是: {num} 份 {dish}')
    print(f'{dish}可是很好吃的')
    print(f'只点了{num}份，够吃吗? \n')
# order(1, '辣椒炒肉')
# order(2, '辣子鸡')


# 位置参数，受顺序限制
# order(3)  # 参数少了
# order(4, '宫保鸡丁', 7)  # 参数多了
# order('宫保鸡丁', 4)  # 实参顺序没有和形参保持一致，不会报错，但会造成数据错乱。

# 关键字参数, 不受顺序限制
# def greet(name, gender, age, height):
#     print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')

# greet(name='张三', gender='男', age=18, height=100)
# greet(gender='女', age=18, height=151, name='杨欢')


##### 限制传参方式: /前面只能用『位置参数』，*后面只能用『关键字参数』。
# def greet(name, /, gender, *, age, height):
#     print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')

# 正确示例
# greet('张三', '男', age=18, height=172)
# greet('张三', gender='男', age=18, height=172)

# 错误示例
# greet(name='张三', gender='男', age=18, height=172)
# greet('张三', '男', 18, height=172)



