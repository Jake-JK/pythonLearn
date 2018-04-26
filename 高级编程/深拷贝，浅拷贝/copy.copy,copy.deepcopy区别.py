# !/usr/bin/env python
# -*- coding: utf-8 -*-

import  copy
a = [1,2,3]
b = [4,5,6]

c = [a,b]

print(c, "---> c = [a,b]")

e = copy.copy(c)

print(e , "---> e = copy.copy(e)")

f = copy.deepcopy(c)

print(f, "---> f = copy.deepcopy(c)")

print(id(c),"---> id(c)")
print(id(e),c is e,"---> id(e), c is e")
print(id(f),c is f,"---> id(f), c is f")

a.append(8888)

print(e,"e---> a.append(8888)")
print(f,"f---> a.append(8888)")

print(e[0] is a,"---> e[0] is a")
print(f[0] is a,"---> f[0] is a")