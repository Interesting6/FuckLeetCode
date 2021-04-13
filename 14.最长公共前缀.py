# @before-stub-for-debug-begin
from python3problem14 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        i = -1
        n = len(strs)
        if n == 0:
            return ""
        if n == 1:
            return strs[0]
        flag = True
        try:
            while flag:
                i += 1
                for j in range(1, n):
                    if strs[j][i] != strs[j-1][i]:
                        flag = False
                        break
            # print(i)
            return strs[0][:i]
        except IndexError:
            return strs[0][:i]
# s = Solution().longestCommonPrefix(["dog","racecar","car"])
# print(s)
"""
Accepted  终于过了，我这个写法算纵向比较，还有横向比较的，可以做到分而治之，之后可以试试
123/123 cases passed (48 ms)
Your runtime beats 26.57 % of python3 submissions
Your memory usage beats 63.42 % of python3 submissions (14.9 MB)
"""

# @lc code=end

