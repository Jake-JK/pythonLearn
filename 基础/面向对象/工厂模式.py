# !/usr/bin/env python

class Animal:
    def __init__(self):
        self.name = None
    def getName(self):
        return  self.name

class Cat(Animal):
    def __init__(self,name):
        self.name = name
        print("创建了一直叫%s的猫" % self.name)

    def __new__(cls, *args, **kwargs):

        return Animal.__new__(cls)
    def run(self):
        print("%s在跑" % self.name)

class Dog(Animal):
    def __init__(self,name):
        self.name = name
        print("创建了一直叫%s的狗" % self.name)
    def run(self):
        print("%s在跑")

class Factory:
    def creatAnimal(self,type,name):
        if type == "dog":
            return Dog(name)
        if type == "cat":
            return Cat(name)
f = Factory()
amy = f.creatAnimal("cat","amy")



