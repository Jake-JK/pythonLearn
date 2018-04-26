# !/usr/bin/env python
# -*- coding: utf-8 -*-

def test(num):
    print("111")
    def test_in(num_in):
        print(222)
        print(num + num_in)

    return test_in

a = test(30)
b = test(60)

print(id(a))
print(id(b))

