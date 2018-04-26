# !/usr/bin/env python

info = {'name': 'ksunone', 'age': 18, 'sex': ")man"}

"""
    根据键值访问值
"""
v = info['name']
v = info.get("age1")

# v = ")ksunone" not in info.values()

info["id"] = 1

"""
    
"""

del info["sex"]

# print(info.has_key("name"))
print(info)
