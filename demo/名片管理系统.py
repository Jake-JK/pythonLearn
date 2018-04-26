# !/usr/bin/env python
import os
import json

MUNE = [
    "添加一个新的名片",
    "删除一个名片",
    "修改一个名片",
    "查询一个名片",
    "显示所有名片",
    "退出系统"
]
LIST_HEAD = ("姓名", "电话", "qq")

# 创建文件
if os.path.exists("card.json"):
    old_card = open("card.json", "r")
    _card = old_card.read()
    card = json.loads(_card)
else:
    old_card = open("card.json", "w")
    card = []
    save_card()
old_card.close()


# 保存写入文件
def save_card():
    f = open("card.json", "w")
    data = json.dumps(card)
    f.write(data)
    f.close()


# 打印功能目录
def print_mune():
    print("=" * 50)
    print("\t名片管理系统 V0.01")
    for index, item in enumerate(MUNE):
        print(index + 1, item)
    print("=" * 50)


# 增加名片
def add_card():
    new_card = {}
    new_card["name"] = input("请输入姓名：")
    new_card["phone"] = input("请输入电话号码：")
    new_card["qq"] = input("请输入qq：")
    card.append(new_card)
    save_card()


# 根据姓名删除名片
def del_card():
    global card
    d_name = input("请输入要删除的姓名：")

    for item in card:
        print(item, d_name)
    # filter返回的对象只能使用一次，使用后销毁。
    new_card = filter(lambda x: x['name'] != d_name, card)
    # print(list(new_card))
    card = list(new_card)
    # print("card", card)

    # card = list(filter(lambda x: x['name'] != d_name, card))
    save_card()


# 根据姓名修改名片
def updata_card():
    global card
    u_name = input("请输入需要修改的姓名:")
    F = filter(lambda x: x["name"] == u_name, card)
    # 判断输入的姓名是否存在
    if not any(list(F)):
        print('您输入的姓名不存在')
        return
    # 定位
    # return
    # print(card.index(list(F)[0]))
    F = filter(lambda x: x["name"] == u_name, card)
    position = card.index(list(F)[0])
    # 打印需要修改的项目
    print("=" * 50)
    print("\t请选择修改项目")
    for index, item in enumerate(LIST_HEAD):
        print(index + 1, item)
    print("0 退出")
    print("=" * 50)
    u_num = input("请输入对应的号码：")
    print(u_num)
    if not (u_num.isdigit()):
        return False
    else:
        print("---------")
        u_num = int(u_num)
        if u_num == 1:
            card[position]["name"] = input("请输入名字：".rjust(20, "-"))
        if u_num == 2:
            card[position]["phone"] = input("请输入电话号码：".rjust(20, "-"))
        if u_num == 3:
            card[position]["qq"] = input("请输入qq".rjust(20, "-"))
        save_card()


# 显示所有名片
def show_all():
    global card
    s = "%s \t %s \t %s" % tuple(map(lambda x: x.ljust(15), LIST_HEAD))
    print(s)
    for item in card:
        print("%s \t %s \t %s" % tuple(map(lambda x: x.ljust(15), item.values())))


# 根据输入姓名搜索名片
def src_card():
    name = input("请输入要搜索的姓名：")
    src_return = list(filter(lambda x: x["name"] == name, card))
    s = "%s \t %s \t %s" % tuple(map(lambda x: x.ljust(15), LIST_HEAD))
    print(s)
    for item in src_return:
        print("%s \t %s \t %s" % tuple(map(lambda x: x.ljust(15), item.values())))


# 入口
def main():
    print_mune()

    while True:
        num = input("请输入操作号码:")

        if not num.isdigit():
            continue
        if int(num) <= 0 | int(num) > len(MUNE):
            print("请输入1到6范围的号码")
            num = input("请输入操作号码:")
            continue
        else:
            num = int(num)
            print(MUNE[num - 1])
            if num == 1:
                add_card()
            if num == 2:
                del_card()
            if num == 3:
                updata_card()
            if num == 4:
                src_card()
            if num == 5:
                show_all()
            if num == 6:
                show_all()


main()
