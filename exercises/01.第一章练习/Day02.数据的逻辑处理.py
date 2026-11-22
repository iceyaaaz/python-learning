# region 练习1 if初体验


# # 成绩超过680就去清华
# score = int(input('输入成绩:'))
# if score >= 680:
#     print('上清华')

# endregion

# region 练习2 实现账号登陆1888888/666666

# user = int(input('请输入账号:'))
# pwd = input('请输入密码：')
# if user == 1888888 and pwd == '666666':
#     print('登陆成功')
# if user != 1888888 or pwd != '666666':
#     print('失败')

# endregion

# region 练习3 判断年份

# a = int(input('请输入年份：'))
#
# if a%100 != 0 and a%4 == 0 or a%100 == 0 and a%400 == 0:
#     print('闰年')
# else:
#     print('平年')

# endregion

# region 练习4 课后练习

# a = int(input('数字'))
# if a%2 ==1:
#     print('奇数')
# else:
#     print('oushu')

# account = input('请输入用户名：')
# pwd = input('请输入密码：')
#
# if account == 'admin' and pwd == '666888':
#     print('登陆成功')
# elif account == 'root' and pwd == '123':
#     print('登陆成功')
# else:
#     print('用户名或密码错误')





# endregion

# region 练习5 match case

# inp = input('请输入动作:')
# match inp:
#     case 'w'|'W':
#         print('角色向上跳跃')
#     case's' | 'S':
#         print('角色向下跳跃')
#     case'a' | 'A':
#         print('角色向左跳跃')
#     case'd' | 'D':
#         print('角色向右跳跃')
#     case'j' | 'J':
#         print('角色发动攻击')
#     case ' ':
#         print('角色隐身')
#     case'esc' | 'ESC':
#         print('角色退出游戏')
#     case _:
#         print('无效动作')







# endregion

# region 练习6 while循环

# i = 1
# while i<10:
#     i=i+1
#     print('人生苦短，我用python')
# else:
#     print('测试else输出')

# 计算1-100偶数和
# i = 1
# s = 0
# while i <= 100:
#     if i % 2 == 0:
#         s += i
#     i+=1
# else:
#     print(s)




# endregion

# region 练习7 for 循环

# msg = '人生苦短，我用python'
# # for i in msg:
# #     print(i,end = '')
# #     print('/',end = '')
# # else:
# #     print('结束')

# # 计算1-100奇数和
# i = 1
# s = 0
# for i in range(101):
#     if i % 2 == 1:
#         s += i
#     i += 1
# print(s)


# # 100-500所有3的倍数之和
# i = 100
# s = 0
# for i in range(100,501):
#     if i % 3 ==0:
#         s +=i
#     i += 1
# print(s)

# endregion

# region 练习8 嵌套循环

# m = int(input('输入m'))
# n = int(input('输入n'))
#
# for i in range(m):
#     for j in range(n):
#         print('*',end = '')
#     print()

# # 打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j} × {i} = {i*j}',end = '\t')
#     print()



# endregion

# region 练习9 综合练习


# while 1:
#     user = input('请输入用户名：').strip()
#     pwd = input('请输入密码：').strip()
#     if user == 'a' and pwd == '1' or user == 'b' and pwd == '2' or user == 'c' and pwd == '3':
#         print('登陆成功，进入首页')
#         break
#     if user == '' or pwd == '':
#         print('用户名和密码不能为空！')
#         continue  # 直接跳过本次循环，重新输入
#     else:
#         print('请重新输入，输入错误')


import random

import random

rand_num = random.randint(1, 100)

while 1:
    num = int(input("请输入你猜的数字："))
    if num == rand_num:
        print("猜对了")
        break
    elif num > rand_num:
        print("猜大了")
    else:
        print("猜小了")




# endregion





