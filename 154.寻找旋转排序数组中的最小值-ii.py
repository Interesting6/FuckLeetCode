#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
"""
最小值右侧的数都小于等于nums[r]；
最小值左侧的数都大于等于nums[r]；
"""
class Solution:
    def findMin(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def bi_search(l, r):
            while l < r:
                m = l + ((r-l)>>1)
                if nums[m] < nums[r]: # nums[m]在最小值右侧
                    r = m # 缩小r到m
                elif nums[m] > nums[r]: # nums[m]在最小值左侧
                    l = m + 1 # 
                else:
                    r = r - 1
            return nums[l]
        res = bi_search(0, n-1)
        return res

# @lc code=end

