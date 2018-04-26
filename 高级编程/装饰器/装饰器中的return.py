# !/usr/bin/env python
# -*- coding: utf-8 -*-

from time import ctime, sleep

def timefun(func):
    def wrappedfunc():
        print(1)
        print("%s called at %s"%(func.__name__, ctime()))
        return func()
    return wrappedfunc

@timefun
def foo():
    print("I am foo")

@timefun
def getInfo():
    return '----hahah---'

foo()
sleep(2)
foo()


print(getInfo())