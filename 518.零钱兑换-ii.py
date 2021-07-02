#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        n = len(coins)
        for i in range(1, n+1): # 遍历物品
            for j in range(coins[i-1], amount+1): # 遍历背包
                dp[j] += dp[j - coins[i-1]]
        print(dp)
        res = dp[amount]
        return res

amount = 5; coins = [1, 2, 5]
s = Solution().change(amount, coins)
print(s)
"""
Accepted
28/28 cases passed (156 ms)
Your runtime beats 65.26 % of python3 submissions
Your memory usage beats 87.44 % of python3 submissions (14.9 MB)
"""

# @lc code=end

