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
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m==0:
            return 0
        def get_next(pattern: str) -> list:
            m = len(pattern)
            next = [0] * m
            j = 0 # 指向前缀末尾，
            # 还代表p[:i+1]的子串最长相等前后缀长度，
            # 如aabaaf中，i指向f时，j应该为aabaa的最长相等前后缀长度2
            for i in range(1, m): # 后缀末尾位置
                while j > 0 and pattern[j] != pattern[i]:
                    j = next[j-1]
                if pattern[j] == pattern[i]:
                    j += 1
                next[i] = j
            return next
        next = get_next(needle)
        i = 0 # 指向haystack
        j = 0 # 指向needle
        while i < n: 
            if needle[j] != haystack[i]:
                if j > 0: # j与i不匹配
                    j = next[j-1]
                else: # 当前i与needle[0]都不匹配，j=0了
                    i += 1 # 到下一个i重新与needle的第一个开始进行匹配
            else: # 匹配成功，两个指针都加一
                i += 1
                j += 1
                if j == m: # needle中的元素都匹配完了
                    return i-j
        # haystack中的元素都走完了，needle里元素还没匹配完
        return -1
            
s = Solution().strStr( "ababcabcacbab", "abcac")         
print(s)
# @lc code=end

