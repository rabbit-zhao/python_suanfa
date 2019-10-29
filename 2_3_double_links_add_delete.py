# -*- coding: utf-8 -*-
# @Author: zhr1030635594
# @Date:   2019-10-28 16:59:03
# @Last Modified by:   zhr1030635594
# @Last Modified time: 2019-10-28 17:17:57

listvalue = [1, 5, 6, 2, 7, 3]
listright = [3, 2, 4, 5, -1, 1]
listleft = [-1, 5, 1, 0, 2, 3]
head = 0
prepos = 5

def printlist(listv, listr, head):
	print(listv[head])
	next = listr[head]
	while next != -1:
		print(listv[next])
		next = listr[next]

printlist(listvalue, listright, head)
print()

listvalue.append(4)
listleft.append(prepos)
listright.append(listright[prepos])
listright[prepos] = len(listvalue)-1
listleft[listright[len(listvalue)-1]] = len(listvalue)-1

printlist(listvalue, listright, head)
print()

listright[prepos] = listright[listright[prepos]]
listleft[listright[listright[prepos]]] = prepos

printlist(listvalue, listright, head)
print()