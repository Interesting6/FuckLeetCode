#
# @lc app=leetcode.cn id=664 lang=python3
#
# [664] 奇怪的打印机
#

# @lc code=start
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0]* n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1, -1, -1): # 注意必须是从后往前，
            # 因为dp[i,j]的计算要用到dp[i,k]与dp[k,j]，k>i在i行下面
            for j in range(i+1, n):
                if s[i] == s[j]: # 相等时，如aba，等于前一个ab
                    dp[i][j] = dp[i][j-1]
                else: # 不等时，如abab，等于a+bab, ab+ab, aba+b中最小的
                    min_val = float("inf")
                    for k in range(i, j):
                        t = dp[i][k] + dp[k+1][j]
                        min_val = min(min_val, t)
                    dp[i][j] = min_val
        res = dp[0][n-1]
        print(dp)
        return res

s = "abab"
x = Solution().strangePrinter(s)
print(x)

# @lc code=end

