#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
"""滑窗法"""
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         @cache
#         def isPalindrome(i, j):
#             if i >= j:
#                 return True
#             if s[i] == s[j]:
#                 return isPalindrome(i+1, j-1)
#             else:
#                 return False
#         max_pali = ''
#         max_pali_len = 0
#         n = len(s)
#         for i,c in enumerate(s):
#             j = n-1 # 窗口直接拉满，缩小右边界找到第一个回文即可，最烂也是找到j=i时
#             while not isPalindrome(i, j): 
#                 j -= 1
#             new_pali_len = j-i+1
#             if new_pali_len > max_pali_len:
#                 max_pali_len = new_pali_len
#                 max_pali = s[i:j+1]
#             if i >= n-max_pali_len: # 剪枝，此时窗口大小小于最大回文子串，以后的肯定也更小，直接终止。
#                 break
#         isPalindrome.cache_clear()
#         return max_pali
"""
Accepted
176/176 cases passed (8732 ms)
Your runtime beats 14.63 % of python3 submissions
Your memory usage beats 5.08 % of python3 submissions (101 MB)
"""

"""试试递归法"""

"动态规划，居然还会偶尔超时"
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[0]*n for _ in range(n)] # s[i到j]是否为回文
        maxlen = 0
        res = ""
        # for i in range(n): 错误不能这样！
        #     for j in range(i, n): # 子串从短到大
        #         if i == j: # 边界
        #             dp[i][j] = 1
        #         elif i+1 == j and s[i] == s[j]: # 边界
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
        #         if dp[i][j] and j-i+1>maxlen:
        #             res = s[i:j+1]
        #             maxlen = j-i+1
        for l in range(n): # 枚举子串长度，必须这样，子串从短到大
            for i in range(n): # 枚举子串起始坐标
                # 主对角线，次对角线，次次对角线这样遍历dp的，内层↘，外层↗
                # 因为dp[i][j]找dp[i+1][j-1]是向着左下方找，所以必须这样遍历
                j = i + l # 起始坐标+长度=子串结束坐标
                if j >= n:
                    break
                if l == 0: # 边界1
                    dp[i][j] = 1
                elif l == 1 and s[i]==s[j]: # 边界2
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i]==s[j])
                if dp[i][j] and l+1 > maxlen:
                    res = s[i:j+1]
                    maxlen = l+1
        return res
"""
Accepted
176/176 cases passed (9276 ms)
Your runtime beats 10.11 % of python3 submissions
Your memory usage beats 37.91 % of python3 submissions (22.4 MB)
"""
# @lc code=end

