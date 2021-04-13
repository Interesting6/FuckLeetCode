#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
def match(l, r):
    if l == "(" and r == ")":
        return True
    if l == "[" and r == "]":
        return True
    if l == "{" and r =="}":
        return True
    return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lft = "([{"
        rit = ")]}"
        for c in s:
            if c in lft:
                stack.append(c)
            else:
                if not stack:
                    return False
                t = stack.pop()
                if not match(t, c):
                    return False
        if stack:
            return False
        else:
            return True
            
# @lc code=end

