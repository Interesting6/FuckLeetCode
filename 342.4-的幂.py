#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n & 3 == 0:
            n >>= 2
        return n == 1
        
        # import math
        # t = math.log(n, 4)
        # return int(t) == t
""" 
Accepted 调库
1061/1061 cases passed (40 ms)
Your runtime beats 75.02 % of python3 submissions
Your memory usage beats 31.27 % of python3 submissions (14.9 MB)
Accepted 位运算
1061/1061 cases passed (44 ms)
Your runtime beats 53.19 % of python3 submissions
Your memory usage beats 14.85 % of python3 submissions (14.9 MB)
"""

# @lc code=end

