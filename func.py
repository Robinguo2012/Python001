# 0. 位置参数
def power(x):
    return x * x

# 1. 可变参数
def add_num(*numbers):
    sum = 0
    # 此处numbers为元组 
    print(type(numbers))
    for n in numbers:
        sum += n * n
    return sum

# 可以把list 或者tuple 当做可变参数传入
numbers = [1,3,4,5]
print(add_num(*numbers))

print(add_num(1, 2, 3, 4, 5))
print(add_num())

# 2. 关键字参数
# def person(name, age, **kw):
#     print('name', name, 'age', age, 'other', kw)

# person('Michael', 30)
# person('Bob', 35, gender='M', city='Beijing')

def person(name, age, *, city, job):
    print(name, age, city, job)

# 命名关键字参数
person('Jack', 24, city='Beijing', job='Engineer')

# 3. 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=10, *args, **kw):
    print(a, b, c, args, kw)

f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 10, x=99)

print('---------------------')

def f2(a, b, *, d, **kw):
    print(a, b, d, kw)

f2(1, 2, d=99, ext=None)

def f3(*args, **kw):
    print(args, kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f3(*args, **kw)
