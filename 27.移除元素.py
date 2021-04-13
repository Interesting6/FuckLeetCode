# @before-stub-for-debug-begin
from python3problem27 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
"""双指针法"""
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         n = len(nums)
#         j = 0 # 慢指针
#         for i in range(n): # 快指针
#             if nums[i] != val:
#                 nums[j] = nums[i] # i,j的互换也可以，主要是把i的值赋给j
#                 j += 1
#             # 否者与给定值相等，快指针i跳过该元素

#         return j


# 2021.03.19 第二次做
class Solution:
    def removeElement(self, nums, val):
        fp = 0
        sp = 0
        for fp in range(len(nums)):
            if nums[fp] != val:
                nums[fp], nums[sp] = nums[sp], nums[fp]
                sp += 1
        return sp
# @lc code=end

