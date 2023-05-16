
import sys
import fibo
import builtins
import sound.formats.echo as echo


# for n in range(10):
#     for x in range(2,n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         print(n, 'is a prime number')



def fib(n):
    """fibonacci 数列"""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# f100 = fib(100)
# print(f100)


def allAnimal(num, *animal, **keyvalues):
    """所有动物"""
    print('动物的数量是：', num)
    for i in range(len(animal)):
        print('动物的名称是：', animal[i])
    print('-'*40)
    for key in keyvalues:
        print(key, ':', keyvalues[key])

# allAnimal(3, '狗', '猫', '猪', 人='张三', 住址='北京市')


even = [2, 4, 6]
odd = [1, 3, 5]

newNums = [x*2 for x in odd]
print(newNums)

newTuple = [(x, y) for x in even for y in odd]
print(newTuple, len(newTuple))



matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

matrix_reverse = [[row[i] for row in matrix] for i in range(4)]
print("matrix", matrix_reverse)

# tuple 
t = 12345, 54321, 'hello!'
print(t)
x,y,z = t
print(x,y,z)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
arr = ['tac', 'toc', 'tie']

def testDict(dict):
    for k, v in dict.items():
        print(k, v)

def testArr(arr):
    for i, v in enumerate(arr):
        print(i, v)

testDict(knights)
testArr(arr)

num = fibo.fibo(10)
print('fibonaic >>', num)



# print(dir(fibo))
# print(dir(sys))
# print(dir(builtins))
print(dir())

echo.testPackage()


