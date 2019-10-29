# -*- coding: utf-8 -*-
# @Author: zhr1030635594
# @Date:   2019-10-29 23:58:31
# @Last Modified by:   zhr1030635594
# @Last Modified time: 2019-10-30 00:11:55
wordpartten= [3, 3, 2, 2]
input = "hello hello hi hi"

def wordPattern(wordpartten, input):
	word = input.split()     # 单词由空格分开
	if len(word) != len(wordpartten):    # 长度不一样，肯定不对
		return False
	Hash = {}     # 记录模式字符串与目标字符串匹配
	Used = {}	  # 记录已经用过的字符串都哪些
	for i in range(len(word)):   # 遍历
		if wordpartten[i] in Hash:   # 如果匹配在HASH里了
			if Hash[wordpartten[i]] != word[i]:   # 是不是那个单词
				return False
		else:     # HASH没这个匹配
			if word[i] in Used:    # 这个单词是不是新单词，若已经被用过了，不能两个匹配对应一个单词
				return False
			else:    # 添加
				Hash[wordpartten[i]] = word[i]
				Used[word[i]] = True
	return True

print(wordPattern(wordpartten, input))