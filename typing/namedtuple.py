
from collections import namedtuple

# 本质上也是生成了一个Point class
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

print(p._asdict())
x,y = p
print(x,y)

l = [1,2,4]
t = (1,2,5)

l[1] = 2
# t[0] = 2 # error




