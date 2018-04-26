# !/usr/bin/env python
class Dog:
    def __init__(self,new_name):
        self.name = new_name;
        self.__age = 0;
    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age


dog = Dog("join")

dog.set_age(18)
print(dog.get_age())
# print(dog.__age)
