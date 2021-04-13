#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        flag = 1
        for i in range(m):
            if obstacleGrid[i][0]: # 有障碍后，后面都是0，不能过去
                flag = 0
            dp[i][0] = flag
        flag = 1
        for i in range(n):
            if obstacleGrid[0][i]:
                flag = 0
            dp[0][i] = flag

        if obstacleGrid[0][0]:
            dp[0][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]: # 当前位置无障碍
                    if not obstacleGrid[i-1][j] and not obstacleGrid[i][j-1]:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    elif obstacleGrid[i-1][j] and not obstacleGrid[i][j-1]:
                        dp[i][j] = dp[i][j-1]
                    elif not obstacleGrid[i-1][j] and obstacleGrid[i][j-1]:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = 0
                else:
                    dp[i][j] = 0
        return dp[m-1][n-1]
# @lc code=end

