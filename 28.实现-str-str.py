#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
"""
翻了下两年前的python代码，写的也是牛逼。。。
直接用haystack.split(needle)，有元素就是其第一个位置，否者就-1
"""

"""KMP算法"""
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         n, m = len(haystack), len(needle)
#         if m==0:
#             return 0
#         def get_next(pattern: str) -> list:
#             m = len(pattern)
#             next = [0] * m
#             j = 0 # 指向前缀末尾，
#             # 还代表p[:i+1]的子串最长相等前后缀长度，
#             # 如aabaaf中，i指向f时，j应该为aabaa的最长相等前后缀长度2
#             for i in range(1, m): # 后缀末尾位置
#                 while j > 0 and pattern[j] != pattern[i]:
#                     j = next[j-1]
#                 if pattern[j] == pattern[i]:
#                     j += 1
#                 next[i] = j
#             return next
#         next = get_next(needle)
#         i = 0 # 指向haystack
#         j = 0 # 指向needle
#         while i < n: 
#             if needle[j] != haystack[i]:
#                 if j > 0: # j与i不匹配
#                     j = next[j-1]
#                 else: # 当前i与needle[0]都不匹配，j=0了
#                     i += 1 # 到下一个i重新与needle的第一个开始进行匹配
#             else: # 匹配成功，两个指针都加一
#                 i += 1
#                 j += 1
#                 if j == m: # needle中的元素都匹配完了
#                     return i-j
#         # haystack中的元素都走完了，needle里元素还没匹配完
#         return -1



# # 2021-04-20 每日一题打卡
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         n1 = len(haystack)
#         n2 = len(needle)
#         def get_next(needle):
#             n2 = len(needle)
#             nxt = [0] * n2
#             # nxt[0] = 1
#             i = 0
#             for j in range(1, n2):
#                 while i > 0 and needle[i] != needle[j]:
#                     i = nxt[i-1] # 注意这里不是i-=1
#                 if needle[i] == needle[j]:
#                     i += 1
#                 nxt[j] = i
#             return nxt
#         nxt = get_next(needle)
#         print(nxt)
#         i = 0
#         j = 0
#         while i < n1:
#             if j == n2:
#                 return i - n2
#             if haystack[i] == needle[j]:
#                 i += 1
#                 j += 1
#             else:
#                 if j > 0:
#                     j = nxt[j-1]
#                 else:
#                     i += 1
#         if j < n2:
#             return -1
#         else:
#             return i - n2

""" 虽然过程中错了几个地方，但还是没有花很久做出来了
Accepted
79/79 cases passed (52 ms)
Your runtime beats 29.17 % of python3 submissions
Your memory usage beats 5.08 % of python3 submissions (16.5 MB)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        def get_next(pattern):
            n = len(pattern)
            nxt = [0] * n
            j = 0
            for i in range(1, n):
                while j > 0 and pattern[i] != pattern[j]:
                    j = nxt[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                nxt[i] = j # 不管上面等不等都要更新！
            return nxt
        nxt = get_next(needle)
        print(nxt)
        j = 0
        # for i in range(m): # 不行，这样i不等时，i会跳到下一个，而不是重新比较
        #     if haystack[i] == needle[j]:
        #         j += 1
        #     else:
        #         j = nxt[j]
        #     if j == n:
        #         return i - n + 1
        # if j < n:
        #     return -1
        i = 0 
        while i < m:
            if j == n:
                return i - n
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = nxt[j-1]
                else:
                    i += 1
        if j < n:
            return -1
        else: # 两个字符串都为空的情况
            return i - n

"""
Accepted 跟上面基本一样，薛定谔的时间复杂度呀
79/79 cases passed (44 ms)
Your runtime beats 58.25 % of python3 submissions
Your memory usage beats 14.54 % of python3 submissions (15.6 MB)
"""

# s = Solution().strStr( "ababcabcacbab", "abcac")         
# haystack = "hello"; needle = "ll"
haystack = "adcadcaddcadde"; needle = "adcadde"
s = Solution().strStr(haystack, needle)
print(s)


# @lc code=end

