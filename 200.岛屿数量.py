#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
# class Solution:
#     def DFS(self, grid, r, c,):
#         if 0 <= r < self.h and 0 <= c < self.w:
#             if grid[r][c] != "1": # 为海水，直接跳过
#                 return False
#             else: # 为岛屿时
#                 grid[r][c] = "0"
        
#                 self.DFS(grid, r+1, c)
#                 self.DFS(grid, r-1, c)
#                 self.DFS(grid, r, c+1)
#                 self.DFS(grid, r, c-1)

#     def numIslands(self, grid: List[List[str]]) -> int:
#         self.h = len(grid)
#         self.w = len(grid[0])
#         if not self.w:
#             return 0
#         res = 0
#         for i in range(self.h):
#             for j in range(self.w):
#                 if grid[i][j] == "1":
#                     res += 1
#                     self.DFS(grid, i, j) # 将此岛屿所有元素变为0
#         return res

# class Solution:
#     def BFS(self, grid, r, c):
#         queue = [(r, c), ]
#         while queue:
#             size = len(queue)
#             for i in range(size):
#                 r, c = queue.pop(0)
#                 if grid[r][c] == "1": # 如果是岛屿
#                     grid[r][c] = 0
#                     if r+1 < self.h:
#                         queue.append((r+1, c))
#                     if 0 <= r-1:
#                         queue.append((r-1, c))
#                     if c+1 < self.w:
#                         queue.append((r, c+1))
#                     if 0 <= c-1:
#                         queue.append((r, c-1))
            

#     def numIslands(self, grid: List[List[str]]) -> int:
#         self.h = len(grid)
#         self.w = len(grid[0])
#         if not self.w:
#             return 0
#         res = 0
#         for i in range(self.h):
#             for j in range(self.w):
#                 if grid[i][j] == "1":
#                     res += 1
#                     self.BFS(grid, i, j) # 将此岛屿所有元素变为0
#         return res

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        self.h = len(grid)
        self.w = len(grid[0])
        if not self.w:
            return 0
        res = 0
        for i in range(self.h):
            for j in range(self.w):
                if grid[i][j] == "1":
                    res += 1
                    self.DFS(grid, i, j) # 将此岛屿所有元素变为0
        return res

# @lc code=end

