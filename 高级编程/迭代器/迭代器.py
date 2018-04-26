# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    可以被newt() 函数调用并不断返回下一个值的对象成为迭代器，Iteraror.
    可以使用instance() 判断一个对象是否是Iterator 对象。
"""

from collections import Iterator


a = ((x for x in range(10)))
# print(isinstance(a,Iterator))

print(next(a))


"""
    把list dict str 等 Iterable  变成 Iterator 可以使用 iter() 函数
    
"""

b = iter("abc")

print(isinstance(b,Iterator))



"""
    凡是可作用于for循环的对象都是Iterable类型；

    凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
    
    集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

    Python的for循环本质上就是通过不断调用next()函数实现的
"""