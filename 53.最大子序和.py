#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
"""滑动窗口法"""
# class Solution:
#     def maxSubArray(self, nums):
#         n = len(nums)
#         res = float("-inf")
#         lf = 0
#         while lf < n:
#             if nums[lf] > 0:
#                 sum_ = 0
#                 for rt in range(lf, n):
#                     sum_ += nums[rt]
#                     res = max(res, sum_)
#                     if sum_ <= 0:
#                         lf = rt
#                         break
#             else:
#                 res = max(res, nums[lf])
#             lf += 1
#         return res
"""
Accepted
203/203 cases passed (468 ms)
Your runtime beats 5.22 % of python3 submissions
Your memory usage beats 84.05 % of python3 submissions (15.2 MB)
"""

"""动态规划
f(i)：以第i个数为结尾的连续子数组的最大和，是局部的一个最大和的连续子串，该最大和并不是全局的。
则f(i) = max{f(i-1)+n[i], n[i]} 表示加入前面的一起作为一段，还是n[i]单独为一段。
    * 若单独作为一段，则f(i-1)<0，此时f(i)=n[i]，还需要跟历史的最大res比一下
    * 若加入前面一段，则f(i-1)>0，此时f(i)=f(i-1)+n[i]，也还需要跟历史最大的res比一下
在遍历中，最后还需要将f(i)与历史中最大和res比较一下
"""
# class Solution:
#     def maxSubArray(self, nums):
#         n = len(nums)
#         pre = 0
#         res = float("-inf")
#         for i in range(n):
#             pre = max(nums[i], pre+nums[i])
#             res = max(res, pre)
#         return res



# 21-04-06 第三次做，还是不会，只是瞎猜得到结果。。
# class Solution:
#     def maxSubArray(self, nums):
#         n = len(nums)
#         dp = [0] * n
#         res = float("-inf")
#         for i in range(n):
#             dp[i] = max(dp[i-1]+nums[i], nums[i])
#             res = max(dp[i], res)
#         return res

# 21-06-03 做前缀和的时候来做
class Solution:
    def maxSubArray(self, nums):
        length = len(nums)
        # dp = [0]* length
        # res = float("-inf")
        # for i, n in enumerate(nums):
        #     dp[i] = max(nums[i], dp[i-1]+nums[i])
        #     res = max(res, dp[i])
        # return res
        preSum = 0
        min_num = 0
        res = nums[0]
        for i in range(length):
            preSum += nums[i]
            res = max(res, preSum - min_num)
            if preSum < min_num:
                min_num = preSum
        return res


# s = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# s = Solution().maxSubArray([5,4,-1, 7, 8])
# print(s)
"""
Accepted 前缀和时间复杂度牛逼
203/203 cases passed (28 ms)
Your runtime beats 99.98 % of python3 submissions
Your memory usage beats 60.73 % of python3 submissions (15.3 MB)
"""

# @lc code=end

