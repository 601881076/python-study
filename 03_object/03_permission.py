"""
@Description: 属性权限控制

"""

"""
三种访问权限
权限类型	    定义方式	    在当前类内部访问	在子类内部访问	在类外部访问
公有属性	    属性名	    ✅ 能	        ✅ 能	        ✅ 能
受保护属性	_属性名	    ✅ 能	        ✅ 能	        ⚠️ 能（但不推荐）
私有属性	    __属性名	    ✅ 能	        ❌ 不能	        ❌ 不能
"""
# class Person:
#     def __init__(self, name, age, idcard):
#         self.name = name        # 公有属性：当前类内部、子类内部、类外部，可都可访问
#         self._age = age         # 受保护属性：当前类内部、子类内部，可以访问
#         self.__idcard = idcard  # 私有属性：仅能在当前类内部访问
#
#     def speak(self):
#         # 类的内部，可以访问任何权限的属性（公有属性、受保护属性、私有属性）。
#         print(f"我叫：{self.name}，年龄：{self._age}，身份证：{self.__idcard}")
#
# class Student(Person):
#     def hello(self):
#         # 子类的内部可以访问：公有属性、受保护属性
#         print(f"我是学生，我叫：{self.name}，年龄：{self._age}")
#
# p1 = Person('张三', 18, '110101199001011234')
# print(p1.name)
#
# # 类的外部，仅能访问公有属性
# # 注意：如果在类的外部，强制访问【受保护的属性】，也能访问，但最好别这么做
# # print(p1._age)
#
# # 强制访问【私有属性】会报错
# # print(p1.__idcard)
#
# # 扩展：Python保护【私有属性】的方式，是重命名，例如：__idcard属性，会被重命名为：_Person__idcard
# # print(p1.__dict__)
# # print(p1._Person__idcard)

"""
getter 与 setter

"""
# class Person:
#     def __init__(self, name, age, idcard):
#         self.name = name
#         self._age = age
#         self.__idcard = idcard
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value <= 120:
#             self._age = value
#         else:
#             print('年龄非法，已将年龄变为最大值120')
#             self._age = 120
#
#     @property
#     def idcard(self):
#         return self.__idcard[:6] + '********' + self.__idcard[-4:]
#
#     @idcard.setter
#     def idcard(self, value):
#         print("抱歉，身份证号不允许随意修改，如有特殊需求，请联系管理员！")
#
# p1 = Person('张三', 18, '110101199001011234')
# print(p1.age)
# print(p1.idcard)
#
# # 测试修改age
# p1._age = 19
# print(p1.age)
# # 测试修改idcard
# p1.idcard = 'asd'

"""
魔法方法
● 概念：以 __xxx__ 命名的特殊方法（双下划线开头和结尾）。
● 特点：不需要手动调，在特定场景由 Python 自动调用。
"""

# 类中以双下划线开头和结尾的方法，叫魔法方法（魔术方法）。
# 魔法方法不需要手动调用，Python会在特定场景自动调用。
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # __str__ 方法，执行时机：当调用 print(对象)或str(对象) 时
    def __str__(self):
        return f'姓名：{self.name}， 年龄：{self.age}， 性别：{self.gender}'

    # __len__ 方法，执行时机：当调用len(对象)时
    def __len__(self):
        return len(self.__dict__)

    # __lt__方法，执行时机：当执行 对象1 < 对象2 时
    def __lt__(self, other):
        return self.age < other.age

    # __gt__方法，执行时机：当执行 对象1 > 对象2 时
    def __gt__(self, other):
        return self.age > other.age

    # __eq__方法，执行时机：当执行 对象1 == 对象2 时
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # __getattr__方法，执行时机：当访问了对象不存在的属性时
    def __getattr__(self, item):
        print(f'您访问的{item}属性，不存在！')

# 创建Person实例
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# 测试代码
print(p1)
print(str(p1))
print(len(p1))
print(p1 < p2)
print(p1 > p2)
print(p1 == p2)
print(p1.address)