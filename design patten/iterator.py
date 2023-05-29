

arr = [1,2,4]

for i in arr:
    print(i)

'''
要区分两个概念
iterable: 可迭代对象，可以通过iter()函数转换为iterator, 也可以通过for循环遍历。它没有状态。

iterator: 迭代器，可以通过next()函数获取下一个元素，它持有关联的容器的当前访问的状态。
'''


