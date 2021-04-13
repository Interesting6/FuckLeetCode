# @before-stub-for-debug-begin
from python3problem202 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        di = {str(i):i**2 for i in range(10)}
        vis = set()
        while n not in vis:
            if n == 1:
                return True
            vis.add(n)
            n = str(n)
            res = 0
            for c in n:
                res += di[c]
            n = res
        return False
"""Accepted
402/402 cases passed (48 ms)
Your runtime beats 43.96 % of python3 submissions
Your memory usage beats 24.6 % of python3 submissions (14.9 MB)"""
# @lc code=end

