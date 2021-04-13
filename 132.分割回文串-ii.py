# @before-stub-for-debug-begin
from python3problem132 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        li = []

        @cache
        def isPalindrome(i, j):
            if i >= j:
                return True
            else:
                return s[i] == s[j] and isPalindrome(i+1, j-1)

        @cache
        def f(x):
            if isPalindrome(0, x):
                return 0
            
            res = x
            for j in range(x):
                if isPalindrome(j+1, x):
                    res = min(res, f(j))
            return res + 1
        
        res = f(n-1)
        isPalindrome.cache_clear()
        f.cache_clear()
        # print(res)
        return res

"""
Accepted
29/29 cases passed (1112 ms)
Your runtime beats 5.16 % of python3 submissions
Your memory usage beats 5.15 % of python3 submissions (161 MB)
"""

# @lc code=end

