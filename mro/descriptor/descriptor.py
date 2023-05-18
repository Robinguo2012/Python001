from typing import Union
import logging


logging.basicConfig(level=logging.INFO)

# log 描述器的功能单一，只是为了记录属性的访问和修改。对于不同的目的，需要定义不同的描述器。
class LoggedAgeAccess:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        value = getattr(instance, self.private_name)
        logging.info('Accessing %s giving %s', self.public_name, value)
        return value
    
    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)
        logging.info('Updating %s to %s', self.public_name, value)


class Person:
    age = LoggedAgeAccess()
    name = LoggedAgeAccess()

    def __init__(self, name, age):
        # 被赋值给self.name, self.age 时，会调用__set_name__方法
        self.name = name
        self.age = age

    def brithday(self):
        self.age += 1

pete = Person('Pete', 34)
dannie = Person('Dannie', 30)

'''
pete {'_name': 'Pete', '_age': 34}
person {'public_name': 'name', 'private_name': '_name'}

1. descriptor 点语法（a.b）进行属性查找时调用，间接查找不会触发描述器。
2. descriptor 只有类变量才会起作用，实例变量不会触发。
3. descriptor 主要作用是提供一个钩子，可以在属性被访问时执行一些操作。

属性访问的默认行为是从一个对象的字典中获取、设置或删除属性。对于实例来说，
a.x 的查找顺序会从 a.__dict__['x'] 开始，然后是 type(a).__dict__['x']，
接下来依次查找 type(a) 的方法解析顺序（MRO）。 
如果找到的值是定义了某个描述器方法的对象，
则 Python 可能会重写默认行为并转而发起调用描述器方法。
这具体发生在优先级链的哪个环节则要根据所定义的描述器方法及其被调用的方式来决定。

. 语法的访问顺序：
要记住的重要点是：

# 描述器由 __getattribute__() 方法调用。

# 类从 object，type 或 super() 继承此机制。

# 由于描述器的逻辑在 __getattribute__() 中，因而重写该方法会阻止描述器的自动调用。

# object.__getattribute__() 和 type.__getattribute__() 会用不同的方式调用 __get__()。前一个会传入实例，也可以包括类。后一个传入的实例为 None ，并且总是包括类。

# 数据描述器始终会覆盖实例字典。

# 非数据描述器会被实例字典覆盖。
# '''
print("pete", vars(pete))
print("person name", vars(vars(Person)['name']))

dannie.brithday()
print(dannie.age)

# # 验证器类
from abc import ABC, abstractmethod

class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass

class OneOf(Validator):
    def __init__(self, *options):
        self.options = set(options)
    
    def validate(self, value):
        if value not in self.options:
            raise ValueError(f'Expected {value!r} to be one of {self.options!r}')

class Number(Validator):

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be an int or float')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Expected {value!r} to be at least {self.min_value!r}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'Expected {value!r} to be no more than {self.max_value!r}')
        

s: Union[int, str] = [2,3,3]

# print('联合类型', s)

class String(Validator):

    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Expected {value!r} to be a str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f'Expected {value!r} to be at least {self.minsize} chars')        
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f'Expected {value!r} to be no more than {self.maxsize} chars')
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f'Expected {self.predicate} to be True for {value!r}')

class Component:
    name = String(minsize=3, maxsize=10, predicate=str.isupper)
    kind = OneOf('wood', 'metal', 'plastic')
    quantity = Number(min_value=0)

    def __init__(self, name, kind, quantity):
        self.name = name
        self.kind = kind
        self.quantity = quantity

c = Component('SEA', 'wood', 10)
print(c.name, c.kind, c.quantity)

import sqlite3


conn = sqlite3.connect('example.db')

# import os

# print(os.getcwd())
# with sqlite3.connect('./example.db') as conn:
#     # 创建游标对象
#     print("Opened database successfully")

#     cursor = conn.cursor()
#     # 查询所有表名
#     # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

#  # 执行SQL语句
#     conn.execute('''CREATE TABLE COMPANY
#            (ID INT PRIMARY KEY     NOT NULL,
#            NAME           TEXT    NOT NULL,
#            AGE            INT     NOT NULL,
#            ADDRESS        CHAR(50),
#            SALARY         REAL);''')
#     conn.commit()
    # 获取查询结果
    # tables = cursor.fetchall()


    # 打印所有表名
    # for table in tables:
    #     print("打印表名称：", table[0])

    # cursor.close()
    







class Field:

    def __set_name__(self, owner, name):
        self.fetch = f'SELECT {name} FROM {owner.table} WHERE {owner.key} = ?;'
        self.store = f'UPDATE {owner.table} SET {name} = ? WHERE {owner.key} = ?;'

    def __get__(self, obj, objtype=None):
        return conn.execute(self.fetch, [obj.key]).fetchone()[0]
    
    def __set__(self, obj, value):
        conn.execute(self.store, [value, obj.key])
        conn.commit()
    
# cib = type(conn)
# a = type('A',(), {'name': 'AAA'})

class Movies:
    key = 'title'
    table = 'movies'
    director = Field()
    year = Field()

    def __init__(self, key):
        self.key = key

class Songs:
    key = 'title'
    table = 'songs'
    artist = Field()
    year = Field()

    def __init__(self, key):
        self.key = key

# m = Movies('The Matrix')
# print("电影：", m.director, m.year)

conn.close()


print('------------------')
class A:

    def classFunc(self):
        print('classFunc')

    def objFunc(self):
        print('objFunc')

o = A()

print(A.objFunc)
print(o.objFunc)

# function object 和 method object 的关系
'''
在类中定义一个方法，执行类的code object 时会生成一个function object。
通过类实例化一个instance 时，通过instance.method()调用时，通过mro 查找方法时会找到类的function object。
他是一个function object descriptor 有一个func_descr_get，返回一个method object。
他是一个结构体对象，保存了function object 和 instance 的引用。
这个过程就是绑定一个方法的过程。
'''

