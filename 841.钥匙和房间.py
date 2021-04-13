# @before-stub-for-debug-begin
from python3problem841 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#

# @lc code=start
# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         N = len(rooms)
#         stack = []
#         stack.append(rooms[0])
#         visited = set()
#         visited.add(0)
#         while stack:
#             keys = stack.pop()
#             visited.update(keys)
#             for k in keys:
#                 nkeys = [nk for nk in rooms[k] if nk not in visited]
#                 stack.append(nkeys)
#         # print(visited)
                
#         if len(visited) == N:
#             return True
#         else:
#             return False

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        vis = set()
        def dfs(idx):
            vis.add(idx)
            for k in rooms[idx]:
                if k not in vis:
                    dfs(k)
        dfs(0)
        return len(vis) == N

        
# @lc code=end

