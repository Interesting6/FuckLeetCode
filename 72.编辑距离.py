#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0]*(1+n2) for _ in range(1+n1)]
        for j in range(1+n2):
            dp[0][j] = j
        for i in range(1+n1):
            dp[i][0] = i
        for i in range(1, 1+n1):
            for j in range(1, 1+n2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    t = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    dp[i][j] = t + 1
        # print(dp)
        return dp[n1][n2]

# word1, word2 = "horse", "ros"
# word1, word2 = "intention", "execution"
# s = Solution().minDistance(word1, word2)
# print(s)
"""
Accepted
1146/1146 cases passed (188 ms)
Your runtime beats 36.26 % of python3 submissions
Your memory usage beats 60.87 % of python3 submissions (18.3 MB)
"""
# @lc code=end

