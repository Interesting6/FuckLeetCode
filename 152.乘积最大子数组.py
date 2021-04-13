#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
# 自己想出来的
# class Solution:
#     def maxProduct(self, nums) -> int:
#         n = len(nums)
#         if not n:
#             return 0
#         if n == 1:
#             return nums[0]
#         dp = [[1, 1] for _ in range(n)] # 最大的负积与最大的正积
#         res = float("-inf")
#         for i in range(0, n):
#             if nums[i] < 0:
#                 dp[i][0] = min(dp[i-1][1]*nums[i], nums[i])   # 当dp[i-1][1]>=1时，i加入最大的负的；当dp[i-1][1]取0时，这时候i不加入是最负的，
#                 dp[i][1] = max(dp[i-1][0]*nums[i], 0) # i加入，算到最大的正的；i不加入(dp[i-1][0]也为正时)则当前最大积为0
#             else:
#                 dp[i][0] = min(dp[i-1][0]*nums[i], 0) # i加入，算出最大的负的；i不加入(dp[i-1][0]为正时)则当前最大积为0
#                 dp[i][1] = max(dp[i-1][1]*nums[i], nums[i]) # 当dp[i-1][1]>=1时，i加入算出最大的正的；当dp[i-1][1]取0时，这是i不加入是最正的。
#             res = max(dp[i][1], res)
#         return res

# nums = [2,3,-2,4]
# nums = [-2, 3, -4]
# nums = [3, -1, 4]
# nums = [-2, 0, -1]
# s = Solution().maxProduct(nums)
# print(s)
"""
Accepted
187/187 cases passed (52 ms)
Your runtime beats 52.47 % of python3 submissions
Your memory usage beats 7.79 % of python3 submissions (16.9 MB)
"""

class Solution:
    def maxProduct(self, nums) -> int:
        n = len(nums)
        if not n:
            return 0
        if n == 1:
            return nums[0]
        dp = [[1, 1] for _ in range(n)] # 最大的负积与最大的正积
        res = float("-inf")
        for i in range(0, n):
            dp[i][0] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])   
            # 最负的积
            dp[i][1] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i]) 
            # 最正的积
            res = max(dp[i][1], res)
        return res

# nums = [2,3,-2,4]
# nums = [-2, 3, -4]
# nums = [3, -1, 4]
# nums = [-2, 0, -1]
# s = Solution().maxProduct(nums)
# print(s)
"""
Accepted
187/187 cases passed (48 ms)
Your runtime beats 73.87 % of python3 submissions
Your memory usage beats 5.03 % of python3 submissions (17.2 MB)
"""
# @lc code=end

