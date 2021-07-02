#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_table = {}
#         for i, n in enumerate(nums):
#             x = target - n
#             if x in hash_table:
#                 return [hash_table[x], i]
#             else:
#                 hash_table[n] = i

# 2021-05-29
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        di = {}
        for i, n in enumerate(nums):
            if target - n in di:
                return [di[target-n], i]
            else:
                di[n] = i

# nums = [2,7,11,15]; target = 9
# s = Solution().twoSum(nums, target)
# print(s)
"""
Accepted
54/54 cases passed (32 ms)
Your runtime beats 96.23 % of python3 submissions
Your memory usage beats 5.02 % of python3 submissions (15.8 MB)
"""

# @lc code=end

