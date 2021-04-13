#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#

# @lc code=start
import pprint
class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])
        def bury(i, j):
            grid[i][j] = 1
            for r,c in [(i-1, j), (i+1,j), (i, j+1), (i, j-1)]:
                if 0<=r<m and 0<=c<n and grid[r][c] == 0:
                    bury(r, c)
            
        for i in range(m):
            if grid[i][0] == 0:
                bury(i, 0)
            if grid[i][-1] == 0:
                bury(i, n-1)
        for j in range(n):
            if grid[0][j] == 0:
                bury(0, j)
            if grid[-1][j] == 0:
                bury(m-1, j)
        # pprint.pprint(grid)

        res = 0
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    bury(i, j)
                    res += 1
        return res

# grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# s = Solution().closedIsland(grid)
# print(s)

"""
Accepted
47/47 cases passed (64 ms)
Your runtime beats 93.7 % of python3 submissions
Your memory usage beats 19.33 % of python3 submissions (15.5 MB)
"""

# @lc code=end

