# !/usr/bin/env python
# -*- coding: utf-8 -*-
import  copy
a = [1,2,3]
b = [4,5,6]

c = (a,b)

e = copy.copy(c)
f = copy.deepcopy(c)


print(id(c)," ---> id(c)")

print(id(e)," ---> id(e)")

print(c is e, " ---> c is e")
print(c is f, " ---> c is f")


"""
    结论：
        在copy模块中的copy，会识别copy的对象是可变类型，还是不可变类型，如果是不可变类型，就进行浅拷贝，反之进行第一层深拷贝。
"""
