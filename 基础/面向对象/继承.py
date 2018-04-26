# !/usr/bin/env python
# 创建一个父类

class People(object):
    def __init__(self, name, height=170):
        self.color = "yellow"
        self.height = height
        self.name = name

    def say(self):
        print("hello,i am %s " % self.name)


class Man(People):
    def run(self):
        print("跑")

    def setName(self, newName):
        self.name = newName

    def setheight(self, height):
        self.height = height


y = Man("ksun")
y.say()
y.setName("ksunone")
y.say()