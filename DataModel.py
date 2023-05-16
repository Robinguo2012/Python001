import numbers
from typing import Any, Self

num = int(20)
numF = float(20.0)

print(numF)

def add(a, b):
    '''===This is a function to add two numbers==='''
    return a+b

# func is a function object
print(add.__module__)
print(add.__doc__)
print(add.__dict__)

class Foo:


    @staticmethod
    def f():
        print("static method")

    def __init__(self, name) -> None:
        self.name = name
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        print("set attr", __name, __value)
        super().__setattr__(__name, __value)

    def __getattribute__(self, __name: str) -> Any:
        print("get attr", __name)
        return super().__getattribute__(__name)
    
    def __delattr__(self, __name: str) -> None:
        print("del attr", __name)
        super().__delattr__(__name)

foo = Foo("dannie")
foo.age = 20
# del foo.age
# print(foo.name)

# 特殊属性
# print(foo.__dict__)
# print(foo.__class__)
# Foo.f()


# 基本定制
class Human:

    x = 0
    foo = None

    # 类方法，创建一个类对象
    def __new__(cls, name, age) -> Self:
        print("new")
        return super().__new__(cls)
    
    # 实例方法，初始化一个实例对象
    def __init__(self,name, age):
        print("init")
        self.name = name
        self.age = age
        # super.__init__(self)

    def __str__(self) -> str:
        return "Human: name: {}, age: {}".format(self.name, self.age)
    
    def __repr__(self) -> str:
        return "Human: name: {}, age: {}".format(self.name, self.age)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("call")
        print(args)
        print(kwds)
        return "call return"
    
    def __len__(self) -> int:
        return 100
    
    def instance_method(self, a, b):
        return a+b

    @classmethod
    def class_method(cls, a, b):
        cls.x = a+b

    @staticmethod
    def static_method(a, b):
        return a+b
    
    def __hash__(self) -> int:
        return hash((self.name, self.age))
    
    # def __bool__(self) -> bool:
    #     return self.name == 

    def __getattribute__(self, __name: str) -> Any:
        print("get attr", __name)
        return super().__getattribute__(__name)

    def __get__(self, instance, owner=None):
        print("get object", instance, owner)

    def __set__(self, instance, owner=None):
        print("set object", instance, owner)

    

human = Human('dannie', 20)
a = human.instance_method(1, 2)
human.foo = foo
print('instance method', a)

Human.class_method(1, 2)
print('class method', Human.x)

res = Human.static_method(10, 2)
print('static method', res)

# f = 'test get {}'.format(res.age)
# print(f)

# metaclass
class LowercaseAttrMetaClass(type):
    def __init__(cls, name, bases, attr):
        for attr_name in attr:
            if not attr_name.startswith("__"):
                # print("attr_name>>>", attr_name)
                if not attr_name.islower():
                    raise ValueError('属性名 {attr_name} 必须为小写')
        super().__init__(name, bases, attr)
        

class LowercaseAttrClass(metaclass=LowercaseAttrMetaClass):
    valid_attr = 1
    # Invalid_Attr = 2

object = LowercaseAttrClass()
print(object.valid_attr)  # 输出: This is valid
# print(object.Invalid_Attr)  # 输出: This is Invalid


## 通过内置方法模拟容器类型

# 通过内置方法模拟数字类型

from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')


class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)

