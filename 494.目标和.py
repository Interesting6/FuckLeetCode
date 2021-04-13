# @before-stub-for-debug-begin
from python3problem494 import *
from typing import *
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

class Solution:
    def findTargetSumWays(self, nums, S):
        n = len(nums)

        @lru_cache(maxsize=1024*2)
        def f(k, t):
            if k == 1:
                return int(nums[0]==t) + int(-nums[0] == t)
            return f(k-1, t-nums[k-1]) + f(k-1, t+nums[k-1])
        res = f(n, S)
        return res
            
# import time
# s = Solution()
# time1 = time.time()
# res = s.findTargetSumWays([42,1,42,35,33,37,26,3,23,29,22,50,34,31,11,28,20,31,32,28], 2)
# print(res)
# print(time.time() - time1)


# @lc code=end

