# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
     装饰器(decorator)功能
        引入日志
        函数执行时间统计
        执行函数前预备处理
        执行函数后清理功能
        权限校验等场景
        缓存
"""

from time import  ctime,sleep

def timefun(func):
    def wrappedfunc():
            print("%s called at %s"%(func.__name__, ctime()))
            func()
    return wrappedfunc

@timefun
def foo():
    print("I am foo")

foo()
sleep(2)
foo()