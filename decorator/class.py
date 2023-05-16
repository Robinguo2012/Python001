import time
from typing import Any

# 装饰器类-无参
# class Timer:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         start = time.time()
#         ret = self.func(*args, **kwds)
#         end = time.time()
#         print('used:', end - start)
#         return ret
    


# 装饰器类-有参
class Timer:
    def __init__(self, prefix):
        self.prefix = prefix
    
    def __call__(self, func) -> Any:
        def inner_wrapper(*args, **kwargs):
                start = time.time()
                ret = func(*args, **kwargs)
                end = time.time()
                print(self.prefix, end - start)
                return ret
        return inner_wrapper
    

@Timer(prefix='current-time')
def foo(x):
    return x * 2

print(foo(3))

# 类装饰器-输入一个类输出一个类。
def add_str(cls):
    def __str__(self):
        return str(self.__dict__)
    cls.__str__ = __str__
    return cls

@add_str
class MyObject:
    def __init__(self, a, b):
         self.a = a
         self.b = b

obj = MyObject(1,2)
print('object desc >> ', obj)


        