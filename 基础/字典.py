# 字典 dict
dict
info = {
    "name": "json",
    "age": 88,
    "k3": False,
    "k1": True,
    "k2": "yes",
    "tuple": (11, 22, 33),
    "k4": {
        "kk1": "vv1",
        "kk2": "vv2"
    }
}

#  删除
# del info["k1"]

# 遍历
# for item in info.keys():
#     print(item)
#
# for item in info.values():
#     print(item)
#
# for k, v in info.items():
#     print(k, v)
# print(info)

dic = {
    "k1": 123,
    "k2": 333
}
# 根据数列创建字典
# v = dict.fromkeys(["11", 33, 8, 66], 123)
# v = dict.fromkeys(["11", 33, 8, 66])
# print(v)
# dict.get 根据Key获取值 key不存在时 可指定默认值（None）
# print(dic.get("111"))
# print(dic["k1"], dic.get("k1"))

# 移除字典中指定的值。并返回删除的值
# v = dic.pop("k1", "如果键值不存在则返回此句")
# 随机删
# v = dic.popitem()
# print(v)

# 设置值
# 已存在，不设置，获取当前key对应值
# 不存在，设置，获取设置的值
# v = dic.setdefault("k333",888)

print(dic)
