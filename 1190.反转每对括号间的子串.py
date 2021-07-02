#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif  97 <= ord(c) <= 122:
                stack.append(c)
            elif c == ')':
                t = ''
                while stack[-1] != '(':
                    t += stack.pop()[::-1]
                stack[-1] = t
        # print(stack)
        res = ''.join(stack)
        return res

# s = "(u(love)i)"
# s = "(ed(et(oc))el)"
# s = "a(bcdefghijkl(mno)p)q"
# s = "(love)"
# res = Solution().reverseParentheses(s)
# print(res)
# @lc code=end

