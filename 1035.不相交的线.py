#
# @lc app=leetcode.cn id=1035 lang=python3
#
# [1035] 不相交的线
#

# @lc code=start
from typing import List
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        # for i in range(n1+1):
        #     dp[i][0] = 0
        # for j in range(n2+1):
        #     dp[0][j] = 0

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[n1][n2]

# nums1 = [2,5,1,2,5]; nums2 = [10,5,2,1,5,2]
# # nums1 = [1,3,7,1,7,5]; nums2 = [1,9,2,5,1]
# s = Solution().maxUncrossedLines(nums1, nums2)
# print(s)
""" 本质上是一个最长公共子序列问题。
Accepted
74/74 cases passed (180 ms)
Your runtime beats 89.83 % of python3 submissions
Your memory usage beats 79.32 % of python3 submissions (15.1 MB)
"""
# @lc code=end

