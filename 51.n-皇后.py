# @before-stub-for-debug-begin
from python3problem51 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # if n == 1:
        #     return [["Q"]]
        res = []
        pth = []
        matrix = [[1]* n for _ in range(n)]
        di = {}
        for i in range(n):
            di[i] = "."*(i) + "Q" + "."*(n-i-1)

        def off(r, c):
            offset = set()
            for i in range(n):
                if matrix[i][c]:
                    matrix[i][c] = 0
                    offset.add((i, c))
            for j in range(n):
                if matrix[r][j]:
                    matrix[r][j] = 0
                    offset.add((r, j))
            k = 1
            while k < n:
                for a,b in [(k,k), (k,-k), (-k, k), (-k, -k)]:
                    a += r
                    b += c
                    if 0<=a<n and 0<=b<n and matrix[a][b]:
                        matrix[a][b] = 0
                        offset.add((a, b))
                k += 1
            return offset

        def back(offset):
            for i,j in offset:
                matrix[i][j] = 1
            
        def backtracking(depth):
            if depth == n:
                res.append(pth[:])
                return True

            for i in range(n):
                for j in range(n):
                    if matrix[i][j]:
                        if i != depth: # 剪枝，
                            continue # 第i个皇后必须放在第i行
                        pth.append(di[j]) # ((i, j))
                        # pth.append(j)
                        offset = off(i, j) # 将皇后可达位置涂黑
                        backtracking(depth+1)
                        back(offset)  # 恢复上一个皇后涂黑的位置
                        pth.pop()
        
        backtracking(0)
        print(res)
        return res

"""
Accepted
9/9 cases passed (176 ms)
Your runtime beats 8.19 % of python3 submissions
Your memory usage beats 67.3 % of python3 submissions (15.2 MB)
"""

# @lc code=end

