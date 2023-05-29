# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart

# class Dog:
#     classTrick = ["four feet", "tail"]

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []

#     def add_trick(self, trick):
#         self.tricks.append(trick)
    

# dannie = Dog("dannie")
# ana = Dog("ana")
# dannie.add_trick("jump")
# ana.add_trick("run")

# print(dannie.tricks)
# print(dannie.classTrick)

# print(ana.tricks)
# print(ana.classTrick)

# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)

#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)

#     __update = update   # private copy of original update() method

# class MappingSubclass(Mapping):

#     def update(self, keys, values):
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)


# mapping = Mapping([1,2,3])
# print(mapping)

import dis

# 建立一个类的过程：
'''
执行类的代码，会创建一个类对象，创建类的命名空间，最后创建类的对象。
需要三样东西：
1. 类的命名空间
2. 类的父类
3. 第三就是dictionary，类的属性 
这些信息共同构成了类对象，保存了类对象的信息。
'''

class Employee:
    name = 'AAA'
    
    def f(self):
        print(1)

# Employer = type('Employer', (), {'name': 'AAA', 'f': lambda self: print('I`m a employer')})
# a = Employer()
# a.f()

# python -m dis test.py 查看字节码

print('------------------')
class A:

    def classFunc(self):
        print('classFunc')

    def objFunc(self):
        print('objFunc')

o = A()

print(A.objFunc)
print(o.objFunc)


# slots
class B:
    __slots__ = ('name', 'age')

class C:
    pass

b = B()
c = C()
# print("B.__dict__", B.__dict__)
# print("C.__dict__", C.__dict__)

# 使用slot 时，会将类的属性存储在一个tuple中，tuple 中的元素是一个member descriptor，而不是dict中。
# print("b.__dict__", b.__dict__)
# print("c.__dict__", c.__dict__)




# super 是一个类，接收两个参数
class Animal:
    def __init__(self, age):
        self.age = age

class Person(Animal):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

class Male(Person):
    def __init__(self, age, name, gender):
        # super().__init__(age, name)
        Person.__init__(self,age, name)
        # super(Person, self).__init__(age, name)
        self.gender = gender

# super 接收两个参数，第一个参数是类，第二个参数是类的对象。
# 第一个类决定了 从MRO 链的那个位置开始找，
# 第二个决定了使用他的对象和MRO。

m = Male(30, "Robin","Male")
print(m.__dict__)
print(Male.mro())

# super 会根据MRO链，找到下一个类，然后调用下一个类的方法。
class A:
    def say(self):
        print('A')

class B(A):
    def say(self):
        # super().say()
        super(B, self).say()

class C(A):
    def say(self):
        print('C')

class D(B,C):
    def say(self):
        # super().say()
        B.say(self)

d = D()
d.say()


class E:
    def f(self):
        print('E')

    @staticmethod
    def g(x):
        print(x)

    @classmethod
    def h(cls, b):
        print(b)
    
e = E()
# print(e.f())
# print(e.g(1))

#
print(E.__dict__['g']) 
print(E.__dict__['h'])
''' 
<staticmethod object at 0x7f9b90229220> PyStaticMethod_Type PyType_Type（typeobject.c/4393）
<classmethod object at 0x7f9b90229250> LOAD_ATTR-> 

obj.property  和 cls.property 调用的是不同的方法

'''
