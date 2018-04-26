# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from collections import Iterator

def gensquares(N):
    for i in range(N):
        yield i ** 2

a = gensquares(5)
b = gensquares(6)

print(isinstance(a,Iterator))
print(isinstance(b,Iterator))

print(next(a))
print(next(b))
print(next(a))
print(next(b))
print(next(a))
print(next(b))

print(list(a))
print(list(b))

a = (x ** 3 for x in  range(5))
print(a)
print(next(a))
print(next(a))
print(list(a))

