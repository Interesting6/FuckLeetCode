#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         if n == 1:
#             return
#         if n == 2:
#             nums[0], nums[1] = nums[1], nums[0]
#             return
#         i = n-2
#         flag = True
#         while i > 0:
#             if nums[i] < nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#                 flag = False
#                 break
#             elif nums[i] > nums[i+1] and nums[i] > nums[i-1]:
#                 if nums[i-1] >= nums[i+1]:
#                     nums[i], nums[i-1] = nums[i-1], nums[i]
#                     nums[i], nums[i+1] = nums[i+1], nums[i]
#                 else:
#                     nums[i], nums[i+1] = nums[i+1], nums[i]
#                     nums[i], nums[i-1] = nums[i-1], nums[i]
#                 flag = False
#                 break
#             elif nums[i] > nums[i+1] and nums[i-1] >= nums[i]:
#                 i -= 1
#             elif nums[i] == nums[i+1]:
#                 i -= 1
#         if i == 0 and flag:
#             nums.sort()
#         return
        # 只过了70%左右。。复杂点的处理不了，有点技巧解决这个问题。

class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        if n == 1:
            return
        i = n-1
        j = -1
        while i >= 1: # 从后往前找，找到第一个前面数小于当前数的数
            if nums[i-1] < nums[i]:
                j = i - 1
                break
            i -= 1
        if i == n-1: # 最后俩元素是升序，只需交换一下
            nums[j], nums[i] = nums[i], nums[j]
        elif j == -1: # 原本就是降序，重拍
            nums.sort()
        else:
            k = n - 1
            while k > j and nums[k] <= nums[j]: # 从后往前找到第一个比num[j]大的数
                k -= 1
            nums[j], nums[k] = nums[k], nums[j] 
            nums[j+1:] = nums[j+1:][::-1] # j后面的肯定是递减的，将其逆序变为递增
        # print(nums)
        return

s = Solution().nextPermutation([0,0,4,2,1,0])


# @lc code=end

