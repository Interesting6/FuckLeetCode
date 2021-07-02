#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#

# @lc code=start
from typing import List
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        from sortedcontainers import SortedList
        res = float("-inf")
        for top in range(m):
            rowCompress = [0] * n # 列的和
            for bot in range(top, m):
                for c in range(n):
                    rowCompress[c] += matrix[bot][c]
                totalSet = SortedList([0])
                s = 0
                for v in rowCompress:
                    s += v
                    lb = totalSet.bisect_left(s - k)
                    if lb != len(totalSet):
                        res = max(res, s-totalSet[lb])
                    totalSet.add(s)

        return res

"""
Accepted
27/27 cases passed (2968 ms)
Your runtime beats 14.28 % of python3 submissions
Your memory usage beats 52.48 % of python3 submissions (15.8 MB)
"""

# @lc code=end

