#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        flag = False
        max_len = 0
        for k,v in cnt.items():
            if v >= 2:
                if v % 2 == 0:
                    max_len += v
                else:
                    flag = True
                    v -= 1
                    max_len += v
            else:
                flag = True
        if flag:
            return max_len + 1
        else:
            return max_len
"""
Accepted
95/95 cases passed (36 ms)
Your runtime beats 87.2 % of python3 submissions
Your memory usage beats 5.94 % of python3 submissions (15 MB)
"""
# @lc code=end

