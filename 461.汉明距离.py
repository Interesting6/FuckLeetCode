#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        t = x ^ y
        res = 0
        while t:
            res += t & 1
            t >>= 1
        return res
"""
Accepted 全位运算居然还这么慢？
149/149 cases passed (44 ms)
Your runtime beats 33.45 % of python3 submissions
Your memory usage beats 8.38 % of python3 submissions (14.9 MB)
"""
# @lc code=end

