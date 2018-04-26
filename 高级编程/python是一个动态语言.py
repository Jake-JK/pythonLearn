# !/usr/bin/env python
# -*- coding: utf-8 -*-
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