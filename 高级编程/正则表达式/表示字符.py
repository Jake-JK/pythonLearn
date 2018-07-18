# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    .	匹配任意1个字符（除了\n）
    [ ]	匹配[ ]中列举的字符
    \d	匹配数字，即0-9
    \D	匹配非数字，即不是数字
    \s	匹配空白，即 空格，tab键
    \S	匹配非空白
    \w	匹配单词字符，即a-z、A-Z、0-9、_
    \W	匹配非单词字符

"""

import re;

#匹配任意一个
# ret = re.match(".","123");
# print(ret.group())


"""
    Python中字符串前面加上 r 表示原生字符串
"""
mm = "c:\\a\\b\\c"
# print(mm)
# print(re.match(r"c:\\a",mm).group())


#表示数量
"""
    *	匹配前一个字符出现0次或者无限次，即可有可无
    +	匹配前一个字符出现1次或者无限次，即至少有1次
    ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
    {m}	匹配前一个字符出现m次
    {m,}	匹配前一个字符至少出现m次
    {m,n}	匹配前一个字符出现从m到n次
"""

# bb = "ksunone"
# ret = re.match("[a-z]?",bb).group()
# print(ret)

ret = re.match("[a-zA-z0-9]{4,20}@163.com{1}","abcad@163.com").group()
print(ret)

"""
    ^	匹配字符串开头
    $	匹配字符串结尾
    \b	匹配一个单词的边界
    \B	匹配非单词边界
"""


"""
    |	匹配左右任意一个表达式
    (ab)	将括号中字符作为一个分组
    \num	引用分组num匹配到的字符串
    (?P<name>)	分组起别名
    (?P=name)	引用别名为name分组匹配到的字符串
"""