
# try:
#     skdmv
#     # print(0)
# except NameError as e:
#     print(1)
#     print(e)
# else:
#     print(2)
# finally:
#     print(3)

class Students:
    def __init__(self,name,age,abc):
        self.sex = 10        #sex = 10 是局部变量，这部分理解对了。写成 self.sex = 10 后，它叫实例属性，保存在 self 指向的那个对象上。
        self.name=name
        self.age=age
    def Introduce(self):
        print(f'我叫{self.name},今年{self.age},{self.sex}')
s1 = Students('lhl',18)
s2 = Students('ssx',15)
s1.Introduce()
s2.Introduce()
