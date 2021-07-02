#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        di = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        stack = []
        n = len(s)
        i = 0
        while i < n:
            if i<n-1:
                if di[s[i]] >= di[s[i+1]]:
                    res += di[s[i]]
                    i += 1
                elif di[s[i]] < di[s[i+1]]:
                    res += di[s[i+1]] - di[s[i]]
                    i += 2
            else:
                res += di[s[i]]
                i += 1
        return res
            

# s = Solution().romanToInt("LVIII")
# print(s)
"""
Accepted
3999/3999 cases passed (56 ms)
Your runtime beats 68.78 % of python3 submissions
Your memory usage beats 89.03 % of python3 submissions (14.8 MB)
"""

# @lc code=end

