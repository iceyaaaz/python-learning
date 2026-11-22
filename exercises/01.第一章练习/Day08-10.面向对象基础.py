from operator import add


# class Calculator:
#     x = 1
#     y = 20
#     def add(self,a,b):
#         self.q = self.x+self.y*2
#         # return self.q
#
#     def add2(self):
#         self.add(0,0)
#         w = self.q + 666
#         return w
#
#     # @staticmethod
#     # def sub(a,b):
#     #     # e = self.q +1  #@staticmethod用不到实例属性和类属性
#     #     return a-b
#
#     @classmethod
#     def Cls(cls,a,b):
#         r = Calculator.x + Calculator.y +a+b#可以用类属性
#         # t = self.q +1   #用不到实例属性
#         print(r)
#         cls.x = 999
#         print(cls.x)


# c = Calculator()
#
# print(c.add2())
# print(c.q)
# d = Calculator()
# d.Cls(5,6)
# print(c.add2())

# a = Calculator()
# print(a.x)
# a.Cls(1,2)
# print(a.x)

# class Car:
#     pass
# car1 = Car()
# car1.name = 'lhl'
# car1.age = 18
# car1.sex = 'nan'
# print(car1.__dict__)

# class Car:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
# car1 = Car(2000,1,2)
# print(car1.year,car1.month,car1.day)
# car1.month = 12
# print(car1.year,car1.month,car1.day)

# class A:
#     def x(self):
#         self.num1 = 10
#     def y(self):
#         self.num2 = 10
#
# q = A()
# print(q.num1 == q.num2)

# # ========
# class A:
#     b = 1
#     def __init__(self,a):
#         self.a = a
#     def First(self):
#         self.a = self.a + 1
#         self.b = self.b + 10
#         # A.b+=10       #这样 b 的变化才由所有实例共享。
#         # A.a+=10       用类名.属性名，属性必须是类属性不能是实例里面定义的属性。但是用实例名.属性名就可以用实例里面的属性
#         print(self.a,self.b)
#     def Second(self):
#         self.a = self.a - 100
#         self.b = self.b - 100
#         print(self.a,self.b)
# a1 = A(1)
# a1.First()  #2,11
# a1.Second() #-98,-89
# a1.First()  #-97,-79
# a2 = A(1)
# a2.First()
# a2.Second()
#
# print(a1.a,a1.b)    #实例名.属性名  可以正常访问
# print(A.b)          #类名.属性名，属性在类里面不是实例新定义的属性可以正常访问，对于a不在类里则不可访问
# print(a2.a,a2.b)
# # print(A.a)        #用类名.属性名，属性必须是类属性不能是实例里面定义的属性。但是用实例名.属性名就可以用实例里面的属性
#
# a1.b = 666          #只给a1新建了实例属性b = 666，类A.b不变
# print(a1.b)         #666
# print(A.b)          #1
# # ==========

# a = int(input(':'))
# if a>5:
#     print('yichang')
#
# b = int(input(':'))
# if b>5:
#     raise ValueError('yichang')

# 封装 _   __   property
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#     @property
#     def Name(self):
#         return self.name
#     def deposit(self,amount):
#         self.balance +=amount
#         # print(self.name,"deposited",amount)
#     def withdraw(self,amount):
#         if amount >=self.balance:
#             raise ValueError('余额不足')
#         self.balance -= amount
#         print(self.name,"withdrawn",amount)
# a1 = BankAccount('lhl',100)
# # a1.deposit(10)
# # a1.withdraw(20)
# # print(a1.balance)
# print(a1.Name)

# class Person:
#     def __init__(self, name, age,sex):
#         self.name = name      # 公开变量
#         self._age = age       # 保护变量（约定不随便访问）
#         self.__sex = sex
#
#     def _internal_method(self):
#         print("这是一个内部方法")
#
#     def __Sex(self):
#         print('这是一个私有方法，不可调用')
#
# p = Person("张三", 25,'male')
# print(p.name)        # ✅ 正常访问：张三
# print(p._age)        # ⚠️ 能访问，但不建议（编辑器可能会给出警告）：25
# # print(p.__sex)       #不能调用
# p._internal_method() # ⚠️ 能调用，但不建议
# # p.__Sex()            #私有方法



# # 继承
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name}发出声音")
# class Dog(Animal):
#     def speak(self):
#         print(f'{self.name}汪汪汪')
# class Cat(Animal):
#         pass
# Dog('狗狗').speak()
# Cat('咪咪').speak()


# # super
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Dog(Animal):
#     def __init__(self,name,age,sex):
#         super().__init__(name,1)
#         self.sex = sex
#     def __str__(self):
#         return f'{self.name} is {self.age} years old {self.sex}'
#
# d = Dog('lhl',1,'male')
# print(d)
# print(isinstance(d,Dog))
# print(isinstance(d,Animal))

# # 多态
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name}发出声音")
# class Dog(Animal):
#     def speak(self):
#         print(f'{self.name}汪汪汪')
# class Cat(Animal):
#     pass
# animals = [Dog('www'),Cat('MMM')]
# for animal in animals:
#     animal.speak()

# # 类方法和静态方法
# class Student:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count += 1
#
#     @classmethod
#     def get_count(cls):            # 第一个参数是类本身 cls
#         return cls.count
#
#     @staticmethod
#     def is_pass(score):            # 没有 self 和 cls，就是放在类里的普通函数
#         return score >= 60
#
# Student("小明")
# Student("小红")
# print(Student.get_count())      # 2
# Student.is_pass(75)      # True
