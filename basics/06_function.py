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


##### 参数默认值
# # 定义函数时，『默认参数』必须放在『必选参数』的后面，或者换一种说法就是：某个形参，一旦设置了默认值，那它后面的所有形参，也必须要写默认值！
# def greet(name, gender, age, height , msg='你好'):
#     print(f'我叫{name}， 性别{gender}， 年龄{age}， 身高是{height}cm')
#     print(f'我想说:{msg}')
# # 调用函数
# greet('张三', '男', 18, 172)
# greet('张三', '男', 18, 172, 'hello')
# greet('张三', '男', 18, 172, msg='hello')


# 可变参数. args 只是大家习惯这么写，也可以用其他变量名称代替
# def test1(*args):
#     print(args)
# test1(1, 2, 3)

# 可变关键字参数。定义函数（使用**kwargs去接收：可变关键字参数，kwargs只是大家习惯这么写，当然也可以换成其他变量）
# def test2(**test_args):
#     print(test_args)
# # 调用函数
# test2(name='张三', gender='男', age=18, height=172)

# 特殊字面量 none
# None是一个特殊的字面量，它表示：空值 / 无值 / 无意义。
msg = None

# None 的类型是 NoneType。
print(type(msg))

# None 转为布尔值是 False。
print(bool(msg))
if not msg:
    print('你好')

# 不能参与数学运算，也不能与字符串拼接。
# result1 = msg + 1
# result1 = msg + 'hello'
