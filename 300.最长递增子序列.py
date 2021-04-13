#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n # 每个初始化为1表示自己形成的子串
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]: # 当前数字，只有与前面小于该数字的才能形成子串
                    dp[i] = max(dp[i], dp[j]+1) # 可能与前面多个子串形成递增子串，取最大的那个
        # print(dp)
        return max(dp)


# @lc code=end

