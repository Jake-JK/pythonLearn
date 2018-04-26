# !/usr/bin/env python

# def name(name):
#     print(name)
#
# name(name="kk")

# 高阶函数 1。函数接收的参数是一个函数名  2#返回值中包含函数
# 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
# 把函数当作参数传给另外一个函数
# def foo(n): #n=bar
#     print(n)
#
# def bar(name):
#     print('my name is %s' %name)
#
# # foo(bar)
# # foo(bar())
# foo(bar('alex'))

# 返回值中包含函数
# def bar():
#     print('from bar')
# def foo():
#     print('from foo')
#     return bar
# n=foo()
# n()
# def hanle():
#     print('from handle')
#     return hanle
# h=hanle()
# h()

# map函数 https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000
# num_l = [1, 2, 10, 5, 3, 7]
# name = "ksunone"
# def map_test(array):
#     ret = []
#     for i in num_l:
#         ret.append(i**2)
#     return ret
#
# v = map(lambda x:x+1,num_l)
# v = map(lambda x:x.upper(),name)
# print(list(v))

# filter 函数
# movie_people = ['alex_sb', 'mik_sb', 'ksunoneb']
# v = filter(lambda x: 'sb' not in x, movie_people)
# print(list(v))

# reduce 函数


# from functools import reduce
# num_l = [1, 2, 3, 4, 5, 100]
# v = reduce(lambda x,y:x+y, num_l)
# print(v)


# 小结
# map 处理序列中的每个元素，得到的记过是一个“列表”，该“列表”元素个数及位置与原来一样
# filter 遍历序列中的每个元素，判断每个元素得到的布尔值，如果是true则留下来。
# reduce 处理一个序列，然后把序列进行合并操作。

p = [
    {"name": "mike", "age": 80},
    {"name": "ksun", "age": 18},
    {"name": "amy", "age": 60}
]


w = filter(lambda x : x["age"] <= 18, p)
print(list(w))