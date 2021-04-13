#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         if n < 3:
#             return []
#         nums.sort() # 先排序
#         if nums[0] > 0 or nums[-1] < 0:
#             return []
#         res = []
#         for i in range(n):
#             if nums[i] > 0: # 之后的三数和肯定都大于0，不会有结果的，直接返回
#                 return res 
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue # 去重
#             # 双指针边框缩小移动
#             left = i+1
#             right = n-1
            
#             while left < right:
#                 s = nums[i] + nums[left] + nums[right]
#                 if s == 0: # 找到正确答案
#                     res.append([nums[i], nums[left], nums[right]])
#                     # 先去重，判断左界和右界是否和下一位置重复，去除重复解。
#                     while left < right and nums[right] == nums[right-1]: 
#                         right -= 1
#                     while left < right and nums[left] == nums[left+1]:
#                         left += 1
#                     # 两指针同时收缩，注意移动两指针不能合并到上面，不要漏掉！！！
#                     right -= 1
#                     left += 1
#                 elif s > 0: # 三数和大了，需要变小，移动右指针
#                     right -= 1
#                 elif s < 0: # 三数小了，需要变大，移动左指针
#                     left += 1
#         return res

"""
Accepted
318/318 cases passed (644 ms)
Your runtime beats 88.13 % of python3 submissions
Your memory usage beats 36.15 % of python3 submissions (17.5 MB)
"""

# 21-04-12 第二次做
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = []
        for i in range(0, n-2):
            if nums[i] > 0: # 别少了这个终止条件
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                if j>i+1 and nums[j] == nums[j-1]: # 去重，只需要对j做就行，不用再对k做了
                    j += 1
                    continue
                if nums[j] + nums[k] == -nums[i]:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
        return res

# nums = [-1,0,1,2,-1,-4]
# nums = [-2,0,0,0,2,2,2]
# s = Solution().threeSum(nums)
# print(s)
"""
Accepted 少了一个早跳出的终止条件
318/318 cases passed (1764 ms)
Your runtime beats 16.2 % of python3 submissions
Your memory usage beats 72.31 % of python3 submissions (17.4 MB)
"""
# @lc code=end

