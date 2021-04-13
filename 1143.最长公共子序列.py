#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n1 = len(text1)
#         n2 = len(text2)
#         dp = [[0]*(n2+1) for _ in range(n1+1)]
#         for i in range(1, n1+1):
#             for j in range(1, n2+1):
#                 if text1[i-1] == text2[j-1]:
#                     dp[i][j] = dp[i-1][j-1] + 1
#                 else:
#                     dp[i][j] = max(dp[i][j-1], dp[i-1][j])
#         return dp[n1][n2]



class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n1, n2 = len(text1), len(text2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]: # 注意偏移
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # return dp[n1][n2]
        # 回溯
        res = []
        def track_back(i, j, pth):
            while i >= 1 and j >= 1:
                if text1[i-1] == text2[j-1]:
                    pth.append(text1[i-1])
                    i -= 1
                    j -= 1
                else:
                    if dp[i-1][j] > dp[i][j-1]:
                        i -= 1
                    elif dp[i-1][j] < dp[i][j-1]:
                        j -= 1
                    # 只需要输出一个的话，把下面else注销，并合并到上面俩的任意一个即可，改成≥
                    else: # 相等情况，最长公共子序列有多个
                        track_back(i, j-1, pth)
                        track_back(i-1, j, pth)
                        return
            res.append(''.join(pth[::-1]))
        track_back(n1, n2, [])
        print(res)


# s = Solution().longestCommonSubsequence("abcde", "ace")
s = Solution().longestCommonSubsequence("vcnwrmxcfcxabkxcvgbozmpspsbenazglyxkpibgzq", "pmlstotylonkvmhqjyxmnqzctonqtobahcrcbibgzgx")
# print(s)

# @lc code=end

