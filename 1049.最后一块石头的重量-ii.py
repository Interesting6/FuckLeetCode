#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if not stones:
            return 0
        n = len(stones)
        sum_ = sum(stones)
        max_weight = sum_ // 2
        dp = [0] * (max_weight+1) # 一维背包，是否有子集数组，凑出重量和为i
        dp[0] = 1  # 选择
        for st in stones:
            for i in range(max_weight, st-1, -1):
                dp[i] = dp[i] or dp[i-st]
        # print(dp)
        i = max_weight
        while i > -1: # 要求最小的重量，即最大的i
            if dp[i]:
                return sum_ - 2 * i
            i -= 1
"""
Accepted
86/86 cases passed (52 ms)
Your runtime beats 94.25 % of python3 submissions
Your memory usage beats 89.91 % of python3 submissions (14.7 MB)
"""

# stones = [31,26,33,21,40]
# stones = [91]
# s = Solution().lastStoneWeightII(stones)
# print(s)


# @lc code=end

