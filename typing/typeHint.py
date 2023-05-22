
from typing import Sequence

def loop(seq: Sequence[int]):
    for i in seq:
        print(i)

loop([1,2,3]) # 
loop((1,3,5))

def f(a: int, b: int):
    return a+b


a = f(1,1)
print(a)

# Path: typing/typeHint.py



from typing import Callable

def my_fun(func: Callable[[int, int], int]):
    def wrapper(*args, **kwargs):
        print("Calling function: " + func.__name__)
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

@my_fun
def g(a: int, b: int)->int:
    return a+b

print(g(1, 3))

from typing import Optional

ReturnType = tuple[int, Optional[str]]

def error_handling(a) -> ReturnType:
    if a > 0:
        return (1, None)
    else:
        return (0, "Error")
    
errorCode, errorMessage = error_handling(1)
print(errorCode, errorMessage)

from typing import NewType

UserId = NewType('UserId', int)
AttactPoint = NewType('AttactPoint', int)

class Player:

    def __init__(self,uid: UserId, attackPoint: AttactPoint):
        self.uid = uid
        self.attackPoint = attackPoint

    def setAtk(self,atk: AttactPoint):
        self.attackPoint = atk

player = Player(UserId(1), AttactPoint(100))

        
