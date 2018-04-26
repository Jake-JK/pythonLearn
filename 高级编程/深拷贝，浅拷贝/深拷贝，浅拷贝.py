# !/usr/bin/env python
# -*- coding: utf-8 -*-

a = [11,22,33]
b = a  #浅拷贝  指向同一个内存地址。

print(id(a) == id(b)) #true
print(id(a))
print(id(b))

import copy

 #深拷贝  内容相同，但重新开辟一个新内存，内存地址不同。

c = a.copy()
print(id(a) == id(c)) #False
print(id(a))
print(id(c))



from collections import Iterator

print(isinstance((x for x in range(10)),Iterator))