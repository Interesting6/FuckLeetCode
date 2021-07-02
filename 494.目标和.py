# @before-stub-for-debug-begin
# from python3problem494 import *
# from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
from functools import lru_cache

# def cache(func):
#     cache_dict = {}
#     def warpper(*args, **kwargs):
#         if args in cache_dict:
#             return cache_dict[args]
#         else:
#             res = func(*args, **kwargs)
#             cache_dict[args] = res
#         return res
#     return warpper

# class Solution:
#     def findTargetSumWays(self, nums, S):
#         n = len(nums)

#         @lru_cache(maxsize=1024*2)
#         def f(k, t):
#             if k == 1:
#                 return int(nums[0]==t) + int(-nums[0] == t)
#             return f(k-1, t-nums[k-1]) + f(k-1, t+nums[k-1])
#         res = f(n, S)
#         return res
            
# class Solution:
#     def findTargetSumWays(self, nums, targes):
#         n = len(nums)
#         dp = [[0]*(targes+1) for _ in range(n+1)]
#         for i in range(1, n+1):
#             for j in range(1, targes+1):
#                 t1 = j - nums[i-1] if j - nums[i-1] >= 0 else 0
#                 t2 = j + nums[i-1] if j + nums[i-1] <= targets else 0
#                 dp[i][j] = dp[i-1][t1] + dp[i-1][t2]
#         res = dp[n][targes]
#         return res

# 202s1-06-07，用0-1背包刷。。。没刷出来，记忆化递归到过了。。。
# class Solution:
#     def findTargetSumWays(self, nums, targets):
#         n = len(nums)
#         @lru_cache(2048)
#         def f(ta, i):
#             if i == n-1:
#                 return int(ta == nums[i]) + int(ta == -nums[i])
#             return f(ta-nums[i], i+1) + f(ta+nums[i], i+1)
#         res = f(targets, 0)
#         return res

import time
s = Solution()
time1 = time.time()
nums = [42,1,42,35,33,37,26,3,23,29,22,50,34,31,11,28,20,31,32,28]; targets = 2
# nums = [1, 1, 1, 1, 1]; targets = 3
res = s.findTargetSumWays(nums, targets)
print(res)
print(time.time() - time1)
"""
Accepted
138/138 cases passed (688 ms)
Your runtime beats 20.37 % of python3 submissions
Your memory usage beats 8.26 % of python3 submissions (20.6 MB)
"""

# @lc code=end

