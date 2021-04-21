#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        prefix = [1]*n
        suffix = [1]*n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(0, n):
            res[i] = prefix[i] * suffix[i]
        return res

""" 
Accepted
20/20 cases passed (84 ms)
Your runtime beats 48.65 % of python3 submissions
Your memory usage beats 12.99 % of python3 submissions (20.8 MB)
"""

# nums = [1,2,3,4]
# res = Solution().productExceptSelf(nums)
# print(res)

# import numpy as np
# pro = np.cumproduct(nums)
# for i in range(len(nums)):
#     nums[i] = pro[-1] // nums[i]
# print(nums)

# @lc code=end

