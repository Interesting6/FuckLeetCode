#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        # max_len = 0
        # n = len(s)
        # for i, c in enumerate(s):
        #     cur_set = set()
        #     cur_set.add(c)
        #     j = i+1
        #     while j < n:
        #         if s[j] in cur_set:
        #             break
        #         else:
        #             cur_set.add(s[j])
        #             j += 1
        #     max_len = max(max_len, j - i)
        # return max_len
""" 
滑窗法，对每个开头的字母，都弄一个递增的滑窗，直到不能增大为止，比较每个开头的字母的滑窗，取最大的那个
Accepted
987/987 cases passed (628 ms)
Your runtime beats 9.32 % of python3 submissions
Your memory usage beats 37.26 % of python3 submissions (15 MB)
"""

# 2021-04-10 第二次做
class Solution: 
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        res = 1
        cnt = 1
        for i,c in enumerate(s):
            curset = set([c])
            flag = True # 停止
            for j in range(i+1, n):
                if s[j] not in curset: # 无重复
                    curset.add(s[j])
                else: # 有重复
                    res = max(res, j-i)
                    flag = False
                    break
            if flag: # 一直无重复
                res = max(res, j - i + 1)
                break # 后面肯定更短
        return res 

# s = Solution().lengthOfLongestSubstring("dvdfasdf")
# print(s)
"""
Accepted
987/987 cases passed (492 ms)
Your runtime beats 11.73 % of python3 submissions
Your memory usage beats 83.17 % of python3 submissions (14.9 MB)
"""

# 上面的改进
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n == 0:
            return 0
        res = 0
        window_set = set()
        j = 0
        for i,c in enumerate(s):
            # i - j-1肯定还是无重复的
            while j<n and s[j] not in window_set: 
                window_set.add(s[j])
                j += 1
            res = max(res, len(window_set))
            window_set.remove(c) # i要移动到下一个位置了，需要把该位置的元素从窗口删除
        return res
# s = Solution().lengthOfLongestSubstring("abb")
# print(s)
"""
Accepted
987/987 cases passed (92 ms)
Your runtime beats 35.34 % of python3 submissions
Your memory usage beats 59.67 % of python3 submissions (15 MB)
"""
# @lc code=end

