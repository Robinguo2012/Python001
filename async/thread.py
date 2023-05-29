import random
from threading import Thread
import time


def task(x):
    print('这是在',x)
    time.sleep(random.randint(1, 3))
    print('子线程结束')

if __name__ == '__main__':
    print('这是在主线程中')
    
    # 创建一个子线程
    t = Thread(target=task, args=('子线程',))
    t.start()
    t.join()
    time.sleep(0.3)
    print('主线程结束')

# https://docs.python.org/3/library/threading.html


