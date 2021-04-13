#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in hash_table:
                return [hash_table[x], i]
            else:
                hash_table[n] = i
# @lc code=end

