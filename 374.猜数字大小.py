#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# pick = 6
# def guess(num: int) -> int:
#     if num < pick:
#         return 1
    

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = l + ((r-l)>>1)
            if guess(m) == 0:
                return m
            elif guess(m) == 1:
                l = m + 1
            elif guess(m) == -1:
                r = m - 1
        return l
"""
Accepted
25/25 cases passed (44 ms)
Your runtime beats 35.46 % of python3 submissions
Your memory usage beats 7.19 % of python3 submissions (14.9 MB)
"""
        
# @lc code=end

