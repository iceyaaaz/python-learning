# region 练习 1

# def triangle(a,b,c):
#     """
#     :param a: 长
#     :param b: 宽
#     :param c: 高
#     :return: 三角形面积
#     963852741
#     """
#     return a+b+c
#
# t = triangle(1,2,3)
# print(t)
#
# help(triangle)


# def a():
#     print('1')
#
#     x = b()
#     print(x)
#     return 444
# def b():
#     print('2')
#     x = c()
#     print(x)
#     print('6')
#
#     return 333
# def c():
#     print('3')
#     x = d()
#     print(x)
#     print('5')
#
#     return 222
# def d():
#     print('4')
#     return 111
#
# # a()             #1234567
# print(a())      #会多返回一个none

# def area(bottom,high):
#     return bottom*high/2
# s = area(4,5)
# print(s)

# def count(words):
#     number = 0
#     for i in words:
#         if i in 'aeiouAEIOU':
#             number += 1
#     return number
# c = count('aaaAAAEEE666666')
# print(c)

# 法1
# def score(s):
#     max_score = max(s)
#     min_score = min(s)
#     avg_score = sum(s)/len(s)
#     return f'{max_score},{min_score},{round(avg_score,1)}'      #此方法可以计算出结果，但是f表达式，不方便取用，可以写成解包形式如下法2
#
# fenshu = score([1,2,3,0.2])
# print(fenshu)

# 法2
# def score(s):
#     max_score = max(s)
#     min_score = min(s)
#     sum_score = sum(s)
#     avg_score = sum_score / len(s)
#     return max_score,min_score,avg_score
#
# largest,smallest,average = score([1,2,3,5,5.3])
# print(f'最高分{largest},最低分：{smallest},平均分：{average:.1f}')

# def a():
#     print(1+2+3)
# x = a()     #首先调用a(),输出6，函数a没有return返回值，默认返回none，赋值给x，但是在此句没有输出x，所以只会输出6，但是x已经被赋值为none
# print(x)    #输出none,上面语句赋值结果
#
# def b():
#     return 1+2+3
# y = b()     #此时调用b()，y被赋值为6，但没有print，所以不会输出任何内容
# print(y)    #输出上一句赋值的6

# # 遇到return后终止，下面不会再执行
# def a():
#     if 1:
#         if 1:
#             if 1:
#                 return 1
#             print('1')
#             print('2')
#             print('3')
#             return 2
#         print('4')
# a()
# print(a())


# ============================day6


# def msg2(name,names = [],age = 18):
#     a = []
#     names.append(name)
#     a.append(names)
#     return a
#
# msg2('1')   #’1‘的年龄是18          ‘1’
#
# print(msg2(666,[2,3,6]) ) #666的年龄是2     2，666
# print(msg2(777) ) #666的年龄是2     2，666
# print(msg2(888) ) #666的年龄是2     2，666
# print(msg2(999) ) #666的年龄是2     2，666
# print(msg2(000) ) #666的年龄是2     2，666
# print(msg2(000,[666],120) ) #666的年龄是2     2，666

# def more(*args,**kwargs):
#      print(args, kwargs.values())
#
# more(1,2,3,name='abc')

# def change_score(scores,subject,new_score):
#         scores[subject] = new_score
# lhl = {'name':'lhl','english':80,'chinese':90}
# ssx = {'name':'ssx','chinese':100}
# print(f'修改前{lhl}')
# print(f'修改前{ssx}')
# change_score(lhl,'english',6666666666)
# print(f'修改后{lhl}')
# print(f'修改后{ssx}')

# def x(a,b,*,c = True):
#     return a+b+c

# def x(a,/,b,*,c):
#     return a+b+c
# res = x(1,b = 2,c = 3)
# print(res)

# count = 0
# def func():
#     global count
#     count += 1
#     # a = count+1
#     print(count)
# func()
# print(count)
# print(count)

# def add666(m,n):
#     return m+n
# def func(oper,b,*c):
#     return oper(b,c)
# x = func(add666,(1,2),[3,4],[5,6],[7,8])
# print(x)

