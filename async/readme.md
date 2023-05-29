# 事件循环机制

Python、JavaScript和OC 都有事件循环机制，这是一种异步编程的方式。
它们底层的实现都基于非阻塞IO和IO 多路复用。

## 事件循环机制的基本原理

从队列中取出事件，然后处理事件，处理完毕后再取出下一个事件，如此循环。

```
while True:
    events = get_events() # 获取事件列表
    for event in events:
        event.handle()
```

首先回顾一下操作系统的IO 模型。


## Python 的事件循环机制

Python 的事件循环机制是基于协程的，它的基本原理是：
