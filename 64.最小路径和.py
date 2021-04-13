#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
"""深度优先递归"""
# class Solution:
#     def minPathSum(self, grid) -> int:
#         m, n = len(grid), len(grid[0])
#         inf = float("inf")
#         dist = [[inf] * n for _ in range(m)]
#         # dist[0][0] = grid[0][0]
#         def dfs(x, y, cursum):
#             t = cursum + grid[x][y]
#             if t < dist[x][y]: # 比之前走过的路径要小，继续走下去
#                 dist[x][y] = t
#                 if x+1 < m:
#                     dfs(x+1, y, t)
#                 if y+1 < n:
#                     dfs(x, y+1, t)
#             else: # 比之前走过的路径和大，直接终止该路线
#                 return
#         dfs(0, 0, 0)
#         # from pprint import pprint
#         # pprint(dist)
#         return dist[m-1][n-1]


# li = [[1,3,1],[1,5,1],[4,2,1]] 
# s = Solution().minPathSum(li)
# print(s)
"""
Accepted
61/61 cases passed (7516 ms)
Your runtime beats 6.12 % of python3 submissions
Your memory usage beats 5.05 % of python3 submissions (16.7 MB)
"""


"""动态规划"""
class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        if m != 1:
            for i in range(m): # 左边界
                dp[i][0] = dp[i-1][0] + grid[i][0]
        if n != 1:
            for i in range(n): # 上边界
                dp[0][i] = dp[0][i-1] + grid[0][i]
        
        for i in range(1, m):
            for j in range(1, n): 
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                # 要么从左→右；要么从上↓下

        return dp[m-1][n-1]
"""
Accepted
61/61 cases passed (52 ms)
Your runtime beats 81.04 % of python3 submissions
Your memory usage beats 8.79 % of python3 submissions (16.5 MB)
"""

# @lc code=end

