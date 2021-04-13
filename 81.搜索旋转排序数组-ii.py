# @before-stub-for-debug-begin
from python3problem81 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
# class Solution:
#     def search(self, nums, target: int) -> bool:
#         n = len(nums)
#         nums = set(nums)
#         return target in nums
""" 直接用python的特性。。。
Accepted
279/279 cases passed (36 ms)
Your runtime beats 88.05 % of python3 submissions
Your memory usage beats 95.1 % of python3 submissions (15 MB)
"""

class Solution:
    def search(self, nums, target):
        n = len(nums)
        if n == 1:
            return nums[0] == target
        break_point = -1
        for i in range(1, n):
            if nums[i-1]>nums[i]:
                break_point = i
                break
        def bi_search(l, r):
            while l <= r:
                mid = l + ((r-l) >> 1)
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    return True
            return False
        if break_point == -1:
            return bi_search(0, n-1)
        left = bi_search(0, break_point-1)
        right = bi_search(break_point, n-1)
        return left or right
"""
Accepted
279/279 cases passed (40 ms)
Your runtime beats 71.97 % of python3 submissions
Your memory usage beats 49.24 % of python3 submissions (15.3 MB)
"""
# @lc code=end

