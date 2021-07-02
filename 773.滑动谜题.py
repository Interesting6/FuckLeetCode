
#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start
from typing import List
from itertools import chain
def b2s(board):
    board = list(chain(*board))
    return ''.join(board)
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = "123450"
        l2s = lambda x: ''.join(x)
        board = [str(i) for i in list(chain(*board))]
        if l2s(board) == target:
            return 0
        # print(board)
        mv_map = {0:[1, 3], 1:[0, 2, 4], 2: [1, 5], 3:[0, 4], 4:[1, 3, 5], 5: [2, 4]}
        def get_chd(board):
            for i, b in enumerate(board):
                if (b=='0'):
                    break
            need_mv = [(i, j) for j in mv_map[i]]
            for (i, j) in need_mv:
                boardt = list(board)
                boardt[i], boardt[j] = boardt[j], boardt[i]
                yield boardt

        from collections import deque
        dq = deque([board])
        vis = set([l2s(board)])
        step = -1
        while dq:
            sz = len(dq)
            step += 1
            for _ in range(sz):
                node = dq.popleft()
                if l2s(node) == target:
                    return step
                for chd in get_chd(node):
                    chd_str = l2s(chd)
                    if chd_str not in vis:
                        dq.append(chd)
                        vis.add(chd_str)
        return -1
"""
Accepted
32/32 cases passed (56 ms)
Your runtime beats 60.67 % of python3 submissions
Your memory usage beats 8.33 % of python3 submissions (15.1 MB)
"""
# board = [[1,2,3],[4,0,5]]
# board = [[4,1,2],[5,0,3]]
# board = [[3,2,4],[1,5,0]]
# board = [[1,2,3],[5,4,0]]
# s = Solution().slidingPuzzle(board)
# print(s)

# @lc code=end

