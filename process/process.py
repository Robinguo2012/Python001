import multiprocessing
import os

print(os.getpid())

def f():
    print(os.getpid())

p = multiprocessing.Process(target=f)
p.start()
p.join()

class MyProcess(multiprocessing.Process):
    def run(self):
        f()

p = MyProcess()
p.start()
p.join()


