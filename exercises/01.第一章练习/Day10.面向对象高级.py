
# 多继承
class A:
    print('a')
    def a(self):
        print('1')
class B:
    print('b')
    def a(self):
        print('2')
class C(A,B):
    pass
c = C()
c.a()
c.a()
