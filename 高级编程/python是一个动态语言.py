# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    动态语言： 就是可以在代码运行时修改代码
    __slots__ ：  定义一个特殊的__slots__ ，限制class实例能添加的属性
"""
class Person(object):
    def  __init__(self,age,name):
        self.age = age;
        self.name = name;

k = Person(10,"ksun")

k.sex = "man"

print(dir(k))

def run(self):
    print("----%s在跑----"% self.name)

y = Person(18,"yey")

k.run = run
k.run(k)

print(dir(y))

