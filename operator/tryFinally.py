import atexit

try:
    print("acquire resource")
    a = 1/0
except ZeroDivisionError:
    print("exception")
finally:
    print("release resource")

atexit.register(lambda :print("exit"))

