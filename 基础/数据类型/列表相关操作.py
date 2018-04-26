# !/usr/bin/env python"

v = ["hello", "world", 1024]
"""
    添加元素
    append,extent,insert
    通过append可以向列表添加元素
    通过extend可以将另一个集合中的元素逐一添加到列表中
    insert(index, object) 在指定位置index前插入元素object
"""

v.append("ksunone")
print(v)
v.extend([3, 2, 1])
print(v)
v.insert(2, "insert")
print(v)

"""
    修改元素
    修改元素的时候，要通过下标来确定要修改的是哪个元素，然后才能进行修改
"""
v[2] = '666'
print(v)

"""
    查找元素 in, not in, index, count
    所谓的查找，就是看看指定的元素是否存在
    python中查找的常用方法为：
        in（存在）,如果存在那么结果为true，否则为false
        not in（不存在），如果不存在那么结果为true，否则false
"""


"""
    删除元素("删"del, pop, remove)
    del：根据下标进行删除
    pop：删除最后一个元素
    remove：根据元素的值进行删除
"""
del v[2]
print(v)
s =v.pop()
print(v,s)
v.remove(1024)
print(v)