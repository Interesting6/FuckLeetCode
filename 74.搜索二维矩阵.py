# @before-stub-for-debug-begin
from python3problem74 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m, n = len(matrix), len(matrix[0])
#         def bifind(l, r, li, tar):
#             while l <= r:
#                 m = l + ((r-l)>>1)
#                 if tar > li[m]:
#                     l = m+1
#                 elif tar < li[m]:
#                     r = m-1
#                 elif tar == li[m]:
#                     return True
#             return False
        
#         for i in range(m):
#             if matrix[i][0] <= target <= matrix[i][-1]:
#                 break 
#             elif i<m-1 and matrix[i][-1]< target < matrix[i+1][0]:
#                 return False
#         res = bifind(0, n-1, matrix[i], target)
#         return res


"""两次二分"""
class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        # 第一次二分行
        l = 0
        r = m-1
        while l < r:
            mid = (l+r+1) >> 1
            if matrix[mid][0] <= target:
                l = mid
            else:
                r = mid - 1
        
        if target == matrix[r][0]:
            return True
        elif target < matrix[r][0]:
            return False
        row = r
        # 结束后， matrix[row][0] < target < matrix[row+1][0]
        # 第二次二分
        l = 0
        r = n -1
        while l < r:
            mid = (l+r+1)>>1
            if matrix[row][mid] <= target:
                l = mid
            else:
                r = mid - 1
        col = r
        return matrix[row][col] == target


# @lc code=end

