# !/usr/bin/env python

f = open("test.txt","rb+")

# one_read = f.read(3)
# print("读出的数据-->"+ one_read)
#
# print( "当前读写的位置-->", f.tell())
#
# print("再次读写的数据-->" + f.read(3))
#
# print( "当前读写的位置-->", f.tell())


str = f.read(10)
print("读取的数据是 : ", str)

# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)

# 重新设置位置
f.seek(-3, 2)

# 查找当前位置`
position = f.tell()
print("当前文件位置 : ", position)


f.close()