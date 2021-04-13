# @before-stub-for-debug-begin
# from python3problem151 import *
# from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = list(s)
#         n = len(s)
#         i = 0
#         j = n-1
#         while s[i] == ' ':
#             i += 1
#         while s[j] == ' ':
#             j -= 1

#         def strip_redundant_space(s, i, j): # 左闭右闭
#             # 双指针法删除单词
#             sp = i # 指向已经调节好的那部分字符串
#             for fp in range(i, j+1): # 遍历整个字符串
#                 if s[fp] != ' ':
#                     s[fp], s[sp] = s[sp], s[fp]
#                     sp += 1
#                 else: # 当前字符为空格
#                     if s[sp-1] != ' ': # 处理好的前一个字符不为空格
#                         sp += 1 # 空出一格
#                     else: # 处理好的前一个字符为空格
#                         pass # 已经有空格了，跳过删去多余的空格
#             return sp
#         sp = strip_redundant_space(s, i, j)
#         s = s[i:sp]
        
#         def reverse(s, i, j): # 翻转，左闭右闭
#             for k in range((j-i)//2+1):
#                 s[i+k], s[j-k] = s[j-k], s[i+k]
#         # 第一次翻转
#         reverse(s, 0, len(s)-1)

#         # 第二次单词翻转
#         sp = 0
#         for fp in range(0, len(s)):
#             if s[fp] == ' ':
#                 reverse(s, sp, fp-1)
#                 sp = fp + 1
#             if fp == len(s)-1:
#                 reverse(s, sp, fp)
#         return ''.join(s)
"""
Accepted
57/57 cases passed (68 ms)
Your runtime beats 5.08 % of python3 submissions
Your memory usage beats 17.82 % of python3 submissions (15.1 MB)
"""



# 其实两种写法都差不多
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i = 0
        while s[i] == ' ': # 去除前面的空格
            i += 1

        """这种写法相当于后面的字符没被改动，靠sp截取掉后面的；
        而我上面的写法是把多的空格放到结尾了"""
        # 双指针法删除单词中间的空格，
        sp = i # 指向已经调节好的那部分字符串
        for fp in range(i, n): # 遍历整个字符串
            if s[fp] == ' ' and s[fp-1] == ' ':
                # 当前字符为空格，且前面一个为空格
                continue
            else: 
                s[sp] = s[fp]
                sp += 1
        if sp-1 > 0 and s[sp-1] == ' ':
            s = s[i:sp-1]
        else:
            s = s[i:sp]
        # print(s)
        def reverse(s, i, j): # 翻转，左闭右闭
            for k in range((j-i)//2+1):
                s[i+k], s[j-k] = s[j-k], s[i+k]
        # 第一次翻转
        reverse(s, 0, len(s)-1)

        # 第二次单词翻转
        sp = 0
        for fp in range(0, len(s)):
            if s[fp] == ' ':
                reverse(s, sp, fp-1)
                sp = fp + 1
            if fp == len(s)-1:
                reverse(s, sp, fp)
        return ''.join(s)
"""
Accepted 快不了多少
57/57 cases passed (64 ms)
Your runtime beats 6.85 % of python3 submissions
Your memory usage beats 41.82 % of python3 submissions (15 MB)
"""

# s = Solution().reverseWords("  Bob    Loves  Alice   ")    
# print(s)
# @lc code=end

