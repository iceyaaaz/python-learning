# region 练习一：Hello World 和 print
# print('hello')
# print("hello1")
#
# # def hello(name):
# #     print(f'hi,{name}')
# #
# # if __name__ == '__main__':
# #     print(hello('宋隋欣'))
# #     print('===')
# #     hello('宋隋欣2')
# #     print('===========')
# #     print(print(hello('宋隋欣')))
# endregion

# region 练习2 函数定义
# def hello(name):
#     # print(f'hi,{name}')
#     return f'hi,{name}'
#
# if __name__ == '__main__':
#     print(hello('宋隋欣'))
#     print('===')
#     hello('宋隋欣2')
#     print('===========')
#     print(print(hello('宋隋欣')))
#     hello('宋隋欣2')
#     hello('宋隋欣2')
#     hello('宋隋欣2')
#     hello('宋隋欣2')
# endregion

# region 练习3# 交换值
# a = 10
# b = 20
# c = a
# a = b
# b = c
# endregion

# region 练习4换行
# print(a,end = " ")
# print('1111',end = ' ')
# print(b)
# print(a,b)
# print(
#     """
# 1
#         2
#     3
#     """
# )
# endregion

# region  练习5 交换值2
"""
现有三个变量，分别为：a = 100, b = 200, c = 300，现需要将这三个变量值进行交换，将a,b,c的值分别赋值给c,a,b，并将其输出到控制台。
"""
# #1. 常规引入临时变量
# a = 100
# b = 200
# c = 300
# d = a
# a = b
# b = c
# c = d
# print(a,b,c)

# # 2.多重赋值，python独有，推荐
# a = 100
# b = 200
# c = 300
#
# c,a,b = a,b,c
# print(a,b,c)

# endregion

# region 练习6 数据类型
# a = 3.14
# print(type(a))
# print(type(a).__name__)
#
# isinstance(type(a),int)
# isinstance(type(a),float)
# print(isinstance(a,int))
# print(isinstance(a,float))

# endregion

# region 练习7 字符串（p14）转义字符

# a = 'i\'m lhl'
# b = "i'm lhl"
# c = "i'm\nlhl"
# d = "i'm\t\t\t\tlhl"
#
# print(a)
# print(b)
# print(c)
# print(d)

# endregion

# region 练习8 +拼接字符串

# a = 'abc'
# b = 'def'
#
# print(a+b)
# print(a+','+b)
# print('123'+a+','+b)
# # print(123+a+','+b)  错误无法实现非字符串与字符相加

# s = "    人生苦短    ""          及时行乐            ""    活在当下    "
# s1 = "人生苦短"                    "及时行乐"                          "    活在当下"
# print(s)
# print('s1 = ',s1)
# print('s1 = '+s1)
# print('s1 = ',s1,s1)
# print('======')

# # 拼接数据类型的数据三种实现方式
# a = 5
# print(f'2+3 = {a}')  # f-string格式化
# print('2+3 = %s'%(a))  # %格式化
# print('2+3 = '+str(a))   #转换类型

# def myself(name,age,major,hobbies):
#     # print(f'大家好，我是{name},今年{age}岁，学习的专业是{major},爱好是{hobbies}')   f-string
#     print('大家好，我是%s,今年%s岁，学习的专业是%s,爱好是%s'%(name,age,major,hobbies))
#
# if __name__ == '__main__':
#     myself('lhl',24,'计算机科学与技术','claude,chatgpt,deepseek,perplexity')

# name = input('请输入name:')
# age = input('age:')
# major = input('请输入major:')
# hobbies = input('请输入hobbies:')
# print('大家好，我是%s,今年%s岁，学习的专业是%s,爱好是%s' % (name, age, major, hobbies))

# total = 10000
# pwd = input('请输入密码:')
# money = int(input('请输入金额:'))   #推荐在此处转为int，如果在下一行转int，若有扣手续费等操作，需要写int(money)比较麻烦
# remain = total - money
# print(f'初始{total}元,取走{money}元,剩余{remain}元')

# a =int(input('请输入第一个数字：'))
# b =int(input('请输入第二个数字：'))
#
# print('和为',a+b)
# print(f'和为{a+b}')

# endregion

# region 练习9 运算符

# 算术运算符=============
# a = 10
# b = 5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

# print('============')

# x = 10
# y = 3
#
# print(x/y)
# print(x//y)
# print(x%y)
# print(x**y)
# print(-7/2)
# print(-7//2)
# print(-7%2)



# # 输入一个秒数，换算成时分秒   要求使用//和%
# seconds =int(input('请输入秒数:'))
#
# print(f'{seconds//3600}小时 {seconds%3600//60}分钟 {seconds%3600%60}秒')

# 赋值运算符===============

# x = 10
# x += 4
# x -= 3
# x *=2
# x/=4
# x //=2
# x %=3
# x **= 2
# print(x)
# print(type(x))

# a = 5
# b = a
# a += 10
# print(a,b)

# total = 0
# total += 25.5
# total+=12
# total -= 5
# total *= 2
# print(total)
# print(type(total))
# total = int(total)
# total//= 2
# print(total)
# print(type(total))

# 比较运算符===============

# print(3 == 3.0)
# print(10!=9)
# print(5>5)
# print(5<=5)
# print('apple' == 'Apple')
# print(10>9>8)

# a = 5
# b = 5.0
# print(a == b)
# print(a is b)

# # 判断60-100
# score = 66
#
# print(f'score = {score},是否在60-100之间:{score>=60 and score<=100}')


# 逻辑运算符==========

# print(True and False)
# print(True or False)
# print(False or False)
# print(not True)
# print(not False)
# print(not(3>5))
# print(5>3 and 2<4)
# print(5<3 or 2<4)

# print(0 and "hello")
# print(3 and "hello")
# print(0 or "hello")
# print(3 or "hello")
# print(not 0)
# print(not '')
# print(not "hello")

# 综合题:判断能否参加活动，条件：满18，完成认证，非黑名单
# 已知
"""
age = 20
vertified = True
blacklisted = False
要求用and not写出判断条件
输出可以参加或不可以参加
再把age改成16，flase,true分别测试结果
"""

# # 纯运算符的高级魔法，不需要 if
# age = 20
# verified = True
# blacklisted = False
#
# # 如果前面条件为真，and 就返回后面的 "可以参加"；如果为假，or 就返回后面的 "不可以参加"
# result = age>=18 and verified and not blacklisted and '可以参加' or '不可以参加'
# print(result)

# 浮点数精度损失

# print(0.1+0.2)
#
# result = 0.1+0.2
# print(f'{result:.2f}')

# endregion