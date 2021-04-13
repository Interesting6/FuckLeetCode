#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        from collections import Counter
        cnt = Counter(nums)
        res = max(cnt.items(), key=lambda x: x[1])
        return res[0]
""" 直接count居然还这么快。。。而且内存占用也小
Accepted
46/46 cases passed (40 ms)
Your runtime beats 94.97 % of python3 submissions
Your memory usage beats 96.21 % of python3 submissions (15.9 MB)
"""


# nums = [3, 2, 3]            
# nums = [2,2,1,1,1,2,2] 
# nums = [2,2,1,1,2,3,3,3,3] 
# s = Solution().majorityElement(nums)
# print(s)


# @lc code=end

