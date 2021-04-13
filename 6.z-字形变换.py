# @before-stub-for-debug-begin
from python3problem6 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
"""模拟行索引的变化"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ['' for _ in range(numRows)]
        n = len(s)
        ridx = 0
        flag = 1
        for c in s:
            res[ridx] += c
            ridx += flag
            if ridx == numRows-1 or ridx == 0:
                flag = -flag
        return ''.join(res)
"""
Accepted
1157/1157 cases passed (52 ms)
Your runtime beats 96.2 % of python3 submissions
Your memory usage beats 67.73 % of python3 submissions (15 MB)
"""           
# @lc code=end

