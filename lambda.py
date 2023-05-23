import sound.formats.echo as echo
import sys

fun = lambda a, b: a +b
print(fun(2, 1))

arr = [1,30, 2, 5, 6]
res = sorted(arr, key=lambda x: x % 2 == 0)

print(res)


print(echo)
print("search path",sys.path)