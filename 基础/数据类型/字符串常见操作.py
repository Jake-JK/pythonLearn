# !/usr/bin/env python

myStr = "hello world by ksunone"

"""
    问题：
        如何把 print("one.find('one')".ljust(60, "."), myStr.find(" ", 0, 5))  方法封装复用
        实现 func("one.find('one')") 就能打印出
        myStr.find('o')............................................. 4 
"""

"""
   find 检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1 （从左到右寻找）
   rfind 从右到左寻找
   mystr.find(str, start=0, end=len(mystr)) #范围区间  “左闭右开”
"""
print("myStr.find('o')".ljust(60, "."), myStr.find("o"))
# 在[0,5)的区间 寻找“ ”
print("one.find('one')".ljust(60, "."), myStr.find(" ", 0, 5))  # 找不到，返回 -1

"""
    index 跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
    一般用find 不用 index
    mystr.index(str, start=0, end=len(mystr)) 
"""
# print(myStr.indx("abc")) 找不到  报错 'str' object has no attribute 'indx'


"""
    count 返回 str在start和end之间 在 mystr里面出现的次数
    mystr.count(str, start=0, end=len(mystr))
"""
print('myStr.count("o")'.ljust(60, "."), myStr.count("o"))

"""
    replace 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
    mystr.replace(str1, str2,  mystr.count(str1))
"""
print("myStr.replace('o','0',myStr.count('o'))".ljust(60, "."), myStr.replace('o', '0', myStr.count('o')))

"""
    split 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
    mystr.split(str, maxsplit=2)
"""

print('myStr.split(" ")'.ljust(60, "."), myStr.split(" "))

"""
    capitalize 把字符串的第一个字符大写
    mystr.capitalize()
"""

print("myStr.capitalize()".ljust(60, "."), myStr.capitalize())

"""
    title 把字符串的每个单词首字母大写
"""
print("myStr.title()".ljust(60, "."), myStr.title())

"""
    startswith 检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False
    endswith 检查字符串是否是以 obj 结束, 是则返回 True，否则返回 False
    mystr.startswith(obj)
"""
print('myStr.startswith("hello")'.ljust(60, '.'), myStr.startswith("hello"))

"""
    lower 转换 mystr 中所有大写字符为小写
    mystr.lower()
"""
print("myStr.lower()".ljust(60, '.'), myStr.lower())

"""
    ljust 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
    rjust 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
    mystr.ljust(width) 
"""

"""
    center 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
"""

"""
    lstrip 删除 mystr 左边的空白字符
    rstrip 删除 mystr 字符串末尾的空白字符
    strip  删除mystr字符串两端的空白字符
"""

"""
    partition 把mystr以str分割成三部分,str前，str和str后  (从左到右)
    rpartition 从右到左
    mystr.partition(str)
"""
print("myStr.partition('o')".ljust(60, '.'), myStr.partition("o"))
print("myStr.rpartition('o')".ljust(60, '.'), myStr.rpartition("o"))

"""
    splitlines  按照行分隔(\n)，返回一个包含各行作为元素的列表
    mystr.splitlines()  
"""

print("'hello\nworld'.partition('by')".ljust(60, '.'), "hello\nworld".splitlines())

"""
    isalpha 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
    mystr.isalpha()
"""
print("'124aaa'.isalpha()".ljust(60, '.'), '124aaa'.isalpha())
print("'aaa'.isalpha()".ljust(60, '.'), 'aaa'.isalpha())

"""
    isdigit 如果 mystr 只包含数字则返回 True 否则返回 False.
    mystr.isdigit() 
"""
print("'124aaa'.isdigit()".ljust(60, '.'), '124aaa'.isdigit())
print("'123'.isdigit()".ljust(60, '.'), '123'.isdigit())

"""
    isalnum 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
    mystr.isalnum()
"""
print("'123.151'.isalnum()".ljust(60, "."), '123.151'.isalnum())
print("'123abc'.isalnum()".ljust(60, "."), '123abc'.isalnum())

"""
    isspace 如果 mystr 中只包含空格，则返回 True，否则返回 False.
    mystr.isspace()
"""
print("'123abc'.isspace()".ljust(60, "."), '123abc'.isspace())
print("'  '.isspace()".ljust(60, "."), '  '.isspace())

"""
    join mystr 中每个字符后面插入str,构造出一个新的字符串
    mystr.join(str)
"""
print('"_".join(myStr)'.ljust(60, "."), "_".join(myStr))
print('["hello", "world", "by", "ksunone"].join(myStr)'.ljust(60, "."), "/".join(["hello", "world", "by", "ksunone"]))


"""
    给定一个字符串aStr，返回使用空格或者'\t'分割后的倒数第二个子串
"""
print("给定一个字符串aStr，返回使用空格或者'\\t'分割后的倒数第二个子串", (myStr.split()))
print(myStr.rpartition("o"))