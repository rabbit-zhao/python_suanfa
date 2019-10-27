# -*- coding: utf-8 -*-
# @Author: zhr1030635594
# @Date:   2019-10-27 22:37:18
# @Last Modified by:   zhr1030635594
# @Last Modified time: 2019-10-27 23:14:17

import time

start = time.time()
arr1 = [1, 3, 4, 6, 10]
arr2 = [2, 5, 8, 11]
ans = arr1.copy()
ind = 0
for i in range(len(arr2)):
	while ind < len(arr1):
		if arr2[i] < arr1[ind]:
			arr1.insert(ind+i, arr2[i])  # 已经插入了i个，所以索引增加i
			break
		else:
			ind += 1
	else:               # while...else...如果while跳出，是因为条件false（ind>=len）执行else
		ans = ans + arr2[i:]
print(ans)
print(time.time()-start)