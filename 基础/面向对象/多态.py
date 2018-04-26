# !/usr/bin/env python

class F1(object):
    def show(self):
        print("F1")

class S1(F1):
    def show(self):
        print("S1")

class S2(F1):
    def show(self):
        print("S2")


def Func(obj):
    obj.show()

obj_s1 = S1()

obj_s2 =S2()

Func(obj_s1)
Func(obj_s2)