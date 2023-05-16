
import dis

# def f(a, b, * ,c=10, **kw):
#     pass

# code = f.__code__


# print(code.co_argcount)
# print(code.co_posonlyargcount)
# print(code.co_kwonlyargcount)

# def f(a):
#     # b = a
#     b = a.attr
#     b = a.method()
#     return b

# 编译期被编译为code object，是imuutable 对象
def f(a):
    c = 1
    d = {}
    def g():
        d['a'] = 1
        pass
    return g

code = f(2).__code__

dis.dis(f)

print('------------------')
# 局部变量的数量
print(f'nlocals : {code.co_nlocals}')

# 局部变量
print(f'varnames : {code.co_varnames}')

# 保存方法中的所有string
print(f'names : {code.co_names}')

# freevars 引用了其他scope 中的变量
print(f'freevars : {code.co_freevars}')

# cellvars 当前的scope 的变量在别的scope中被引用
print(f'cellvars : {code.co_cellvars}')


# 常量
print(f'consts : {code.co_consts}')