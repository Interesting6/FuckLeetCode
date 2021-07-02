#
# @lc app=leetcode.cn id=1269 lang=python3
#
# [1269] 停在原地的方案数
#

# @lc code=start
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 1e9+7
        m = steps
        n = min(steps, arrLen)
        dp = [[0]*(n) for _ in range(m)] # i步走到j处的方案数
        dp[0][0] = 1
        for i in range(1, m):
            for j in range(n):
                if j-1 < 0: # 左边靠墙，不能从墙左边走到右边当前位置了
                    # 第i步停留 + 第i步向左走
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j+1]) % mod
                elif j+1 >= n: # 右边靠墙，不能从墙右边走到左边当前位置了
                    # 第i步停留 + 第i步向右走
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % mod
                else:
                    # 向右 + 停留 + 向左
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % mod
        res = (dp[m-1][0] + dp[m-1][1]) % mod # i-1在0处到i时不动 + i-1在1处向左

        return int(res)
                
# s = Solution().numWays(2, 4)
# print(s)
"""
Accepted
31/31 cases passed (452 ms)
Your runtime beats 39.51 % of python3 submissions
Your memory usage beats 28.39 % of python3 submissions (24.2 MB)
"""  

# @lc code=end

