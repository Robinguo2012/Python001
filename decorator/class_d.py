
class Decorators:
    
    def log_function(func):
        def wrapper(*args, **kwargs):
            print(f'function start')
            print(f"args: {args}")
            ret = func(*args, **kwargs)
            print(f'function end')
            return ret
        return wrapper
    
    @log_function
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
        
    log_function = staticmethod(log_function)

d = Decorators()

@d.log_function
def f():
    pass

@Decorators.log_function
def g():
    pass

f()
g()


    
