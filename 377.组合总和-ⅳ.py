#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
# class Solution:
#     def combinationSum4(self, nums, target):
#         n = len(nums)
#         dp = [0]* (target+1)
#         dp[0] = 1
#         for i in range(1, target+1):
#             for j in range(n):
#                 if i - nums[j] >= 0:
#                     dp[i] += dp[i-nums[j]]
#         return dp[target]


# 2021-04-24 每日一题打卡
class Solution:
    def combinationSum4(self, nums, target):
        n = len(nums)
        res = 0
        from functools import lru_cache
        @lru_cache(None)
        def track_backing(tar):
            nonlocal res
            if tar == 0:
                return 1
            elif tar < 0:
                return 0
            else:
                sm = 0
                for i in range(n):
                    sm += track_backing(tar - nums[i])
                return sm
        res = track_backing(target)
        track_backing.cache_clear()
        return res

""" 回溯法
Accepted
15/15 cases passed (48 ms)
Your runtime beats 75.13 % of python3 submissions
Your memory usage beats 8.36 % of python3 submissions (15.1 MB)
"""

# @lc code=end

