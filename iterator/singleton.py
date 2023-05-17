
'''
实现单例有几种方法，讨论一下
1. 使用函数装饰器
'''

def singleton(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@singleton    
class Foo(object):
    def __init__(self):
        pass

foo1 = Foo()
foo2 = Foo()
print("函数装饰器单例：", id(foo1) == id(foo2))


# 2. 类装饰器实现单例
class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
           self._instance[self._cls] = self._cls(*args, **kwargs)
        return self._instance[self._cls]

@Singleton
class Bar:

    def __init__(self,name):
        self.name = name

bar1 = Bar('bar1')
bar2 = Bar('bar2')
print('类装饰器单例:', id(bar1) == id(bar2))

# bar2.name = 'bar3'

# print('类装饰器单例:', bar1.name, bar2.name)

# 3. 使用new 方法创建单例

class Single(object):

    _instance = None
    
    ## new 是一个类方法，创建一个对象
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
    

single1 = Single()
single2 = Single()
print("使用new 创建单例：", id(single1) == id(single2))

        

# 4. 使用metaclass 创建单例
def func(self):
    print('do something')

# 使用type 创建一个类
Klass = type('Klass', (), {'func': func})
c = Klass()
c.func()

class Singleton1(type):
    _instance = {}

    # 它作为一个元类，调用new 方法返回一个类
    def __new__(cls, *args, **kw):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton1, cls).__call__(*args, **kw)
        return cls._instance[cls]
    
class Foo2(metaclass=Singleton1):
    pass

o1 = Foo2()
o2 = Foo2()
print("使用metaclass 创建单例：", id(o1) == id(o2))








