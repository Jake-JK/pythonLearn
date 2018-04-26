# !/usr/bin/env python
# -*- coding: utf-8 -*-

# class Test:
#     def __init__(self):
#         self.__num = 100
#
#     def setNum(self,num):
#         self.__num = num
#
#     def getNum(self):
#         return self.__num
#     num = property(getNum,setNum)
#
#
# a = Test()
# a.num = 900
#
# print(a.num)


class Test:
    def __init__(self):
        self.__num = 100
    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num):
        self.__num = num


a = Test()
a.num = 900

print(a.num)
