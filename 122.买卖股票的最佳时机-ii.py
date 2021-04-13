#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        memo = [-1] * n
        def dp(start):
            if start >= n:
                return 0
            if memo[start] != -1:
                return memo[start]
            res = 0
            min_stock = float("inf")
            for sell in range(start, n):
                min_stock = min(min_stock, prices[sell])
                earn = prices[sell] - min_stock
                res = max(res, earn+dp(sell+1))
            memo[start] = res
            return res
        return dp(0)
# @lc code=end

