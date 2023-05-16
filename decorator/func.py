import time

# 函数装饰器-无参
# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         ret = func(*args, **kwargs)
#         end = time.time()
#         print('used:', end - start)
#         return ret
#     return wrapper


 
# print(foo(3))

# 函数装饰器-有参
def timeit(iter_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(iter_times):
                ret = func(*args, **kwargs)
            end = time.time()
            print('used:', end - start)
            return ret
        return wrapper
    return decorator

@timeit(1000)
def foo(x):
    return x * 2
# 相当于 foo = timeit(1000)(foo) 类似函数柯里化，接收一个参数，然后返回一个参数。执行一个函数的上下文中插入一特定的操作
print(foo(3))
