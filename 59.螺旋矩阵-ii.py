# @before-stub-for-debug-begin
from python3problem59 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
"""循环不变量：左闭右开"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [ [1] ]
        res = [[0]*n for _ in range(n)]
        i, j = 0, 0
        l = 0
        k = 1
        while l < n-1-l:
            for j in range(l, n-1-l):
                res[i][j] = k
                k += 1
            j += 1
            for i in range(l, n-1-l):
                res[i][j] = k
                k += 1
            i += 1
            for j in range(n-1-l, l, -1):
                res[i][j] = k
                k += 1
            j -= 1
            for i in range(n-1-l, l, -1):
                res[i][j] = k
                k += 1

            l += 1
        if n % 2: # 当n为奇数时，矩阵中间的位置需要单独考虑
            res[n//2][n//2] = k
        return res
"""
Accepted
20/20 cases passed (44 ms)
Your runtime beats 34.37 % of python3 submissions
Your memory usage beats 15.07 % of python3 submissions (15 MB)
"""
# @lc code=end

