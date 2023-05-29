
import asyncio

'''
三个对象
1. coroutine
2. task
3. future

coroutine: 协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
task: 任务，它是对协程对象的进一步封装，包含了任务的各个状态。
future: 代表将来执行或没有执行的任务的结果。它和task上没有本质上的区别

coroutine 不能直接运行，只有通过await 隐式变成了task对象，才能被调用执行。

'''

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print("started at", asyncio.get_running_loop().time())

    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    print("task1", task1)
    print("task2", task2)

    await task1
    await task2

    print("finished at", asyncio.get_running_loop().time())

asyncio.run(main())


