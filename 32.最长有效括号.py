#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0 :
            return 0
        stack = []
        res = 0
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')':
                if stack:
                    stack.pop()
                    res += 2
                else:
                    pass
        return res


# @lc code=end

