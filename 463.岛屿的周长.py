#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        nums = 0
        connc = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    nums += 1
                    if i-1>=0 and grid[i-1][j] == 1: # 左边是岛屿
                        connc += 1
                    if j-1>=0 and grid[i][j-1] == 1: # 上边是岛屿
                        connc += 1
                    # 无右下，因为避免重复计算

        return 4*nums - 2*connc
"""
有点容斥原理的意思
Accepted
5833/5833 cases passed (116 ms)
Your runtime beats 88.09 % of python3 submissions
Your memory usage beats 66.23 % of python3 submissions (15.1 MB)
"""
# @lc code=end

