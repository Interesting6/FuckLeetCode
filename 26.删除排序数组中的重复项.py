#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         n = len(nums)
#         if n < 2:
#             return n
#         i = 1 # 维护已处理好的序列
#         j = 1 # 遍历
#         while j < n:
#             if nums[j] > nums[i-1]: # i-1是维护好的升序序列中最后一个(最大的)，
#                 # 若后面还出现比其大，则加入维护序列中
#                 nums[j], nums[i] = nums[i], nums[j]
#                 i += 1
#             else: # 不比维护序列中最大的大，即在该序列里肯定有重复，跳过即可
#                 pass
#             j += 1
#         return i

# 2021-04-18 每日一题打卡
class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        i = 1
        pre = nums[0]
        for j in range(1, n):
            if nums[j] == pre:
                continue
            else:
                nums[i] = nums[j]
                pre = nums[j]
                i += 1
        return i
"""
Accepted
161/161 cases passed (40 ms)
Your runtime beats 91.26 % of python3 submissions
Your memory usage beats 40.94 % of python3 submissions (15.8 MB)
"""
# @lc code=end

