#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [0] * n
        min_stock = float("inf")
        for i,prs in enumerate(prices):
            min_stock = min(min_stock, prs)
            diff = prs - min_stock
            dp[i] = max(dp[i-1], diff)
        return dp[-1]

# s = Solution().maxProfit([2, 4, 1])
# print(s)
# @lc code=end

