# !/usr/bin/env python

# 定义 无序 不同元素组成 集合中元素必须是不可变类型
s = {1, 23, 3, 3, 3, 3,0}

print(s)
# s=set('hello')
# print(s)
#
# s=set(['alex','alex','sb'])
# print(s)

# s={1,2,3,4,5,6}

#添加
# s.add('s')
# s.add('3')
# s.add(3)
# print(s)

# s.clear()
# print(s)

# s1=s.copy()

s={'sb',1,2,3,4,5,6}
#随机删
# s.pop()

#指定删除
# s.remove('sb')
# s.remove('hellol') #删除元素不存在会报错
# s.discard('sbbbb')#删除元素不存在不会报错
# print(s)


python_l=['lcg','szw','zjw','lcg']
linux_l=['lcg','szw','sb']
p_s=set(python_l)
l_s=set(linux_l)
# #求交集
# print(p_s,l_s)
# print(p_s.intersection(l_s))
# print(p_s&l_s)
# #求并集
# print(p_s.union(l_s))
# print(p_s|l_s)
#差集
# print('差集', p_s-l_s)
# print(p_s.difference(l_s))
# print('差集', l_s-p_s)
# print(l_s.difference(p_s))
