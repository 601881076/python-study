"""
以下函数是截至目前，我们需要掌握的一些常用函数，
注意：下面这些并不是所有，我们后面还会学习到更多的常用内置函数。
"""
import sys
from cmd import PROMPT
from os.path import sep

"""
输入与输出
函数 / 参数	功能说明
print	    输出指定内容
objects	    要输出的内容
sep	        输出多个内容时的分隔符
end	        结尾追加的内容
file	    输出位置（默认控制台）
flush	    是否立即刷新输出, 默认 False。设为 True 会强制立刻把缓冲区内容写出去。
input()	    获取用户输入
"""
# str_nums = ['张三', '李四','王五']
# print(*str_nums, sep='|', end='\n', file=sys.stdout, flush=True)
#
# # input(prompt='') ，prompt 是提示字符串，会先输出到控制台，不会自动换行。可以省略：
# result = input(">>> ")
# print("你好,", result)

"""
类型转换
函数  	功能说明
int()	转为整数
float()	转为浮点数
str()	转为字符串
bool()	转为布尔值
list()	转为列表
tuple()	转为元组
set()	转为集合
dict()	转为字典
"""
# b = bool(1)
# print(b)

"""
数学相关
函数	            功能说明
abs()	        取绝对值
round()	        银行家舍入法：小于5舍，大于5入，等于5看奇偶（奇入偶舍）
pow(a, b)	    计算 a 的 b 次方
pow(a, b, c)	计算 a 的 b 次方后，再对 c 取模
divmod(a, b)	返回 (商, 余数)
max()	        最大值（支持 key）
min()	        最小值（支持 key）
sum()	        求和
map()	        加工一组数据
filter()	    按条件过滤数据
reduce()	    合并计算（需 functools.reduce）
sorted()	    排序（支持 key）
"""

"""
number：要舍入的数字，通常是 int 或 float。
ndigits：保留位数，可省略。
        省略或为 None：返回最接近的整数。
        正数：保留小数位。
        负数：对整数部分舍入，如十位、百位。
"""
# print(round(5.34, 1))
# print(round(5.66, 1))
# print(round(566, -1))

print(pow(2,4))
print(pow(2,4,2))

"""
数据容器相关
函数	        功能说明
len()	    获取容器中元素个数
range()	    生成数字序列（常用于循环）
enumerate()	为序列添加索引
zip()	    将多个序列一一配对
"""

# enumerate(可迭代对象, start=0) 每次产生一个 (编号, 元素) 元组。
# names: list[str] = ['张三', '李四', '王五']
#
#
# print('\n--- enumerate() ---')
# print(list(enumerate(names)))  # [(0, '张三'), (1, '李四'), (2, '王五')]
#
# # 展示名单时用 start=1，让编号从 1 开始。
# for number, name in enumerate(names, start=1):
#     print(f'{number}. {name}')
#
# # zip() 按位置配对，每次从每个可迭代对象取一个元素组成元组。
# scores: list[int] = [90, 85, 92]
#
# print('\n--- zip() ---')
# for name, score in zip(names, scores):
#     print(f'{name} 得了 {score} 分')
#
# # 默认以最短的输入为准。这里只有两个分数，所以只得到前两组。
# print(list(zip(names, [90, 85])))  # [('张三', 90), ('李四', 85)]

"""
逻辑判断相关

函数	功能说明
all()	所有元素为真时返回 True
any()	至少一个为真返回 True

两个函数的入参是一个可迭代对象。
"""

# exam_scores: list[int] = [90, 85, 92]
#
# print('\n--- all() 和 any() ---')
#
# # score >= 90 for score in exam_scores 会依次判断每个分数，产生 True、False、True。
# # all() 遇到第一个假值就返回 False，any() 遇到第一个真值就返回 True。
# print('所有人都及格：', all(score >= 60 for score in exam_scores))  # True
# print('所有人都达到 90 分：', all(score >= 90 for score in exam_scores))  # False
# print('至少一人达到 90 分：', any(score >= 90 for score in exam_scores))  # True
# print('至少一人拿到满分：', any(score == 100 for score in exam_scores))  # False
#
# # 也可以直接传入列表。Python 会判断每个元素的真假，例如空字符串为假。
# names_to_check: list[str] = ['张三', '', '王五']
# print('姓名全部已填写：', all(names_to_check))  # False
# print('至少填写了一个姓名：', any(names_to_check))  # True
#
# # 空列表里没有假值，也没有真值，因此 all([]) 为 True，any([]) 为 False。
# print('空列表的判断结果：', all([]), any([]))  # True False


