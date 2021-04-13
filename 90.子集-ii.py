#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums):
        n = len(nums)
        nums.sort()
        res = []
        pth = []
        def f(d):
            res.append(pth[:])
            for i in range(d, n):
                if i > d and nums[i] == nums[i-1]:
                    continue
                pth.append(nums[i])
                f(i+1)
                pth.pop()
        f(0)
        return res

# s = Solution().subsetsWithDup([1,2,2])
# print(s)

# @lc code=end

