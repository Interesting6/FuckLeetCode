# @before-stub-for-debug-begin
from python3problem695 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         res = 0
#         def dfs(i, j):
#             nonlocal res, cnt
#             grid[i][j] = 2
#             cnt += 1
#             res = max(res, cnt)
#             for r,c in [(i-1, j), (i+1,j), (i,j-1), (i,j+1)]:
#                 if 0<=r<m and 0<=c<n and grid[r][c]==1:
#                     dfs(r, c)
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     cnt = 0
#                     dfs(i, j)
#         return res
""" 总得来说上面这种写法没有掌握递归的返回值写法，只是在每次都声明一个nonlocal的cnt来改变
Accepted
726/726 cases passed (144 ms)
Your runtime beats 78.34 % of python3 submissions
Your memory usage beats 5.06 % of python3 submissions (18.6 MB)
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        def dfs(i, j):
            grid[i][j] = 2
            cnt = 1 # 当前格子面积为1
            for r,c in [(i-1, j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0<=r<m and 0<=c<n and grid[r][c]==1:
                    cnt += dfs(r, c) # 加上其相邻的面积之和，感觉这里才体现了后序遍历的深度优先，必须到了最深处才能计算，一步步回到根部
            return cnt # 返回当前格子面积与其相邻的面积之和，所以必须先进入最深处；而像上面只是一个先序遍历

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = dfs(i, j)
                    res = max(res, cnt)
        return res
""" 但这种写法好像空间复杂度也挺高的样子
Accepted
726/726 cases passed (140 ms)
Your runtime beats 86.75 % of python3 submissions
Your memory usage beats 5.06 % of python3 submissions (18.4 MB)
"""   
# @lc code=end

