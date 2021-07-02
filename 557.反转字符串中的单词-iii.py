#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        i0 = 0
        for i, c in enumerate(s):
            if c == ' ':
                s[i0:i] = s[i0:i][::-1]
                i0 = i+1
                
        if i > i0:
            s[i0:i+1] = s[i0:i+1][::-1]
        res = ''.join(s)
        return res

# s = "Let's take LeetCode contest"
# so = Solution().reverseWords(s)
"""
Accepted
29/29 cases passed (76 ms)
Your runtime beats 19.9 % of python3 submissions
Your memory usage beats 60.05 % of python3 submissions (15.3 MB)
"""

# @lc code=end

