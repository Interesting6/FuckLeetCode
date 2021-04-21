#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        nums = [(j,i) for i,j in enumerate(nums)]
        nums.sort()
        for ni, it in enumerate(nums):
            j = ni + 1
            while j < n and abs(nums[j][0] - it[0])<=t:
                if abs(nums[j][1] - it[1]) <= k:
                    return True
                j += 1
        return False
            
            
# nums = [1,2,3,1]
# k = 3
# t = 0
# s = Solution().containsNearbyAlmostDuplicate(nums, k, t)
# print(s)
"""
Accepted
54/54 cases passed (92 ms)
Your runtime beats 13.3 % of python3 submissions
Your memory usage beats 9.85 % of python3 submissions (17.9 MB)
"""



# @lc code=end

