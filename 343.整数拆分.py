#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
"""自己居然摸索出来了"""
# class Solution:
#     def integerBreak(self, n: int) -> int:
#         @cache
#         def f(x):
#             if x == 1 or x == 2:
#                 return 1
#             res = 0
#             for i in range(2, x):
#                 res = max(f(x-i)*i, res, (x-i)*i)
#             return res
#         return f(n)
"""
Accepted
50/50 cases passed (48 ms)
Your runtime beats 33.05 % of python3 submissions
Your memory usage beats 64.48 % of python3 submissions (14.8 MB)
"""
class Solution:
    def integerBreak(self, n):
        dp = [1] * (n+1)
        for i in range(3, n+1):
            for j in range(2, i):
                dp[i] = max(dp[i], dp[i-j]*j, (i-j)*j)
        return dp[n]
# s = Solution().integerBreak(11)
# print(s)
"""
Accepted
50/50 cases passed (36 ms)
Your runtime beats 91.63 % of python3 submissions
Your memory usage beats 81.34 % of python3 submissions (14.7 MB)
"""
# @lc code=end

