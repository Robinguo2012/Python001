import inspect
from objprint import op

def f():
    frame = inspect.currentframe()
    # op(
    #     frame,
    #     honor_existing=False,
    #     depth=2
    # )
    # print(frame.f_back.f_code.co_name)
    # print(frame.f_back.f_locals)
    print(frame.f_back.f_code.co_filename)
    print(frame.f_back.f_lineno)


def g():
    a = 1
    name = 'robin'
    f()

g()



