# -*- coding: utf-8 -*-
# @Author: zhr1030635594
# @Date:   2019-10-29 22:58:13
# @Last Modified by:   zhr1030635594
# @Last Modified time: 2019-10-29 23:31:32

nums = [3, 4, 5, 7, 10]
def twoSum(nums, target):
	res = []  # 存放结果编号
	newnums = nums.copy()   
	newnums.sort()  # 排序
	left = 0   # 左指针
	right = len(newnums) - 1   # 右指针

	while left < right:    
		if newnums[left] + newnums[right] == target:    # 相等
			for i in range(len(newnums)):    # 储存left下标
				if nums[i] == newnums[left]:
					res.append(i)
					break
			for i in range(len(newnums)-1, -1, -1):   # right
				if nums[i] == newnums[right]:
					res.append(i)
					break
			break
		elif newnums[left] + newnums[right] < target:   # left右移
			left += 1
		elif newnums[right] + newnums[left] > target:   # right左移
			right -= 1

	return(res[0]+1, res[1]+1)

print(twoSum(nums, 11))

def twoSumHash(nums, target):
	dict = {}
	for i in range(len(nums)):
		m = nums[i]
		if target-m in dict:   # 直接判断的是键
			return(dict[target-m]+1 , i+1)
		dict[m] = i

print(twoSum(nums, 11))