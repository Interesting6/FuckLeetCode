#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        n = len(S)
        stack = []
        for i in range(n):
            if not stack:
                stack.append(S[i])
            else:
                if stack[-1] == S[i]:
                    stack.pop()
                else:
                    stack.append(S[i])
        return ''.join(stack)

# @lc code=end

