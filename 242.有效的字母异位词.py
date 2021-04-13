# @before-stub-for-debug-begin
from python3problem242 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        di = {}
        for sc, tc in zip(s, t):
            if sc in di:
                di[sc] += 1
            else:
                di[sc] = 1
            if tc in di:
                di[tc] -= 1
            else:
                di[tc] = -1
        res = True
        for k,v in di.items():
            res = res and (v == 0)
        return res
"""
Accepted
34/34 cases passed (60 ms)
Your runtime beats 56.01 % of python3 submissions
Your memory usage beats 81.86 % of python3 submissions (14.9 MB)
"""
# @lc code=end

