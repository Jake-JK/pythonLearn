# !/usr/bin/env python

a= [x for x in range(1,101)]
b = [a[x:x+3] for x in range(0,100,3)]


print(a)
print(b)