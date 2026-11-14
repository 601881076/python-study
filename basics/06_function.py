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

if __name__ == '__main__':
    # 调用函数（让函数中的代码运行起来）
    welcome()
    welcome()
    welcome()