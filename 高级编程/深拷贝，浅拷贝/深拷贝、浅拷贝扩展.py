# !/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
a = [11, 22, 33]
b = [55, 44]

c = [a, b]

print(c,"--->c")   # [[11, 22, 33], [55, 44]] --->c

a.append(66)
print(c,"--->c")  #[[11, 22, 33, 66], [55, 44]] --->c


d = copy.deepcopy(c)
print(d,"--->d") #[[11, 22, 33, 66], [55, 44]] --->d

b.append(666)
print(d,"--->d") #[[11, 22, 33, 66], [55, 44]] --->d



isinstance()