
# module 是一个独立的命名空间，它本身就是一个python object。还能包含其他python object。
# module 通常是一个.py文件，但也可以是一个包含python object的任何文件。
# module 是一个运行时概念，一般一个文件对应一个module，当通过import 引入一个文件时，才会动态生成一个module。
# 
import sys


# import 引用module 时首先从缓存中找，没找到才去从sys.path中找。
# import sound as formats

# if __name__ == '__main__':
#     if __package__ is None:
#         import sys
#         from os import path
#         sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
#         from sound import formats
#     else:
#         from ..sound import formats

from ..sound.formats import echo as echo

print(echo)
print(sys.path)
