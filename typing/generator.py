
lst = [1,3,4,5]
g = (x for x in lst)
print(g)

# 
a = [1,2,3]
b = [4,5,6,7]
# c = zip(a, b)

d = [v + w for v, w in zip(a, b)]
for i in d:
    print(i)


# 打印杨辉三角
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]

from typing import Generator


def triangles():
    L = [1]
    yield
    while True:
        L = [v + w for v, w in zip(L + [0], [0] + L)]
        yield L

for i,row in enumerate(triangles()):
    print(row)
    if i == 10:
        break




