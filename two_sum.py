# -*- coding: utf-8 -*-
# @Time    : 2018/6/22 10:13
# @Author  : Martin

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]
"""
nums = [2, 7, 11, 15]
target = 9

import bisect

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        for j_index in range(len_nums):
            for k_index in range(j_index + 1, len_nums):
                if nums[j_index] + nums[k_index] == target:
                    return [j_index,k_index]


print(Solution().twoSum(nums, target))


