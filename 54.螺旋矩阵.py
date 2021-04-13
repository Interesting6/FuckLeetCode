# @before-stub-for-debug-begin
from python3problem54 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
"""自己的按方向模拟，四个方向一致走完是一圈，最小边为单数时，存在一条线情况"""
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         m, n = len(matrix), len(matrix[0])
#         res = []
#         r, c = 0, 0
#         l = 0
#         k = min(m//2, n//2)
#         while l <= k:
#             if m%2==1 or n%2==1: # m和n其中有一个为奇数时
#                 if m-1-l == l: # 只剩单独一行了，直接读取该行全部
#                     for c in range(l, n-l):  # l -> n-1 - (l-1)
#                         res.append(matrix[l][c])
#                     break
#                 if n-1-l == l: # 只剩单独一列了，直接读取该列全部
#                     for r in range(l, m-l):  # l -> m-1 - (l-1)
#                         res.append(matrix[r][l])
#                     break
#             else: # m, n都为偶数时，l执行到k-1即可
#                 if l == k:
#                     break
#             for c in range(l, n-1-l):
#                 res.append(matrix[r][c])
#             c += 1
#             for r in range(l, m-1-l):
#                 res.append(matrix[r][c])
#             r += 1

#             for c in range(n-1-l, l, -1):
#                 res.append(matrix[r][c])
#             c -= 1
#             for r in range(m-1-l, l, -1):
#                 res.append(matrix[r][c])

#             l += 1
#         return res

"""
    Accepted
    22/22 cases passed (48 ms)
    Your runtime beats 10.7 % of python3 submissions
    Your memory usage beats 41.57 % of python3 submissions (14.9 MB)
"""

class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        res = []
        x1, y1 = (0, 0)
        x2, y2 = (m-1, n-1) # 两个点唯一的确定一个矩形
        while x1<=x2 and y1<=y2:
            if x1 == x2:
                for j in range(y1, y2+1):
                    res.append(matrix[x1][j])
                break
            if y1 == y2:
                for i in range(x1, x2+1):
                    res.append(matrix[i][y1])
                break
            for j in range(y1, y2):
                res.append(matrix[x1][j])
            for i in range(x1, x2):
                res.append(matrix[i][y2])
            for j in range(y2, y1, -1):
                res.append(matrix[x2][j])
            for i in range(x2, x1, -1):
                res.append(matrix[i][y1])
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
        return res
"""
Accepted
22/22 cases passed (40 ms)
Your runtime beats 56.12 % of python3 submissions
Your memory usage beats 5.07 % of python3 submissions (15 MB)
"""
# @lc code=end

