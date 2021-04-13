# @before-stub-for-debug-begin
from python3problem416 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
# 关键：背包容量为和的一半，物品价值和物品重量都是数组的元素。
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        n = len(nums)
        if sum_ % 2 != 0:
            return False
        weight = sum_ // 2 # 等和子集的和必然是总和一半
        dp = [[0]*(weight+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for w in range(1, weight+1):
                tmp = w - nums[i-1]
                if tmp < 0: # 放不下
                    dp[i][w] = dp[i-1][w]
                else:  # 第i个物品放得下
                    dp[i][w] = max(
                        dp[i-1][w], 
                        dp[i-1][tmp] + nums[i-1]
                    )
        if dp[n][weight] == weight:
            return True
        else:
            return False

# @lc code=end

