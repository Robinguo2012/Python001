class makeHtmlTagClass:

    def __init__(self, tag, css_class=''):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
            if css_class != '' else ''
        
    def __call__(self, fn):
        def wrapped(*args, **kwds):
            return "<" + self._tag + self._css_class +  ">" \
            + fn(*args, **kwds) + "</" + self._tag + ">"
        return wrapped

# 通过这种方式生成的装饰器，可以传递参数。可以扩展为一个html 生成器
@makeHtmlTagClass(tag='b', css_class='bold_css')
@makeHtmlTagClass(tag='i', css_class='italic_css')
def hello(name):
    return "Hello, {}".format(name)

print(hello("Hao"))


from inspect import getmembers, getargs, ismethod, getfullargspec, currentframe
from functools import wraps

def wraps_decorator(f):
    @wraps(f)
    def wraps_wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wraps_wrapper
class SomeClass(object):
    @wraps_decorator
    def method(self, x, y):
        pass

def getTrueArgs(obj):
    for name, func in getmembers(obj, predicate=ismethod):
        print('member name: ', name)
        print('member func: ', func)        
        print('member func args: ', getfullargspec(func)[0])

obj = SomeClass()
getTrueArgs(obj)


# 缓存

def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args, **kwargs)
            cache[args] = result
        return result
    return wrapper

@memo
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
    
from collections.abc import Callable

# register route
class MyApp(object):
    def __init__(self):
        self.func_map:dict[str, Callable] = {}
    
    def register(self, name):
        def func_wrapper(func):
            self.func_map[name] = func
            return func
        return func_wrapper
    
    def call_method(self, name='default'):
        func = self.func_map.get(name, None)
        if func is None:
            raise Exception('No function registered against - ' + str(name))
        return func()
    
app = MyApp()

@app.register('/')
def main_page_func():
    return 'This is the main page'

@app.register('/other')
def other_page_func():
    return 'This is some other page'

print(app.call_method('/'))
print(app.call_method('/other'))


    

# function logger

import inspect
import time

# DRY(Don't repeat yourself) 原则，提取了一个函数，用于打印函数的基本信息
def advance_logger(log_level):

    def _get_num_line():
        frame = inspect.currentframe()
        if frame is not None:
            return frame.f_back.f_back.f_lineno # type: ignore
    
    def _basic_log(fn, result, *args, **kwds):
        print("function name: ", fn.__name__)
        print("arguments args: {0}, {1} ".format(args, kwds))
        print("return result: {}".format(result))

    def _info_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwds):
            result = fn(*args, **kwds)
            _basic_log(fn, result, *args, **kwds)
            return result
        return wrapper
    
    def _debug_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwds):
            ts = time.time()
            result = fn(*args, **kwds)
            te = time.time()
            _basic_log(fn, result, *args, **kwds)
            print("function called at line: {}".format(_get_num_line()))
            print("function execution time: {}".format(te - ts))
            return result
        return wrapper
    
    if log_level == 'info':
        return _info_log_decorator
    else:
        return _debug_log_decorator
    
@advance_logger(log_level='logger')
def add(x, y):
    return x + y

print(add(1, 2))



        
        