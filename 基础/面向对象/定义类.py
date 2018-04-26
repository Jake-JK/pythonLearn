# !/usr/bin/env python

class Car:
    def __init__(self):
        self.wheelNum = 5
        self.color = "ye6low"
        self.__name = "BMW"
    # def __str__(self):
    #     msg = "hello"
        # return msg
    def getCarInfo(self):
        print("轮子个数%d,颜色%s" %(self.wheelNum,self.color))

    def move(self):
        print("移动")

carOne = Car()

carOne.wheelNum = 4
carOne.color = "yellow"
carOne.getCarInfo()

carTwo = Car()
carTwo.getCarInfo()
print(carTwo.color)