# !/usr/bin/env python

import os

file = open("test.txt","r")
# print(file.read(3))


print(file.readline())
print(file.readline())
file.close()

