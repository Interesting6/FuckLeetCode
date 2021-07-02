#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = l + ((r-l)>>1)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return r
"""
Accepted
22/22 cases passed (44 ms)
Your runtime beats 31 % of python3 submissions
Your memory usage beats 17.12 % of python3 submissions (14.9 MB)
"""    

# @lc code=end

