#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         n = len(nums)
#         if n == 1:
#             return n
#         i = 1 # 维护已经处理好的序列
#         cnt = 1
#         pre = nums[0]
#         for j in range(1, n):
#             if nums[j] == pre:
#                 if cnt < 2: # pre还可以存一个，将j的换到i
#                     nums[i], nums[j] = nums[j], nums[i]
#                     cnt += 1
#                     i += 1
#                 elif cnt >= 2:
#                     pass # i不动，j动
#             elif nums[j] != pre: # 跟上一个不相等了，肯定要放进去
#                 pre = nums[j] # 注意先将pre设为num[j]后再交换
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#                 cnt = 1
#         return i

# s = Solution().removeDuplicates([1,1,1,2,2,2,3,3])
# print(s)
"""
Accepted
164/164 cases passed (32 ms)
Your runtime beats 97.82 % of python3 submissions
Your memory usage beats 57.77 % of python3 submissions (14.9 MB)
"""

# 通解版：
class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        def process(k):
            i = 0
            for j, x in enumerate(nums):
                if i<k or nums[i-k] != x:
                    nums[i] = x
                    i += 1
            return i
        return process(2)
"""
Accepted
164/164 cases passed (36 ms)
Your runtime beats 92.83 % of python3 submissions
Your memory usage beats 60.94 % of python3 submissions (14.9 MB)
"""

# @lc code=end

