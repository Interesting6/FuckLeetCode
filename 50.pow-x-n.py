#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def f(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            m = n >> 1
            t = f(m)
            if n & 1:
                return x*t*t
            else:
                return t*t
        if n >= 0:
            res = f(n)
        else:
            res = 1 / f(-n)
        f.cache_clear()
        return res
"""
Accepted
304/304 cases passed (44 ms)
Your runtime beats 38.38 % of python3 submissions
Your memory usage beats 50.08 % of python3 submissions (14.9 MB)
"""

# @lc code=end

