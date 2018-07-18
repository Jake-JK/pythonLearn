# !/usr/bin/env python
# -*- coding: utf-8 -*-

from time import ctime, sleep

def timefun(func):
    def wrappedfunc(*args, **kwargs):
        print("%s called at %s"%(func.__name__, ctime()))
        func(*args, **kwargs)
    return wrappedfunc

@timefun
def foo(*args,**kwargs):
    print(args)
    if kwargs:
        print(kwargs(0))

foo({"name":123})
sleep(2)
foo(2,4,9)