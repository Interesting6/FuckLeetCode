#
# @lc app=leetcode.cn id=1006 lang=python3
#
# [1006] 笨阶乘
#

# @lc code=start
class Solution:
    def clumsy(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 6
        res = 0
        r = n % 4
        for i in range(n, r, -4):
            if i == n:
                tmp = i * (i-1) // (i-2) + (i-3)
            else:
                tmp = -(i * (i-1) // (i-2)) + (i-3)
            res += tmp
        i = r
        if r == 1:
            res -= 1
        elif r == 2:
            res -= 2
        elif r == 3:
            res -= 6
        return res
"""
Accepted
84/84 cases passed (44 ms)
Your runtime beats 82.61 % of python3 submissions
Your memory usage beats 41.3 % of python3 submissions (14.9 MB)
"""
# s = Solution().clumsy(10)     
# @lc code=end

