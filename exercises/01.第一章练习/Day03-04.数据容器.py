# region 练习 1 列表

# a = ['a','b','c',1,2,True,2.22,[1,2,3],['a',1],'',]
# print(a)
# print(type(a[5]))
# print(type(a[6]))
# print(type(a[7]))
# print(type(a[8]))
#
# print(a[0])
# print(len(a))

# a = ["A", "B", "C", "D", "E"]
# print(a[-3:-1:1])
# print(a[99:] )    # []，切片会把越界端点裁剪到有效边界


# i = 0
# s = []
# while i<10:
#     s.append(int(input('请输入数字：')))
#     i = i + 1
# s.sort(reverse=True)
# print(s)
# print(s[-1])
# print(s[0])
# print(sum(s)/len(s))

# 去重
# num_list1 = [1,2,5,33,6,4,1]
# num_list2 = [1,2,5,5,6,3,88,4,1]
# num_list3 = []
#
# for num in num_list1+num_list2:
#     if num not in num_list3:
#         num_list3.append(num)
# print(num_list3)

# # 法2用 | 运算符求并集，或者用 set1.union(set2)
# result = list(set(num_list1) | set(num_list2))
# print(result)


# a = [1,2,3]
#
# b = a[:]
# print(a)
# print(b)
# print(a is b)

# # 创建二维列表1
# rows = 2
# cols = 3
#
# table = [[0] * cols for _ in range(rows)]
# print(table)  # [[0, 0, 0], [0, 0, 0]]
#
# # 创建列表2
# table = []
#
# for _ in range(rows):
#     table.append([0] * cols)


# 练习
# # 生成1-20平方列表
# squares = [a**2 for a in range(1,21)]
# print(squares)
#
# num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
#
# # 语法：[对元素的处理 for 元素 in 原列表 if 条件]
# a = [x**2 for x in num_list if x%2==0]
# print(a)
#
# num_list2 = []
# for i in num_list:
#     if i % 2 == 0:
#         num_list2.append(i**2)
# print(num_list2)

# endregion

# region 练习2 字符串

# print('aaa,;  /\\  ')

# s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaa'
# s1 = [1,1,1,1,1,1,1]
# # print(s[99])
# # print(s1[99])
#
# print(s[99::-1])


# s= 'banana'.find('na')
# print(s)
#
# s = 'banana'
# print(s in 'bananana')


# print('hi \n\n\n\n'.strip())

# print("apple,banana,pear".split("==="))  # ['apple', 'banana', 'pear']

# words = ["apple", "banana", "pear"]
#
# print(",".join(words))    # 'apple,banana,pear'
# print(" 666".join(words))    # 'apple banana pear'
# print("".join(words))     # 'applebananapear'




# a = input('请输入邮箱:')
#
# if '@' in a and '.' in a:
#     print('111')
# else:
#     print('zzz')

# # 判断回文
# a = input("请输入一个字符串：")
#
# for i in range(len(a)):
#     if a[i] != a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')

# # 用切片
# a = input("请输入一个字符串：")
# if a[::] == a[::-1]:
#     print('yes')
# else:
#     print('no')


# # 输入10个字符串，反转后全部转为大写，记录在列表中，最后将列表内容遍历输出
# n = 0
# a = []
# for i in range(10):
#     n = n + 1
#     a.append(input(f'请输入第{n}个字符串：'))
# a.reverse()
#
# for k in range(len(a)):
#     a[i] = a[k].upper()
#
# for j in a:
#     print(j)


# a = 'aaa''bbb'
# b = 'aaa'+'bbb'
# c = a+b
# # c = ab   隐式拼接不能用变量
# print(a)
# print(b)


# s = "Python"
# a = s[99:]
# b = s[:99]
# print(a)
# print(b)

# print('na' in 'banana')
# print('banana'.rfind('na'))

# print('banana'.find('na'))
# print('banana'.index('na'))
#
# # print('banana'.find('666'))
# print('banana'.index('666'))

# s = 'python'        #不能p
# if s.find('y') != 0:
#     print('包含y字符串，且位置不为0')


# s = '    py\nt    \\hon     '
# print(s)
# print(repr(s))
# print(s.upper())
# print(s.lower())

# s[0] = 'aaa'
# print(s)

# s1 = 'P'
# s = s1+s[1:]
# print(s)

# s = s.replace('o','O')
# print(s)
#
# s = s.strip()
# print(s)
#
# s=s.upper()
# print(s)

