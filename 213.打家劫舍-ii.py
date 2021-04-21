#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
# class Solution:
#     def rob(self, nums) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         if n == 2:
#             return max(nums[0], nums[1])
#         dp1 = [0] * (n-1) # 对应[0, n-1]
#         dp1[0] = nums[0]
#         dp1[1] = max(nums[0], nums[1])
#         for i in range(2, n-1):
#             dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
#         dp2 = [0] * (n-1) # 对应[1, n]
#         dp2[0] = nums[1]
#         dp2[1] = max(nums[1], nums[2])
#         for i in range(3, n): # nums里从3开始，但dp2还是从2开始
#             dp2[i-1] = max(dp2[i-2], dp2[i-3]+nums[i])
#         return max(dp1[n-2], dp2[n-2])

# 2021-04-15 第二次刷--每日一题，做对啦！
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        dp1 = [0] * (n-1)
        dp2 = [0] * (n-1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        for i in range(3, n):
            dp2[i-1] = max(dp2[i-2], dp2[i-3]+nums[i])
        res = max(dp1[-1], dp2[-1])
        return res



# @lc code=end

