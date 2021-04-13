# @before-stub-for-debug-begin
from python3problem1089 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0 # 转换后的？
        j = 0
        while j< n:
            if arr[i] == 0:
                j += 1
            i += 1
            j += 1
        i -= 1
        j -= 1

        while i >= 0:
            if j<n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                arr[j] = 0
            i -= 1
            j -= 1
"""
Accepted
30/30 cases passed (44 ms)
Your runtime beats 80.07 % of python3 submissions
Your memory usage beats 78.7 % of python3 submissions (14.9 MB)
"""

# @lc code=end

