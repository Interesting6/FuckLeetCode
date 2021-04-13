# @before-stub-for-debug-begin
from python3problem283 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 快速排序思想：一个左指针左边维护非零元素，一个右指针左边维护0
        n = len(nums)
        l = r = 0
        for r in range(n):
            if nums[r] != 0 and r!=l:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        # n = len(nums)
        # i = n-1
        # j = n-1
        # while j >= 0:
        #     if nums[j] == 0:
        #         k = j
        #         while k < i:
        #             nums[k], nums[k+1] = nums[k+1], nums[k]
        #             k += 1
        #         i -= 1
        #     j -= 1
        # 太慢了

# @lc code=end

