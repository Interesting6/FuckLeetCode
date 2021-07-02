#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n & 1 == 0:
            n >>= 1
        return n == 1
        

# s = Solution().isPowerOfTwo(5)
# print(s)
"""
Accepted
1108/1108 cases passed (44 ms)
Your runtime beats 49.18 % of python3 submissions
Your memory usage beats 80.82 % of python3 submissions (14.7 MB)
"""

# @lc code=end

