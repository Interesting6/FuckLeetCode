#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        def bi_search(l, r):
            while l < r:
                m = l + ((r-l)>>1)
                t = m**2
                if t == x:
                    return m
                elif t < x:
                    l = m + 1
                elif t > x:
                    r = m
            return l - 1
        res = bi_search(0, x)
        return res

""" 2021-04-19第一次做，ac了
Accepted
1017/1017 cases passed (56 ms)
Your runtime beats 31.92 % of python3 submissions
Your memory usage beats 76.92 % of python3 submissions (14.8 MB)
"""

# x = 293737
# s = Solution().mySqrt(x)
# print(s)
# import math
# print(math.sqrt(x))
# @lc code=end