# print("hello wORLd".capitalize())
# print("hello wORLd".replace('l','9',1))
# print("hello wORLd".replace('l','9',2))
# print("hello wORLd".removesuffix('Ld'))
# print("he666llo 666wORLd666".removeprefix('666'))
# print("   he666llo    666wORLd666   ".strip())

# print('123'.isdigit())
# print('123'.isalnum())
# print('aaa'.isalnum())
# print('aa a '.isalnum())
# print('aa'.isalpha())
# print('aa1'.isalpha())
# print('aa1 '.isspace())
# print('                  \n\t        '.isspace())







# endregion

# region 练习3 元组

# print(len(tuple(10, 20, 30)))

# empty = ()
# single = (10,)
# number = (10)
# list = [10,]
#
# print(type(empty))   # 输出: <class 'tuple'> （是元组）
# print(type(single))  # 输出: <class 'tuple'> （是元组）
# print(type(number))  # 输出: <class 'int'>   （是整数！）
# print(type(list))
# print(type([10,]))
# print(type(([10,])))

#
# students = (
#     ['lhl',18,'y','6666'],
#     666,
#     True,
#     2.5,
#     ['lhl',1888888,'y','6666']
# )
# print(students)
# print(students[0])
# print(type(students))
# print(type(students[0]))
# print(type(students[1]))
# print(type(students[2]))
# print(type(students[3]))















# endregion tuple

# region 练习 4 集合set

# s = {True,1,1,1,1,5,9,6,'ff',True,'true',555,(123),}
# print(s)
# print(type(s))
#
#
# print(hash("aaa"))
# print(hash(('python')))
# print(hash(True))
# print(hash(False))

# print(set('banana'))
# print({'banana', 'aaaa'})
# print(type(('banana','aaaa')))

# s = {1,2,3}

# print(s)
# s.add(4)
# print(s)
# s.update([7,8,9])
# print(s)
# s.update({4,5,6})
# print(s)
# s.update('abc')
# print(s)
# s.remove('a')
# print(s)
# s.discard('b')
# print(s)
# s.discard('b')
# print(s)
# s.pop()
# print(s)
# s.pop()
# print(s)
# # s.clear()
# print(s)
# print(2 in s)
# print(len(s))
#
# a = {1,2,3,6,9}
# b = {4,5,6,1,8}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a.issubset(b))
# result = list(a | b)
# print(result)

# print(hash('a'))
# print(hash(''))
# print(hash('[6,2]'))
#
# # print(hash([1,2]))     #列表可变不可哈希
# # print(hash([[1,2],6]]))   #列表不可哈希
#
# print(hash('dfc,eaf')) #字符串可以哈希
#
# print(hash((6,2)))          #元组可以哈希
# # print(hash(([66615,66],666)))     #元组中元素含有不可哈希值，元组变得不可哈希
#
# # print(hash({1,2,3}))    #集合不可哈希
#
# # print(hash({6:2,5:3}))  #字典不可哈希
#
# a = 5
# print(hash(a))      #a 指向不可变的整数，所以 hash(a) 合法（等价于 hash(5)）。
#
# b = [1,2]
# # print(hash(b))    # 指向可变的列表，所以 hash(b) 报错（等价于 hash([1, 2])）。


# a = {1,2,3}
# print(a)
# print(type(a))
#
# print(set((1,2,3,4,5)))  #等价于print({1,2,3,4,5})
# print(set([1,2,3,4,5]))
# print(set([1,'a',3,4,5]))
#
# print(set([(1,2),(3,4)]))
# # print(set(([1,2],[3,4])))     #不可哈希报错
#
# print(set([(1,2)+(3,4)+(4,5)]))

# print(set([(1, 2) , (2, 3),(1,2)])) #等价于print({(1, 2), (2, 3), (1, 2)})
# print(set([(1, 2)+ (2, 3)+(1,2)])) #等价于print({(1, 2) + (2, 3) + (1, 2)})
#
# print(set(((1, 2), (2, 3),(1,2)))) #等价于print({(1, 2), (2, 3), (1, 2)})
# print(set((1, 2)+ (2, 3)+(1,2)))


# endregion

# region 练习 5 字典dict

# stu = {'name':'lhl','age':18,'sex':'nan'},{'name':'lhl','age':18,'sex':'nan'}
# stu2 = [{'name':'lhl','age':18,'sex':'nan'},{'name':'lhl','age':18,'sex':'nan'}]
# # stu3 = {{'name':'lhl','age':18,'sex':'nan'},{'name':'lhl','age':18,'sex':'nan'}}
# print(stu)
# print(type(stu))
# print(stu2)
# print(type(stu2))
# # print(type(stu3))
# stu4 = (1,2)
# print(stu4)
# stu5 = (1,[2,3])
# print(stu5)
# print(type(stu5))


