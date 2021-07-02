#
# @lc app=leetcode.cn id=879 lang=python3
#
# [879] 盈利计划
#

# @lc code=start
from typing import List
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = (10**9+7)
        length = len(profit)
        dp = [[[0]*(minProfit+1) for _ in range(n+1)] for _1 in range(length+1)]
        dp[0][0][0] = 1
        for i in range(1, length+1): # 第i-1个工作
            member = group[i-1]
            earn = profit[i-1]
            for j in range(n+1): # 第j-1个员工，注意从0开始
                for k in range(minProfit+1): # 至少利润
                    if j < member:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - member][max(0, k - earn)]) % MOD
        res = 0
        for j in range(0, n+1):
            res = (res + dp[length][j][minProfit]) % MOD
        return res    
        # total = sum(dp[length][j][minProfit] for j in range(n + 1))
        # return total % MOD
        

# @lc code=end

