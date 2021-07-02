#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#

# @lc code=start
from typing import List
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        def get_pos(num):
            r = (num-1) // N
            c = (num-1) % N
            c =  c if ((r+1) & 1) else (N-1 - c) 
            r = N-1 - r
            return r, c
        # r, c = get_pos(20)
        # print(r, c)
        def skip(num):
            r, c = get_pos(num)
            if board[r][c] != -1:
                return board[r][c]
            else:
                return num
        from collections import deque
        dq = deque([1])
        vis = set([1])
        step = -1
        while dq:
            sz = len(dq)
            step += 1
            for _ in range(sz):
                node = dq.popleft()
                if (node == N*N):
                    return step
                for i in range(1, 7):
                    new_node = node + i
                    if (new_node > N*N):
                        continue
                    new_node = skip(new_node)
                    if (new_node not in vis):
                        dq.append(new_node)
                        vis.add(new_node)

        return -1

""" 21-06-27 每日一题打卡BFS
Accepted
211/211 cases passed (100 ms)
Your runtime beats 99.08 % of python3 submissions
Your memory usage beats 14.68 % of python3 submissions (15.1 MB)
"""

# board = [[-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]

# s = Solution().snakesAndLadders(board)
# print(s)

# @lc code=end

