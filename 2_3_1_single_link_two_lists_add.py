# -*- coding: utf-8 -*-
# @Author: zhr1030635594
# @Date:   2019-10-28 01:09:30
# @Last Modified by:   zhr1030635594
# @Last Modified time: 2019-10-28 02:02:59
# 由两个列表组成的单链表

def printlist(listv, listr, head):   # 输出链表
	print(listv[head])
	next = listr[head]
	while next != -1:
		print(listv[next])
		next = listr[next]

listvalue = [1, 5, 6, 2, 7, 3]
listright = [3, 2, 4, 5, -1, 1]
head = 0
prepos = 3   # 要插入元素的上一个元素位置
printlist(listvalue, listright, head)
print()

listvalue.append(4)   # 添加新元素
listright.append(listright[prepos])   # 新元素对应的索引为上一个元素对应的索引
listright[prepos] = len(listvalue)-1    # 上一个元素的索引指向最后一个元素，即新添加的

printlist(listvalue, listright, head)
print()

prepos2 = 1
listright[prepos2] = listright[listright[prepos2]]
printlist(listvalue, listright, head)