# a = 10
# def x():
#     a= 20
#     def y():
#         # global a      #10
#         nonlocal a
#         print(a)
#     y()
#
# # x()     #10
# x()     #20
#
# def key1(x):
#     return -x**2        #key只按照规则排序，不改变数据
# a = [1,-2,3,4,-5,8,7,6,-9,0,-10]
#
# s = sorted(a,key = key1 , reverse=True)
# print(s)

# date_list = ['sf','bafcgrsf','dd','aaaaaaaaa']
# # date_list.sort()
# # print(date_list)
#
# date_list.sort(key=lambda x:len(x))
# print(date_list)
#
# s = sorted(date_list,key=lambda x:len(x),reverse=True)
#
# print(date_list)
# print(s)

# def jie(x):
#     if x <=1:
#         return 1
#     return x*jie(x-1)
# print(jie(3))

# def outer():
#     x = 10
#     def inner():
#         print(x)
#     return inner
# outer()
# f = outer()
# f()

# def mm(score):
#     return max(score),min(score)#如果返回的形式是f表达式，就不能解包，会被解析成字符串。只有这种最简单的才能被解析成两个值
# a,b = mm([1,2,3,4,5,6,7,8,9,5,5,222,41])#解包
# print(a)
# print(b)
#
# def msg(name,age,sex = 'nan'):
#     return f'{name} is {age} years old and {sex}性'
# print( msg('lhl',24))
# print( msg(age = 24,name='lhl'))#位置参数必须写在关键字参数的前面。

# def a(name,names = [1,2,3] ):
#     names.append(name)
#     return names
# print(a(1))
# print(a(1))
# print(a(1))

# def f(scores):
#     scores[name] = 'lhl'
#     return scores


# def f(scores):
#     scores["math"] = 98     # 修改传进来的那份字典
#     scores["math"] = 989999     # 修改传进来的那份字典
#     scores = {"math": 100}  # 让局部变量 scores 指向一份新字典,之后再执行scores["math"] = 666都无法改变外部scores了，因为已经不是指向同一个变量了
#     print(scores)           # {'math': 100}
#     scores["math"] = 666    #只能改变函数内部分数，无法改变外部了，因为上面指向变了
#     print(scores)
#
# ming_scores = {"math": 95}
# f(ming_scores)
# print(ming_scores)          # {'math': 98}


# def f(scores):
#     scores['math'] = 666    #全局和局部都指向
#     print(scores)
#     scores = {'english': 77, 'french': 88}  #生成新的局部scores，此后对scores的修改只对局部scores生效
#     print(scores)
#     scores['math'] = 888    #对全局不生效，只对局部生效。不存在则新增math=888，若存在则修改math值为888
#     print(scores)
#
# lhl = {'name':'lhl','math':100}
# f(lhl)
# print(lhl)

# # 变量作用域
# a = 1
# def x():
#     a = 2
#     print(a)
#     return a
# x()
# print(a)
#
# b = x()
# print(b)

# def x(counts):
#     return counts+1
#
# c = 1
# counts = x(c)
# counts = x(counts)
# counts = x(counts)
# print(counts)

# def x():
#     global c
#     c+=1
#
# c = 0
# x()
# x()
# x()
# print(c)

# def outer():
#     score = 60
#     def inner():
#         nonlocal score    # 声明：这个 score 是 outer 里的
#         score += 10
#     inner()
#     print(score)          # 70
#
# outer()

# def f(x):
#     return max(x)
# a =([1,2,3,5,6,4])
# print(a)

# a =([1,2,3,5,6,4],[9,5,2,3,6],[51,4,52,5])
# b = max(a,key=lambda x:x[2])
# print(b)

# a = [1,2,3,4]
# b = map(lambda x: x*2,a)
# print(list(b))

# 递归阶乘
# def x(n):
#     if n <= 0:
#         return 1
#     return n*x(n-1)
# a = x(2)
# print(a)

# bibao闭包
# def outer():
#     x = 10
#     def inner():
#         print(x)
#     return inner
# outer()  #空
#
# f = outer()
# f() #10

# # 计数器闭包
# def outer():
#     x = 0
#     def inner():
#         nonlocal x
#         x = x + 1
#         return x
#     return inner
# a = outer()
# print(a())
# print(a())
# print(a())

# def s(a:int,b:float)->float:
#     return a+a*b
# print(s(5,3.3))













