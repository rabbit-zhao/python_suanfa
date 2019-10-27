# -*- coding: utf-8 -*-
# @Author: zhr1030635594
# @Date:   2019-10-27 23:42:05
# @Last Modified by:   zhr1030635594
# @Last Modified time: 2019-10-27 23:50:52

numbers = [1, 3, 5, 6, 7, 8, 13, 14, 15, 17, 18, 24, 30, 43, 56]
head, tail = 0, len(numbers)   # 数组长度为最后下标值+1
search = int(input())

while tail - head > 1:   # 头尾间无元素
	mid = (tail + head) // 2
	if search < numbers[mid]:
		tail = mid
	elif search > numbers[mid]:
		head = mid + 1
	elif search == numbers[mid]:
		ans = mid
		break
else:    # 只剩head一个元素
	if numbers[head] == search:
		ans = head
	else:
		ans = -1   # 没找到
print(ans)