# d = {'name':'lhl','age':18}
# print(['name'])
# print(d['name'])
#
# print(d.get('name1',222))
# # print(d['nam1e'])
#
# d['sex'] = 'male'
# print(d)
#
# del d['name']
# print(d)
#
# d.pop('age')
# print(d)

# for key in d:
#     print(key)
# for value in d.values():
#     print(value)

# students = {0:'lhl',1:'jkl','ssx':18}
# print(students[0])
# print(students[1])
# print(students['ssx'])

# print({1:[1,2],3:4})    #不可哈希列表可作为值
# print({(1,2):1,3:4})    #可哈希元组可作为键
# # print({[1,2]:2,3:4})    #不可哈希列表不可作为键

# d = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7)
# print(d)

# base = {"name": "小明", "score": 80}
# extra = {"score": 95, "age": 18}
# result = base|extra
# print(result)
# result = {**base,**extra}
# print(result)
# base.update(extra)
# print(base)

# name = {1:{'name':'lhl','age':18}}
# print(name[1]['age'])
# print(name[1]['name'])

# scores = {'lhl':95,'ssx':100,'abc':66}
# jige = {name:score for name , score in scores.items() if score >= 90}
# print(jige)

# scores = {'lhl':95,'ssx':100,'abc':66}
# jige = {}
# for name,score in scores.items():
#     if score >= 90:
#         jige[name] = score  #注意 【name】 = score,因为是赋值操作，把值赋给键。右边不能是name
# print(jige)

# n = 0
# msg = {n:n**2 for n in range(9) if n%2==0}
# print(msg)

# endregion

# region 练习6 综合

print('##################################################【菜单】##################################################')
print('#1.添加学生信息\t2.修改学生信息\t3.删除学生信息\t4.查询学生信息\t5.列出所有学生\t6.统计班级成绩\t7.退出系统\t')
print('#########################################################################################################')

xueke = ("chinese", "math", "english")      #定义学科元组，不可修改

students = {}   #学生集合

while True:

    operate = input("请选择要执行的操作（1-7）：")

    if operate == '1':
        name = input('请输入学生姓名:')
        scores = {}  # 分数集合    ！！注意：scores = {} 写在 while 外面的话，两个学生共用了同一个成绩字典。会导致新增学生信息会修改之前的学生成绩信息

        for subject in xueke:
            scores[subject] = int(input(f"请输入 {subject} 的成绩："))

        students[name] = scores   #students新增key字段name，并将scores作为value值

        print(f'添加【{name}】成功')
        print(students)

    if operate == '2':
        name_change = input('请输入要修改的学生姓名：')
        if name_change not in students:
            print('您要修改的学生姓名不存在!')
        else:
            for subject in xueke:
                new_score = int(input(f'请输入修改后的{subject}成绩：'))
                students[name_change][subject] = new_score
        print(students[name_change])

    if operate == '3':
        name_del = input('请输入要删除的学生姓名：')
        if name_del not in students:
            print('您要删除的学生姓名不存在!')
        else:
            del students[name_del]
        print(students)

    if operate == '4':
        name_sel = input('请输入要查询的学生姓名：')
        if name_sel not in students:
            print('您要查询的学生姓名不存在!')
        else:
            print(students[name_sel])

    if operate == '5':
        print(students)

    if operate == '6':
        if not students:
            print('还没有学生')
        else:
            for subject in xueke:
                highest = max(scores[subject] for scores in students.values())
                lowest = min(scores[subject] for scores in students.values())
                high_names = []
                low_names = []

                for name,scores in students.items():
                    if scores[subject] == highest:
                        high_names.append(name)
                    if scores[subject] == lowest:
                        low_names.append(name)

                print(f"{subject} 最高分：{highest}，姓名：{'、'.join(high_names)}")
                print(f"{subject} 最低分：{lowest}，姓名：{'、'.join(low_names)}")

    if operate == '7':
        break

print('\n\n##################################################【菜单】##################################################')
print('#1.添加学生信息\t2.修改学生信息\t3.删除学生信息\t4.查询学生信息\t5.列出所有学生\t6.统计班级成绩\t7.退出系统\t')
print('#########################################################################################################')


# endregion