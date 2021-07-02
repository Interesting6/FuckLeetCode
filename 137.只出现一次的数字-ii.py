#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        di = {}
        for i in nums:
            if di.get(i, 0):
                di[i] += 1
            else:
                di[i] = 1
        res = [i for i in di if di[i]==1][0]
        return res
"""
Accepted
14/14 cases passed (52 ms)
Your runtime beats 32.81 % of python3 submissions
Your memory usage beats 22.14 % of python3 submissions (16.1 MB)
"""

# @lc code=end

