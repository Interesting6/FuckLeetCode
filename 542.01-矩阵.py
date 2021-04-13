# @before-stub-for-debug-begin
from python3problem542 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
from collections import deque
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         h = len(matrix)
#         w = len(matrix[0])
#         def BFS(r, c):
#             vis = set()
#             step = 0
#             queue = deque([(r, c)])
#             vis.add((r, c))
#             while queue:
#                 size = len(queue)
#                 for _ in range(size):
#                     nr, nc = queue.popleft()
#                     vis.add((nr, nc))
#                     if matrix[nr][nc] == 0:
#                         return step
#                     else:
#                         if 0 <= nr-1 and (nr-1, nc) not in vis:
#                             queue.append((nr-1, nc))
#                         if nr+1 < h and (nr+1, nc) not in vis:
#                             queue.append((nr+1, nc))
#                         if 0 <= nc-1 and (nr, nc-1) not in vis:
#                             queue.append((nr, nc-1))
#                         if nc+1 < w and (nr, nc+1) not in vis:
#                             queue.append((nr, nc+1))

#                 step += 1

#         for i in range(h):
#             for j in range(w):
#                 if matrix[i][j] != 0:
#                     matrix[i][j] = BFS(i, j)
            
#         return matrix

class Solution:
    def updateMatrix(self, matrix):
        h = len(matrix)
        w = len(matrix[0])
        # 各个点到最近0的距离。
        dist = [[0 if matrix[i][j] == 0 else 10000 for j in range(w)] for i in range(h)] 
        zero_point = [(i, j) for j in range(w) for i in range(h) if matrix[i][j]==0]
        dq = deque(zero_point) # 将所有为0的点加入初始队列中
        vis = set(zero_point)
        while dq:
            r, c = dq.popleft()
            for i,j in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                if 0 <= i < h and 0 <= j < w and (i,j) not in vis:
                    if dist[r][c] + 1 < dist[i][j]:
                        dq.append((i, j))
                        dist[i][j] = dist[r][c] + 1
                        vis.add((i,j))
        return dist



# @lc code=end

"""
在广度优先搜索的每一步中，
如果我们从矩阵中的位置 x 搜索到了位置 y，并且 y 还没有被搜索过，
那么位置 y 离 0 的距离就等于位置 x 离 0 的距离加上 1。
因为每步搜索只搜索邻居节点，距离为1。
"""