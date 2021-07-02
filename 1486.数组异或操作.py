#
# @lc app=leetcode.cn id=1486 lang=python3
#
# [1486] 数组异或操作
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        from functools import reduce
        res = reduce(lambda a, b: a^b, [start+2*i for i in range(n)])
        return res

"""
Accepted
54/54 cases passed (32 ms)
Your runtime beats 95.35 % of python3 submissions
Your memory usage beats 94.61 % of python3 submissions (14.6 MB)
"""
# @lc code=end

