# @before-stub-for-debug-begin
from python3problem131 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         n = len(s)
#         res = []
#         ans = []

#         # @cache
#         def isPalindrome(i, j): # i到j的子串是否为回文 i should < j
#             if i >= j: # 空串
#                 return True
#             if s[i] == s[j]: # 第一个字符与最后一个要相等
#                 return isPalindrome(i+1, j-1) # 再往后继续判断
#             else:
#                 return False

#         def dfs(i): # 对于位置i，看[i, j]能否构成回文，若能则继续深度优先；若不能则看[i, j+1]
#             if i == n: # 停止条件
#                 res.append(ans[:])
#                 return

#             for j in range(i, n):
#                 if isPalindrome(i, j):
#                     ans.append(s[i:j+1]) # 在树里，相当于是当前的路径
#                     dfs(j+1)
#                     ans.pop()  # 在路径里回溯
#                 # 当[i, j]子串不是回文时，看[i, j+1]是否为回文

#         dfs(0)
#         # isPalindrome.cache_clear()
#         return res
                


# 第二次做
class Solution:
    def partition(self, s: str):
        if not s:
            return []
        @cache
        def isPalindrome(i, j):
            if i >= j:
                return True
            return s[i] == s[j] and isPalindrome(i+1, j-1)
        n = len(s)
        res = []
        li = []
        pth = ""
        # dfs中不能用cache呀！！！！是用dfs去递归，而不是求值！
        def dfs(i):
            if i == n:
                res.append(li[:])
                return
            for j in range(i, n):
                if isPalindrome(i, j):
                    li.append(s[i: j+1])
                    dfs(j+1)
                    li.pop()
        dfs(0)
        isPalindrome.cache_clear()
        return res

# @lc code=end

